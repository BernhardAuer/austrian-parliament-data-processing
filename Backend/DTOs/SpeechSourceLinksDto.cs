namespace WebApi.DTOs;

public class SpeechSourceLinksDto
{
    public string? VideoUrl { get; set; }
    public string? SpeechUrl { get; set; }
    
    public string? NameOfSpeaker { get; set; }
    public string? Topic { get; set; }
}