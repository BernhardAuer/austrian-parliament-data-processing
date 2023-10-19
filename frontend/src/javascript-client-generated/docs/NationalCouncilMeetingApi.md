# WebApiVersion1000CultureneutralPublicKeyTokennull.NationalCouncilMeetingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiNationalCouncilMeetingGetNationalCouncilMeetingsGet**](NationalCouncilMeetingApi.md#apiNationalCouncilMeetingGetNationalCouncilMeetingsGet) | **GET** /api/NationalCouncilMeeting/getNationalCouncilMeetings | 



## apiNationalCouncilMeetingGetNationalCouncilMeetingsGet

> [NationalCouncilMeetingsPerYearDto] apiNationalCouncilMeetingGetNationalCouncilMeetingsGet(opts)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.NationalCouncilMeetingApi();
let opts = {
  'year': 56 // Number | 
};
apiInstance.apiNationalCouncilMeetingGetNationalCouncilMeetingsGet(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **Number**|  | [optional] 

### Return type

[**[NationalCouncilMeetingsPerYearDto]**](NationalCouncilMeetingsPerYearDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

