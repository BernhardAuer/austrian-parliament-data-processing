# WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiSpeechesMetaDataGetDistributionOfSpeakingTimeGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetDistributionOfSpeakingTimeGet) | **GET** /api/SpeechesMetaData/getDistributionOfSpeakingTime | 
[**apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet) | **GET** /api/SpeechesMetaData/getLegislaturesAndMeetingNumbers | 
[**apiSpeechesMetaDataGetPureSpeechesGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetPureSpeechesGet) | **GET** /api/SpeechesMetaData/getPureSpeeches | 
[**apiSpeechesMetaDataGetSpeechDurationsGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetSpeechDurationsGet) | **GET** /api/SpeechesMetaData/getSpeechDurations | 
[**apiSpeechesMetaDataGetSpeechSourceLinksGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetSpeechSourceLinksGet) | **GET** /api/SpeechesMetaData/getSpeechSourceLinks | 
[**apiSpeechesMetaDataGetSpeechesGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetSpeechesGet) | **GET** /api/SpeechesMetaData/getSpeeches | 
[**apiSpeechesMetaDataGetTypeOfSpeechesCountListGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetTypeOfSpeechesCountListGet) | **GET** /api/SpeechesMetaData/getTypeOfSpeechesCountList | 
[**apiSpeechesMetaDataSearchTopicsGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataSearchTopicsGet) | **GET** /api/SpeechesMetaData/searchTopics | 



## apiSpeechesMetaDataGetDistributionOfSpeakingTimeGet

> [DistributionOfSpeakingTimeDto] apiSpeechesMetaDataGetDistributionOfSpeakingTimeGet(opts)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
let opts = {
  'politicalParty': ["null"], // [String] | 
  'legislature': "legislature_example", // String | 
  'meetingNumber': 56, // Number | 
  'topic': "topic_example" // String | 
};
apiInstance.apiSpeechesMetaDataGetDistributionOfSpeakingTimeGet(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **politicalParty** | [**[String]**](String.md)|  | [optional] 
 **legislature** | **String**|  | [optional] 
 **meetingNumber** | **Number**|  | [optional] 
 **topic** | **String**|  | [optional] 

### Return type

[**[DistributionOfSpeakingTimeDto]**](DistributionOfSpeakingTimeDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet

> [LegislatureMeetingsListDto] apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet()



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
apiInstance.apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[LegislatureMeetingsListDto]**](LegislatureMeetingsListDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## apiSpeechesMetaDataGetPureSpeechesGet

> [SpeechDto] apiSpeechesMetaDataGetPureSpeechesGet(opts)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
let opts = {
  'legislature': "legislature_example", // String | 
  'meetingNumber': 56, // Number | 
  'topic': "topic_example", // String | 
  'nameOfSpeaker': "nameOfSpeaker_example", // String | 
  'speechNrOfPerson': 0 // Number | 
};
apiInstance.apiSpeechesMetaDataGetPureSpeechesGet(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legislature** | **String**|  | [optional] 
 **meetingNumber** | **Number**|  | [optional] 
 **topic** | **String**|  | [optional] 
 **nameOfSpeaker** | **String**|  | [optional] 
 **speechNrOfPerson** | **Number**|  | [optional] [default to 0]

### Return type

[**[SpeechDto]**](SpeechDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## apiSpeechesMetaDataGetSpeechDurationsGet

> [SpeechDurationDto] apiSpeechesMetaDataGetSpeechDurationsGet(opts)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
let opts = {
  'politicalParty': ["null"], // [String] | 
  'legislature': "legislature_example", // String | 
  'meetingNumber': 56, // Number | 
  'topic': "topic_example" // String | 
};
apiInstance.apiSpeechesMetaDataGetSpeechDurationsGet(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **politicalParty** | [**[String]**](String.md)|  | [optional] 
 **legislature** | **String**|  | [optional] 
 **meetingNumber** | **Number**|  | [optional] 
 **topic** | **String**|  | [optional] 

### Return type

[**[SpeechDurationDto]**](SpeechDurationDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## apiSpeechesMetaDataGetSpeechSourceLinksGet

> SpeechSourceLinksDto apiSpeechesMetaDataGetSpeechSourceLinksGet(opts)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
let opts = {
  'legislature': "legislature_example", // String | 
  'meetingNumber': 56, // Number | 
  'topic': "topic_example", // String | 
  'nameOfSpeaker': "nameOfSpeaker_example", // String | 
  'speechNrOfPerson': 0 // Number | 
};
apiInstance.apiSpeechesMetaDataGetSpeechSourceLinksGet(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legislature** | **String**|  | [optional] 
 **meetingNumber** | **Number**|  | [optional] 
 **topic** | **String**|  | [optional] 
 **nameOfSpeaker** | **String**|  | [optional] 
 **speechNrOfPerson** | **Number**|  | [optional] [default to 0]

### Return type

[**SpeechSourceLinksDto**](SpeechSourceLinksDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## apiSpeechesMetaDataGetSpeechesGet

> [SpeechesDto] apiSpeechesMetaDataGetSpeechesGet(opts)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
let opts = {
  'legislature': "legislature_example", // String | 
  'meetingNumber': 56 // Number | 
};
apiInstance.apiSpeechesMetaDataGetSpeechesGet(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legislature** | **String**|  | [optional] 
 **meetingNumber** | **Number**|  | [optional] 

### Return type

[**[SpeechesDto]**](SpeechesDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## apiSpeechesMetaDataGetTypeOfSpeechesCountListGet

> [TypeOfSpeechCountDto] apiSpeechesMetaDataGetTypeOfSpeechesCountListGet(opts)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
let opts = {
  'politicalParty': ["null"], // [String] | 
  'legislature': "legislature_example", // String | 
  'meetingNumber': 56, // Number | 
  'topic': "topic_example" // String | 
};
apiInstance.apiSpeechesMetaDataGetTypeOfSpeechesCountListGet(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **politicalParty** | [**[String]**](String.md)|  | [optional] 
 **legislature** | **String**|  | [optional] 
 **meetingNumber** | **Number**|  | [optional] 
 **topic** | **String**|  | [optional] 

### Return type

[**[TypeOfSpeechCountDto]**](TypeOfSpeechCountDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## apiSpeechesMetaDataSearchTopicsGet

> [TopicSearchResultDto] apiSpeechesMetaDataSearchTopicsGet(opts)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
let opts = {
  'searchTerm': "searchTerm_example", // String | 
  'legislature': "legislature_example", // String | 
  'meetingNumber': 56 // Number | 
};
apiInstance.apiSpeechesMetaDataSearchTopicsGet(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchTerm** | **String**|  | [optional] 
 **legislature** | **String**|  | [optional] 
 **meetingNumber** | **Number**|  | [optional] 

### Return type

[**[TopicSearchResultDto]**](TopicSearchResultDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

