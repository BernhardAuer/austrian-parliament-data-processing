# WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiSpeechesMetaDataGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGet) | **GET** /api/SpeechesMetaData | 
[**apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet) | **GET** /api/SpeechesMetaData/getLegislaturesAndMeetingNumbers | 
[**apiSpeechesMetaDataGetTypeOfSpeechesCountListGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetTypeOfSpeechesCountListGet) | **GET** /api/SpeechesMetaData/getTypeOfSpeechesCountList | 
[**apiSpeechesMetaDataIdDelete**](SpeechesMetaDataApi.md#apiSpeechesMetaDataIdDelete) | **DELETE** /api/SpeechesMetaData/{id} | 
[**apiSpeechesMetaDataIdGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataIdGet) | **GET** /api/SpeechesMetaData/{id} | 
[**apiSpeechesMetaDataIdPut**](SpeechesMetaDataApi.md#apiSpeechesMetaDataIdPut) | **PUT** /api/SpeechesMetaData/{id} | 
[**apiSpeechesMetaDataPost**](SpeechesMetaDataApi.md#apiSpeechesMetaDataPost) | **POST** /api/SpeechesMetaData | 
[**apiSpeechesMetaDataSearchTopicsGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataSearchTopicsGet) | **GET** /api/SpeechesMetaData/searchTopics | 



## apiSpeechesMetaDataGet

> [SpeechesMetaData] apiSpeechesMetaDataGet()



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
apiInstance.apiSpeechesMetaDataGet().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[SpeechesMetaData]**](SpeechesMetaData.md)

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


## apiSpeechesMetaDataIdDelete

> apiSpeechesMetaDataIdDelete(id)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
let id = "id_example"; // String | 
apiInstance.apiSpeechesMetaDataIdDelete(id).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiSpeechesMetaDataIdGet

> SpeechesMetaData apiSpeechesMetaDataIdGet(id)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
let id = "id_example"; // String | 
apiInstance.apiSpeechesMetaDataIdGet(id).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**SpeechesMetaData**](SpeechesMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## apiSpeechesMetaDataIdPut

> apiSpeechesMetaDataIdPut(id, opts)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
let id = "id_example"; // String | 
let opts = {
  'speechesMetaData': new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaData() // SpeechesMetaData | 
};
apiInstance.apiSpeechesMetaDataIdPut(id, opts).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **speechesMetaData** | [**SpeechesMetaData**](SpeechesMetaData.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json, application/*+json
- **Accept**: Not defined


## apiSpeechesMetaDataPost

> apiSpeechesMetaDataPost(opts)



### Example

```javascript
import WebApiVersion1000CultureneutralPublicKeyTokennull from 'web_api_version1_0_0_0_cultureneutral_public_key_tokennull';

let apiInstance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaDataApi();
let opts = {
  'speechesMetaData': new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesMetaData() // SpeechesMetaData | 
};
apiInstance.apiSpeechesMetaDataPost(opts).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **speechesMetaData** | [**SpeechesMetaData**](SpeechesMetaData.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json, application/*+json
- **Accept**: Not defined


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

