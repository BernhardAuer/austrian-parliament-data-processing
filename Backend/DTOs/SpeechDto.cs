using WebApi.Enums;

namespace WebApi.DTOs;

public class SpeechDto // generics for DTOs: good or bad idea?
{
    public SpeechObjectTypeEnum Type { get; set; } // todo: does current C# version support string enums?
    
    public string Subtype { get; set; }
    public string Data { get; set; }
    public string? NameOfSpeaker { get; set; }
    public string? Activity { get; set; }
    public string? PoliticalRole { get; set; }
    public int OrderId { get; set; }

}