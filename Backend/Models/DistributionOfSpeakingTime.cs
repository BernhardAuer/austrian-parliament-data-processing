namespace WebApi.Models;

public class DistributionOfSpeakingTime
{
    public string PoliticalParty { get; set; }
    public double SpeechDurationPercentage { get; set; }
    public int SpeechDurationByParty { get; set; }
    
    public double NumberOfSpeechesPercentage { get; set; }
    public int NumberOfSpeechesByParty { get; set; }

}