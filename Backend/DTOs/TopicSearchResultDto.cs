namespace WebApi.DTOs;

public class TopicSearchResultDto
{
    public string Topic { get; set; }
    public string TopNr { get; set; }
    public int? MeetingNr { get; set; }
    public string Legislature { get; set; }
}