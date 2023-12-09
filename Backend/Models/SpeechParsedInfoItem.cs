using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using WebApi.Enums;

namespace WebApi.Models;

[BsonIgnoreExtraElements]
public class SpeechParsedInfoItem
{
    public string[] activityList { get; set; }
    public SpeechParsedInfoItemEntity[] entityList { get; set; }
}