using System;
using System.Text.RegularExpressions;
using Microsoft.AspNetCore.Mvc;
using WebApi.Constants;
using WebApi.DTOs;
using WebApi.Enums;
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
        private readonly string _sourceOriginBaseUrl = "https://www.parlament.gv.at";

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
                    NameOfSpeakerUrlSlug = x.nameOfSpeakerUrlSlug,
                    Topic = x.topic,
                    TopicUrlSlug = x.topicUrlSlug,
                    TopNr = x.topNr,
                    PoliticalParty = x.politicalPartie,
                    TypeOfSpeech = _austrianParliamentAbbreviationMappings.GetLongNameSpeechType(x.typeOfSpeech),
                    LengthOfSpeechInSec = x.lengthOfSpeechInSec,
                    SpeechSneakPeak = GetTextWithoutSalutation(x?.speech?.FirstOrDefault(x => x.type == SpeechObjectTypeEnum.Speech)?.data),
                    SpeechNrInDebate = x.speechNrInDebate ?? 0,
                    SpeechNrOfPerson = x.nrOfSpeechByThisPerson,
                    ActivitiesCount = x?. speech == null ? new Dictionary<string, int>(): x.speech
                        .Where(y => y.parsedInfoItems != null)
                        .SelectMany(y => y.parsedInfoItems)
                        .Where(y => y.activityList != null)
                        .SelectMany(y => y.activityList)
                        .GroupBy(y => y)
                        .Select(grp => new
                        {
                            activityName = grp.Key,
                            Count = grp.Count()
                        }).ToDictionary(y => y.activityName, y => y.Count)
                })
                .ToList();
            return result;
        }

        private string? GetTextWithoutSalutation(string? input)
        {
            if (input == null)
            {
                return null;
            }

            input = input.Trim('!');
            
            var pattern = @".*\!(.*)";
            var rg = new Regex(pattern);
            var match = rg.Match(input);
            if (match.Groups.Count > 1)
            {
                return "..." + match.Groups[1].Value + "...";
            }

            return input + "...";
        }
        
        [HttpGet]
        [Route("getPureSpeeches")]
        public async Task<List<SpeechDto>> GetPureSpeeches([FromQuery] string legislature, [FromQuery] int meetingNumber, 
            [FromQuery] string topicUrlSlug, [FromQuery] string nameOfSpeakerUrlSlug, [FromQuery] int speechNrOfPerson = 0)
        {
            var speeches =
                await _speechesMetaDataService.GetPureSpeeches(legislature, meetingNumber, topicUrlSlug, nameOfSpeakerUrlSlug, speechNrOfPerson);
            List<SpeechDto> speechDtos = new List<SpeechDto>();
            foreach (var speech in speeches)
            {
                SpeechDto speechDto = null;
                switch (speech.type)
                {
                    case SpeechObjectTypeEnum.Info:
                        foreach (var infoItem in speech?.parsedInfoItems ?? Enumerable.Empty<SpeechParsedInfoItem>())
                        {
                            speechDto = null;
                            if (infoItem?.activityList?.Length > 0 && (infoItem.activityList.Contains("shouting") ||
                                                                       infoItem.activityList.Contains("shout")))
                            {
                                speechDto = new SpeechDto()
                                {
                                    NameOfSpeaker = string.Join(", ", infoItem?.entityList?.Select(x => x.name) ?? Enumerable.Empty<string>()),
                                    OrderId = speech.orderId,
                                    Data = infoItem?.quote ?? infoItem?.rawSourceText,
                                    Description = infoItem?.description,
                                    Type = infoItem?.quote != null
                                        ? SpeechObjectTypeEnum.Speech
                                        : SpeechObjectTypeEnum.Info, // speech.type,
                                    Subtype = infoItem?.quote != null
                                        ? SpeechTypes.Interjection
                                        : SpeechTypes.InterjectionWithoutQuote
                                };
                                speechDtos.Add(speechDto);
                            }

                            if (infoItem?.activityList?.Length > 0 && (infoItem.activityList.Contains("applause")))
                            {
                                speechDto = new SpeechDto()
                                {
                                    Data = infoItem?.rawSourceText,
                                    NameOfSpeaker = string.Join(", ", infoItem?.entityList?.Select(x => x.name) ?? Enumerable.Empty<string>()),
                                    OrderId = speech.orderId,
                                    Type = SpeechObjectTypeEnum.Info, // speech.type,
                                    Subtype = SpeechTypes.Applause
                                };
                                speechDtos.Add(speechDto);
                            }

                            if (infoItem?.activityList?.Length > 0 && (infoItem.activityList.Contains("cheerfulness")))
                            {
                                speechDto = new SpeechDto()
                                {
                                    Data = infoItem?.rawSourceText,
                                    NameOfSpeaker = string.Join(", ",
                                        infoItem?.entityList?.Select(x => x?.name) ?? Enumerable.Empty<string>()),
                                    OrderId = speech.orderId,
                                    Type = SpeechObjectTypeEnum.Info, // speech.type,
                                    Subtype = SpeechTypes.Cheerfulness
                                };
                                speechDtos.Add(speechDto);
                            }

                            if (speechDto == null)
                            {
                                speechDto = new SpeechDto()
                                {
                                    Data = infoItem?.rawSourceText,
                                    OrderId = speech.orderId,
                                    Type = SpeechObjectTypeEnum.Info, // speech.type,
                                    Subtype = speech.subType
                                };
                                speechDtos.Add(speechDto);
                            }
                        }
                        if (speech.subType == "time")
                        {
                            speechDto = new SpeechDto()
                            {
                                OrderId = speech.orderId,
                                Data = speech.data,
                                Type = speech.type,
                                Subtype = speech.subType
                            };
                            speechDtos.Add(speechDto);
                        }

                        if (speechDto == null)
                        {
                            speechDto = new SpeechDto()
                            {
                                OrderId = speech.orderId,
                                Data = speech.data,
                                Type = speech.type,
                                Subtype = speech.subType
                            };
                            speechDtos.Add(speechDto);
                        }
                        break;
                
                    case SpeechObjectTypeEnum.Speech:
                        speechDto = new SpeechDto()
                        {
                            NameOfSpeaker = speech.speaker,
                            PoliticalRole = speech.politicalRole,
                            OrderId = speech.orderId,
                            Data = speech.data,
                            Type = speech.type,
                            Subtype = speech.politicalRole == "presidentOfParliament"
                                ? SpeechTypes.RemarksFromPresident
                                : SpeechTypes.SpeechByMainSpeaker
                        };
                        speechDtos.Add(speechDto);
                        break;
                }
            }
            return speechDtos;
        }

        [HttpGet]
        [Route("getSpeechSourceLinks")]
        public async Task<SpeechSourceLinksDto> GetSpeechSourceLinks([FromQuery] string legislature, [FromQuery] int meetingNumber, 
            [FromQuery] string topic, [FromQuery] string nameOfSpeaker, [FromQuery] int speechNrOfPerson = 0)
        {
            var sourceLinks =
                await _speechesMetaDataService.GetSpeechSourceLinks(legislature, meetingNumber, topic, nameOfSpeaker, speechNrOfPerson);

            return new SpeechSourceLinksDto { SpeechUrl = _sourceOriginBaseUrl + sourceLinks?.speechUrl, VideoUrl = _sourceOriginBaseUrl + sourceLinks?.videoUrl };
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
