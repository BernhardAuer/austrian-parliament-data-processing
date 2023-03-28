using Microsoft.Extensions.Options;
using MongoDB.Bson;
using MongoDB.Bson.Serialization;
using MongoDB.Driver;
using WebApi.DTOs;
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

    public async Task<List<TypeOfSpeechCount>> GetTypeOfSpeechesCountList(TypeOfSpeechFilterDto typeOfSpeechFilterDto)
    {
        var query = _speechesMetaDataCollection
            .Aggregate()
            .Match(x => typeOfSpeechFilterDto.PoliticalParty.Any(pp => pp == x.politicalPartie));
        
        if (typeOfSpeechFilterDto.Legislature != null)
        {
            query = query.Match(x => x.legislature == typeOfSpeechFilterDto.Legislature);
        }
        
        if (typeOfSpeechFilterDto.MeetingNumber != null)
        {
            query = query.Match(x => x.meetingNr == typeOfSpeechFilterDto.MeetingNumber);
        }
        
        if (typeOfSpeechFilterDto.TopNumber != null)
        {
            query = query.Match(x => x.topNr == typeOfSpeechFilterDto.TopNumber);
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

    public async Task<List<SpeechesMetaData>> GetAsync()
    {
        return await _speechesMetaDataCollection.Find(x => true)
            .Project(x => new SpeechesMetaData
        {
            Id = x.Id,
            nameOfSpeaker = x.nameOfSpeaker
        }).ToListAsync();
    }

    public async Task<SpeechesMetaData?> GetAsync(string id) =>
        await _speechesMetaDataCollection.Find(x => x.Id == id).FirstOrDefaultAsync();

    public async Task CreateAsync(SpeechesMetaData newSpeechesMetaData) =>
        await _speechesMetaDataCollection.InsertOneAsync(newSpeechesMetaData);

    public async Task UpdateAsync(string id, SpeechesMetaData updatedSpeechesMetaData) =>
        await _speechesMetaDataCollection.ReplaceOneAsync(x => x.Id == id, updatedSpeechesMetaData);

    public async Task RemoveAsync(string id) =>
        await _speechesMetaDataCollection.DeleteOneAsync(x => x.Id == id);

    public async Task<List<LegislatureMeetingsListDto>> GetLegislaturesAndMeetings()
    {
        return await _speechesMetaDataCollection.Aggregate().Group(key => key.legislature,
            group => new LegislatureMeetingsListDto()
            {
                Legislature = group.Key,
                Meetings = group.Where(x => x.meetingNr != null).Select(x => x.meetingNr!.Value).Distinct().ToArray()
            }).ToListAsync();

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
}