using System;
using Microsoft.AspNetCore.Mvc;
using WebApi.DTOs;
using WebApi.Services;
using WebApi.Mappings;

namespace WebApi.Controllers;

[Route("api/[controller]")]
[ApiController]
public class SpeechesController : ControllerBase
{
    private readonly SpeechesMetaDataService _speechesMetaDataService;

    public SpeechesController(SpeechesMetaDataService speechesMetaDataService,
        AustrianParliamentAbbreviationMappings austrianParliamentAbbreviationMappings)
    {
        _speechesMetaDataService = speechesMetaDataService;
    }

    [HttpGet]
    [Route("getPureSpeeches")]
    public async Task<List<SpeechDto>> GetPureSpeeches([FromQuery] string legislature, [FromQuery] int meetingNumber, 
         [FromQuery] int speechNrInDebate, [FromQuery] string topic)
    {
        var speeches =
            await _speechesMetaDataService.GetPureSpeeches(legislature, meetingNumber, topic, speechNrInDebate);

        var result = speeches.Select(x => new SpeechDto()
            {
                NameOfSpeaker = x.speaker,
                OrderId = x.orderId,
                Data = x.data,
                Type = x.type
            })
            .ToList();
        return result;
    }
}