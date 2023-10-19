using System;
using Microsoft.AspNetCore.Mvc;
using WebApi.DTOs;
using WebApi.Models;
using WebApi.Services;

namespace WebApi.Controllers;

[Route("api/[controller]")]
[ApiController]
public class NationalCouncilMeetingController : ControllerBase
{
    private readonly NationalCouncilMeetingService _nationalCouncilMeetingService;

    public NationalCouncilMeetingController(NationalCouncilMeetingService nationalCouncilMeetingService)
    {
        _nationalCouncilMeetingService = nationalCouncilMeetingService;
    }

    [HttpGet]
    [Route("getNationalCouncilMeetings")]
    public async Task<List<NationalCouncilMeetingsPerYearDto>> GetNationalCouncilMeetings([FromQuery] int year)
    {
        var speeches = await _nationalCouncilMeetingService.GetNationalCouncilMeetingsOfYear(year);

        var result = speeches.Select(x => new NationalCouncilMeetingsPerYearDto()
            {
                Month = x.Item1,
                Count = x.Item2

            })
            .ToList();
        return result;
    }
}

