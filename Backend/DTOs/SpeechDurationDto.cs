namespace WebApi.DTOs;

public class SpeechDurationDto
{
    public string? PoliticalParty { get; set; }
    public string? Speaker { get; set; }
    public int DurationSumInSec { get; set; }
    public int TotalNumberOfSpeeches { get; set; }
}