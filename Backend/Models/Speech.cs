using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using WebApi.Enums;

namespace WebApi.Models;

[BsonIgnoreExtraElements]
public class Speech
{
    public SpeechObjectTypeEnum type { get; set; } // todo: does current C# version support string enums?
    public string? subType { get; set; } // todo: does current C# version support string enums?
    public string data { get; set; }
    public string? speaker { get; set; }
    
    public string? politicalRole { get; set; }
    public int orderId { get; set; }
    
    public SpeechParsedInfoItem[] parsedInfoItems { get; set; }
}