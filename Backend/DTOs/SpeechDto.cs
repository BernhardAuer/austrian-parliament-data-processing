using WebApi.Enums;

namespace WebApi.DTOs;

public class SpeechDto // generics for DTOs: good or bad idea?
{
    public SpeechObjectTypeEnum Type { get; set; } // todo: does current C# version support string enums?
    public string Data { get; set; }
    public string? NameOfSpeaker { get; set; }
    public int OrderId { get; set; }

}