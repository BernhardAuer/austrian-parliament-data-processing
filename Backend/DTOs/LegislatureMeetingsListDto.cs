namespace WebApi.DTOs;

public class LegislatureMeetingsListDto
{ 
   public string Legislature { get; set; }
   public int[] Meetings { get; set; } = Array.Empty<int>();
}