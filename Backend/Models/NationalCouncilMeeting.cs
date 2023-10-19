using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace WebApi.Models;

public class NationalCouncilMeeting
{
    [BsonId]
    [BsonElement("_id")]
    [BsonRepresentation(BsonType.ObjectId)]
    public string? Id { get; set; }
    public string? name { get; set; }
    public DateTime date { get; set; }
    public string? legislativePeriod { get; set; }
    public string? meetingType { get; set; }
    public int? meetingNumber { get; set; }
    public int? meetingDay { get; set; }
    public string link { get; set; } 
    
}