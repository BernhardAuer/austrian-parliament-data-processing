# WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet) | **GET** /api/SpeechesMetaData/getLegislaturesAndMeetingNumbers | 
[**apiSpeechesMetaDataGetTypeOfSpeechesCountListGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetTypeOfSpeechesCountListGet) | **GET** /api/SpeechesMetaData/getTypeOfSpeechesCountList | 
[**apiSpeechesMetaDataSearchTopicsGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataSearchTopicsGet) | **GET** /api/SpeechesMetaData/searchTopics | 



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

