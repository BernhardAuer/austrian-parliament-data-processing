using Microsoft.Extensions.Options;
using MongoDB.Driver;
using RomanNumerals;
using WebApi.DTOs;
using WebApi.Models;

namespace WebApi.Services;

public class NationalCouncilMeetingService
{
    private readonly IMongoCollection<NationalCouncilMeeting> _nationalCouncilMeetingCollection;
    private readonly ILogger<NationalCouncilMeetingService> _logger;

    public NationalCouncilMeetingService(ILogger<NationalCouncilMeetingService> logger,
        IOptions<AustrianParliamentScrapeDatabaseSettings> austrianParliamentScrapeDatabaseSettings)
    {
        var mongoClient = new MongoClient(austrianParliamentScrapeDatabaseSettings.Value.ConnectionString);
        var mongoDatabase = mongoClient.GetDatabase(austrianParliamentScrapeDatabaseSettings.Value.DatabaseName);

        _nationalCouncilMeetingCollection = mongoDatabase
            .GetCollection<NationalCouncilMeeting>(austrianParliamentScrapeDatabaseSettings.Value
                .NationalCouncilCollectionName);
        _logger = logger;
    }
    
    public async Task<List<Tuple<int, int>>> GetNationalCouncilMeetingsOfYear(int year)
    {
        var query = _nationalCouncilMeetingCollection
            .Aggregate()
            .Match(x => x.date.Year == year);
        var result = await query
            .Group(key => key.date.Month,
                group => new Tuple<int, int>(group.Key, group.Count()))
            .SortBy(x => x.Item1)
            .ToListAsync();

        if (!result.Any())
        {
            return result;
        }
        
        // add months with zero meetings
        var allMonths = Enumerable.Range(1, 12);
        var missingMonths = allMonths.Except(result.Select(x => x.Item1));
        result.AddRange(missingMonths.Select(month => new Tuple<int, int>(month, 0)));
        result = result.OrderBy(x => x.Item1).ToList();
        return result;
    }

}