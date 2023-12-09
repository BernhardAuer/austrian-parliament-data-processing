using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using WebApi.Enums;

namespace WebApi.Models;

[BsonIgnoreExtraElements]
public class SpeechParsedInfoItemEntity
{
    public string type { get; set; }
    public string name { get; set; }
}