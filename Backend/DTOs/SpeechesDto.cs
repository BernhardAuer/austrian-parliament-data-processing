namespace WebApi.DTOs;

public class SpeechesDto
{
    public string NameOfSpeaker { get; set; }
    public string NameOfSpeakerUrlSlug { get; set; }
    public string TypeOfSpeech { get; set; }
    public int LengthOfSpeechInSec { get; set; }
    public string TopNr { get; set; }
    public string Topic { get; set; }
    public string TopicUrlSlug { get; set; }
    public string PoliticalParty { get; set; }
    public string? SpeechSneakPeak { get; set; }
    
    public int SpeechNrInDebate { get; set; }
    public int SpeechNrOfPerson { get; set; }
    
    public Dictionary<string, int> ActivitiesCount { get; set; }

}