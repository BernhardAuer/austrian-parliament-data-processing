# WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiSpeechesGetPureSpeechesGet**](SpeechesApi.md#apiSpeechesGetPureSpeechesGet) | **GET** /api/Speeches/getPureSpeeches | 



## apiSpeechesGetPureSpeechesGet

> [SpeechDto] apiSpeechesGetPureSpeechesGet(opts)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesApi();
let opts = {
  'legislature': "legislature_example", // String | 
  'meetingNumber': 56, // Number | 
  'speechNrInDebate': 56, // Number | 
  'topic': "topic_example" // String | 
};
apiInstance.apiSpeechesGetPureSpeechesGet(opts).then((data) => {
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
 **speechNrInDebate** | **Number**|  | [optional] 
 **topic** | **String**|  | [optional] 

### Return type

[**[SpeechDto]**](SpeechDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

