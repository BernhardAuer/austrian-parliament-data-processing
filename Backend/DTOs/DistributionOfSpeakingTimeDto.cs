namespace WebApi.DTOs;

public class DistributionOfSpeakingTimeDto
{
    public string PoliticalParty { get; set; }
    public double SpeechDurationPercentage { get; set; }
    public double NumberOfSpeechesPercentage { get; set; }

}