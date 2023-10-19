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
        return result;
    }

}