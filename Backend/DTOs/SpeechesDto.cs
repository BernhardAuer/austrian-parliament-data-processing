namespace WebApi.DTOs;

public class SpeechesDto
{
    public string NameOfSpeaker { get; set; }
    public string TypeOfSpeech { get; set; }
    public int LengthOfSpeechInSec { get; set; }
    public string TopNr { get; set; }
    public string Topic { get; set; }
    public string PoliticalPartie { get; set; }
    public string Speech { get; set; }

}