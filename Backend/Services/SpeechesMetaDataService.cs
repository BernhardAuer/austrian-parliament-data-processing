using Microsoft.Extensions.Options;
using MongoDB.Driver;
using MongoDB.Driver.Linq;
using RomanNumerals;
using WebApi.DTOs;
using WebApi.Enums;
using WebApi.Models;

namespace WebApi.Services;

public class SpeechesMetaDataService
{
    private readonly IMongoCollection<SpeechesMetaData> _speechesMetaDataCollection;
    private readonly ILogger<SpeechesMetaDataService> _logger;

    public SpeechesMetaDataService(ILogger<SpeechesMetaDataService> logger,
        IOptions<AustrianParliamentScrapeDatabaseSettings> austrianParliamentScrapeDatabaseSettings)
    {
        var mongoClient = new MongoClient(austrianParliamentScrapeDatabaseSettings.Value.ConnectionString);
        var mongoDatabase = mongoClient.GetDatabase(austrianParliamentScrapeDatabaseSettings.Value.DatabaseName);

        _speechesMetaDataCollection = mongoDatabase
            .GetCollection<SpeechesMetaData>(austrianParliamentScrapeDatabaseSettings.Value
                .SpeechesMetaDataCollectionName);
        _logger = logger;
    }
    
    public async Task<List<SpeechesMetaData>> GetSpeeches(string legislature, int meetingNumber)
    {
        var query = _speechesMetaDataCollection
            .Aggregate()
            .Match(x => x.legislature == legislature && x.meetingNr == meetingNumber);
        
        var result = await query
            .SortBy(x => x.topNr)
            .SortBy(x => x.topic)
            .SortBy(x => x.typeOfSpeech)
            .Project(x => new SpeechesMetaData
            {
                nameOfSpeaker = x.nameOfSpeaker,
                typeOfSpeech = x.typeOfSpeech,
                lengthOfSpeechInSec = x.lengthOfSpeechInSec,
                topNr = x.topNr,
                topic = x.topic,
                politicalPartie = x.politicalPartie,
                speechNrInDebate = x.speechNrInDebate,
                nrOfSpeechByThisPerson = x.nrOfSpeechByThisPerson,
                speech = x.speech
            })
            .ToListAsync();
        
        return result;
    }

    public async Task<List<Speech>> GetPureSpeeches(string legislature, int meetingNumber, string topic, string nameOfSpeaker, int speechNrOfPerson)
    {
        var query = _speechesMetaDataCollection
            .Aggregate()
            .Match(x => x.legislature == legislature && x.meetingNr == meetingNumber 
                                                     && x.topic == topic
                                                     && x.nameOfSpeaker == nameOfSpeaker
                                                     && x.nrOfSpeechByThisPerson == speechNrOfPerson);
        
        var result = await query.Limit(1)
            .Project(x => x.speech)
            .FirstOrDefaultAsync();
        return result.ToList();
    }
    
    public async Task<dynamic> GetSpeechSourceLinks(string legislature, int meetingNumber, string topic, string nameOfSpeaker, int speechNrOfPerson)
    {
        var query = _speechesMetaDataCollection
            .Aggregate()
            .Match(x => x.legislature == legislature && x.meetingNr == meetingNumber 
                                                     && x.topic == topic
                                                     && x.nameOfSpeaker == nameOfSpeaker
                                                     && x.nrOfSpeechByThisPerson == speechNrOfPerson);
        
        var result = await query.Limit(1)
            .Project(x => new { x.videoUrl, x.speechUrl })
            .FirstOrDefaultAsync();
        return result;
    }

    public async Task<List<TypeOfSpeechCount>> GetTypeOfSpeechesCountList(TypeOfSpeechFilterDto typeOfSpeechFilterDto)
    {
        var query = _speechesMetaDataCollection
            .Aggregate()
            .Match(x => typeOfSpeechFilterDto.PoliticalParty.Any(pp => pp == x.politicalPartie));
        
        if (typeOfSpeechFilterDto.Legislature != null)
        {
            query = query.Match(x => x.legislature == typeOfSpeechFilterDto.Legislature);
        }
        else
        {
            query = query.Match(x => x.legislature == "XXVII"); // hardcoded for now, pls fix this
        }
        
        if (typeOfSpeechFilterDto.MeetingNumber != null)
        {
            query = query.Match(x => x.meetingNr == typeOfSpeechFilterDto.MeetingNumber);
        }
        else
        {
            var maxMeetingNumber = await _speechesMetaDataCollection.Aggregate().Match(x => x.legislature == "XXVII")
                .SortByDescending(x => x.meetingNr).Project(x => x.meetingNr).FirstOrDefaultAsync();
            query = query.Match(x => x.meetingNr == maxMeetingNumber);
        }
        
        if (typeOfSpeechFilterDto.Topic != null)
        {
            query = query.Match(x => x.topic == typeOfSpeechFilterDto.Topic);
        }

        return await query
            .SortByCount(x => x.typeOfSpeech)
            .Project(x => new TypeOfSpeechCount()
            {
                TypeOfSpeech = x.Id!.ToString(),
                Count = x.Count
            })
            .ToListAsync();
    }
  
    public async Task<List<LegislatureMeetingsListDto>> GetLegislaturesAndMeetings()
    {
        var legislaturesAndMeetings = await _speechesMetaDataCollection.Aggregate()
            .SortBy(x => x.legislature) // this is needed, so that groupBy utilizes index
            .ThenBy(x => x.meetingNr) // this is needed, so that groupBy utilizes index
            .Group(key => key.legislature,
            group => new LegislatureMeetingsListDto()
            {
                Legislature = group.Key,
                Meetings = group.Select(x => x.meetingNr!.Value).Distinct().ToArray()
            }).ToListAsync();

        legislaturesAndMeetings.ForEach(x => x.LegislatureAsInt = (new RomanNumeral(x.Legislature)).ToInt());
        var sortedLegislaturesAndMeetings = legislaturesAndMeetings.OrderBy(x => x.LegislatureAsInt).ToList();
        return sortedLegislaturesAndMeetings;
    }
    
    public async Task<List<TopicSearchResultDto>> SearchTopicsByName(string? searchTerm, string? legislature, int? meetingNumber)
    {
        if ((searchTerm is null && meetingNumber is null) || (searchTerm is null && legislature is null))
        {
            return new List<TopicSearchResultDto>();
        }
        
        var query = _speechesMetaDataCollection
            .Aggregate(new AggregateOptions{Collation = new Collation(locale:"de", numericOrdering: true)});

        if (searchTerm is not null)
        {
            query
                .Match(Builders<SpeechesMetaData>.Filter.Text(searchTerm))
                .AppendStage<SpeechesMetaData>("{$addFields: {textMatchScore: {$meta:'textScore'}}}");
        }

        if (legislature is not null)
        {
            query = query.Match(x => x.legislature == legislature);
        }     
        
        if (meetingNumber is not null)
        {
            query = query.Match(x => x.meetingNr == meetingNumber);
        }

        IAggregateFluent<TopicSearchResultDto>? groupedQuery;
        if (searchTerm is not null)
        {
            groupedQuery = query
                .Group(key => key.topic,
                    group => new TopicSearchResultDto()
                    {
                        Topic = group.Key,
                        TopNr = group.First().topNr,
                        Legislature = group.First().legislature,
                        MeetingNr = group.First().meetingNr,
                        TextMatchScore = group.First().textMatchScore
                    })
                .SortByDescending(x => x.TextMatchScore)
                .ThenBy(x => x.TopNr)
                .Limit(25);
        }
        else
        {
            groupedQuery = query
                .Group(key => key.topic,
                    group => new TopicSearchResultDto()
                    {
                        Topic = group.Key,
                        TopNr = group.First().topNr,
                        Legislature = group.First().legislature,
                        MeetingNr = group.First().meetingNr
                    })
                .SortBy(x => x.TopNr)
                .Limit(100);
        }
        
        return await groupedQuery.ToListAsync();
    }
    public async Task<List<SpeechDuration>> GetSpeechDurations(TypeOfSpeechFilterDto typeOfSpeechFilterDto)
    {
        var query = _speechesMetaDataCollection
            .Aggregate()
            .Match(x => typeOfSpeechFilterDto.PoliticalParty.Any(pp => pp == x.politicalPartie));
        
        if (typeOfSpeechFilterDto.Legislature != null)
        {
            query = query.Match(x => x.legislature == typeOfSpeechFilterDto.Legislature);
        }
        else
        {
            query = query.Match(x => x.legislature == "XXVII"); // hardcoded for now, pls fix this
        }
        
        if (typeOfSpeechFilterDto.MeetingNumber != null)
        {
            query = query.Match(x => x.meetingNr == typeOfSpeechFilterDto.MeetingNumber);
        }
        else
        {
            var maxMeetingNumber = await _speechesMetaDataCollection.Aggregate().Match(x => x.legislature == "XXVII")
                .SortByDescending(x => x.meetingNr).Project(x => x.meetingNr).FirstOrDefaultAsync();
            query = query.Match(x => x.meetingNr == maxMeetingNumber);
        }
        
        if (typeOfSpeechFilterDto.Topic != null)
        {
            query = query.Match(x => x.topic == typeOfSpeechFilterDto.Topic);
        }

        return await query
            .Group(x => x.nameOfSpeaker, g => new  SpeechDuration()
            {
                Speaker = g.Key,
                PoliticalParty = g.First().politicalPartie,
                TotalNumberOfSpeeches = g.Count(),
                DurationSumInSec = g.Sum(x => x.lengthOfSpeechInSec)
            })
            .ToListAsync();
    }
    
    public async Task<List<DistributionOfSpeakingTime>> GetDistributionOfSpeakingTime(TypeOfSpeechFilterDto typeOfSpeechFilterDto)
    {
        var query = _speechesMetaDataCollection
            .Aggregate()
            .Match(x => typeOfSpeechFilterDto.PoliticalParty.Any(pp => pp == x.politicalPartie));
        
        if (typeOfSpeechFilterDto.Legislature != null)
        {
            query = query.Match(x => x.legislature == typeOfSpeechFilterDto.Legislature);
        }
        else
        {
            query = query.Match(x => x.legislature == "XXVII"); // hardcoded for now, pls fix this
        }
        
        if (typeOfSpeechFilterDto.MeetingNumber != null)
        {
            query = query.Match(x => x.meetingNr == typeOfSpeechFilterDto.MeetingNumber);
        }
        else
        {
            var maxMeetingNumber = await _speechesMetaDataCollection.Aggregate().Match(x => x.legislature == "XXVII")
                .SortByDescending(x => x.meetingNr).Project(x => x.meetingNr).FirstOrDefaultAsync();
            query = query.Match(x => x.meetingNr == maxMeetingNumber);
        }
        
        if (typeOfSpeechFilterDto.Topic != null)
        {
            query = query.Match(x => x.topic == typeOfSpeechFilterDto.Topic);
        }

        var distributionOfSpeakingTimes = await query
            .Group(x => x.politicalPartie, g => new  DistributionOfSpeakingTime()
            {
                PoliticalParty = g.Key,
                SpeechDurationByParty = g.Sum(x => x.lengthOfSpeechInSec),
                NumberOfSpeechesByParty = g.Count()
            })
            .ToListAsync();

        var totalNrOfSpeeches = (await query.Count().FirstOrDefaultAsync())?.Count ?? 0;
        // it seems as you need to do a group by in order to get the sum of a single field
        // https://stackoverflow.com/questions/63337061/how-to-sum-the-value-of-a-key-across-all-documents-in-a-mongodb-collection-with
        var totalSpeechDuration = (await query
            .Group(key => "", group =>  group.Sum(x => x.lengthOfSpeechInSec))
            .ToListAsync()
            ).FirstOrDefault();

        foreach (var distributionOfSpeakingTime in distributionOfSpeakingTimes)
        {
            distributionOfSpeakingTime.SpeechDurationPercentage = (distributionOfSpeakingTime.SpeechDurationByParty / (double) totalSpeechDuration) * 100;
            distributionOfSpeakingTime.NumberOfSpeechesPercentage = (distributionOfSpeakingTime.NumberOfSpeechesByParty / (double) totalNrOfSpeeches) * 100;
        }

        return distributionOfSpeakingTimes;
    }
}