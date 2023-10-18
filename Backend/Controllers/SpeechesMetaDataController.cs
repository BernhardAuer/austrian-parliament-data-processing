using System;
using Microsoft.AspNetCore.Mvc;
using WebApi.DTOs;
using WebApi.Models;
using WebApi.Services;
using WebApi.Mappings;

namespace WebApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SpeechesMetaDataController : ControllerBase
    {
        private readonly SpeechesMetaDataService _speechesMetaDataService;
        private readonly AustrianParliamentAbbreviationMappings _austrianParliamentAbbreviationMappings;

        public SpeechesMetaDataController(SpeechesMetaDataService speechesMetaDataService, AustrianParliamentAbbreviationMappings austrianParliamentAbbreviationMappings)
        {
            _speechesMetaDataService = speechesMetaDataService;
            _austrianParliamentAbbreviationMappings = austrianParliamentAbbreviationMappings;
        }
        
        [HttpGet]
        [Route("getSpeeches")]
        public async Task<List<SpeechesDto>> GetSpeeches([FromQuery] string legislature, [FromQuery] int meetingNumber)
        {
            var speeches = await _speechesMetaDataService.GetSpeeches(legislature, meetingNumber);
            
            var result = speeches.Select(x => new SpeechesDto()
                {
                    NameOfSpeaker = x.nameOfSpeaker,
                    Topic = x.topic,
                    TopNr = x.topNr,
                    PoliticalPartie = x.politicalPartie,
                    TypeOfSpeech = _austrianParliamentAbbreviationMappings.GetLongNameSpeechType(x.typeOfSpeech),
                    LengthOfSpeechInSec = x.lengthOfSpeechInSec,
                    Speech = ""
                    
                })
                .ToList();
            return result;
        }
        
        [HttpGet]
        [Route("getTypeOfSpeechesCountList")]
        public async Task<List<TypeOfSpeechCountDto>> GetTypeOfSpeechesCountList([FromQuery] TypeOfSpeechFilterDto typeOfSpeechFilterDto)
        {
            var speechesCountList = await _speechesMetaDataService.GetTypeOfSpeechesCountList(typeOfSpeechFilterDto);
            // use automapper in the future
            var result = speechesCountList.Select(x => new TypeOfSpeechCountDto()
                {
                    TypeOfSpeech = _austrianParliamentAbbreviationMappings.GetLongNameSpeechType(x.TypeOfSpeech),
                    Count = x.Count
                })
                .OrderBy(x => x.TypeOfSpeech)
                .ToList();
            return result;
        }
        
        [HttpGet]
        [Route("searchTopics")]
        public async Task<List<TopicSearchResultDto>> SearchTopics([FromQuery] string? searchTerm, 
            [FromQuery] string? legislature, [FromQuery] int? meetingNumber)
        {
            var speechMetaData = await _speechesMetaDataService.SearchTopicsByName(searchTerm, legislature, meetingNumber);
            
            return speechMetaData;
        }
        
        [HttpGet]
        [Route("getLegislaturesAndMeetingNumbers")]
        public async Task<List<LegislatureMeetingsListDto>> GetLegislaturesAndMeetingNumbers()
        {
            var legislaturesAndMeetings = await _speechesMetaDataService.GetLegislaturesAndMeetings();
            
            return legislaturesAndMeetings;
        }
        
        [HttpGet]
        [Route("getSpeechDurations")]
        public async Task<List<SpeechDurationDto>> GetSpeechDurations([FromQuery] TypeOfSpeechFilterDto typeOfSpeechFilterDto)
        {
            var speechDurations = await _speechesMetaDataService.GetSpeechDurations(typeOfSpeechFilterDto);

            var result = speechDurations.Select(x => new SpeechDurationDto()
                {
                    Speaker = x.Speaker,
                    PoliticalParty = x.PoliticalParty,
                    DurationSumInSec = x.DurationSumInSec,
                    TotalNumberOfSpeeches = x.TotalNumberOfSpeeches
                })
                .OrderBy(x => x.PoliticalParty)
                .ThenBy(x => x.Speaker)
                .ToList();
            return result;
        }
        
        [HttpGet]
        [Route("getDistributionOfSpeakingTime")]
        public async Task<List<DistributionOfSpeakingTimeDto>> GetDistributionOfSpeakingTime([FromQuery] TypeOfSpeechFilterDto typeOfSpeechFilterDto)
        {
            var distributionOfSpeakingTimes = await _speechesMetaDataService.GetDistributionOfSpeakingTime(typeOfSpeechFilterDto);

            var result = distributionOfSpeakingTimes.Select(x => new DistributionOfSpeakingTimeDto()
                {
                    PoliticalParty = x.PoliticalParty,
                    SpeechDurationPercentage = x.SpeechDurationPercentage,
                    NumberOfSpeechesPercentage = x.NumberOfSpeechesPercentage
                })
                .ToList();
            return result;
        }
    }
}
