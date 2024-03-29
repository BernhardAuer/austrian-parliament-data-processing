using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace WebApi.Models;

public class SpeechesMetaData
{
    [BsonId]
    [BsonElement("_id")]
    [BsonRepresentation(BsonType.ObjectId)]
    public string? Id { get; set; }
    public string? nameOfSpeaker { get; set; }
    public string? nameOfSpeakerUrlSlug { get; set; }
    public int nrOfSpeechByThisPerson { get; set; }
    public string? typeOfSpeech { get; set; }
    public DateTime startDateTime { get; set; }
    public bool timeLimitInSec { get; set; }
    public bool isVoluntaryTimeLimit { get; set; }
    public int lengthOfSpeechInSec { get; set; }
    public string? nationalCouncilMeetingTitle { get; set; }
    public string? topic { get; set; }
    public string? topicUrlSlug { get; set; }
    public bool hasSpeechFinished { get; set; }
    
    public string politicalPartie { get; set; }
    public string topNr { get; set; }
    public int? meetingNr { get; set; }
    public string legislature { get; set; } 
    
    [BsonIgnoreIfNull]
    public double? textMatchScore { get; set; }
    
    public int? speechNrInDebate { get; set; }
    
    public Speech[]? speech { get; set; }
    public string? speechUrl { get; set; } 
    public string? videoUrl { get; set; } 
    
}