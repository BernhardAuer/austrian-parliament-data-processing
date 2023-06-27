/**
 * WebApi, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import LegislatureMeetingsListDto from './model/LegislatureMeetingsListDto';
import SpeechesDto from './model/SpeechesDto';
import TopicSearchResultDto from './model/TopicSearchResultDto';
import TypeOfSpeechCountDto from './model/TypeOfSpeechCountDto';
import SpeechesMetaDataApi from './api/SpeechesMetaDataApi';


/**
* JS API client generated by OpenAPI Generator.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var WebApiVersion1000CultureneutralPublicKeyTokennull = require('index'); // See note below*.
* var xxxSvc = new WebApiVersion1000CultureneutralPublicKeyTokennull.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new WebApiVersion1000CultureneutralPublicKeyTokennull.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new WebApiVersion1000CultureneutralPublicKeyTokennull.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new WebApiVersion1000CultureneutralPublicKeyTokennull.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The LegislatureMeetingsListDto model constructor.
     * @property {module:model/LegislatureMeetingsListDto}
     */
    LegislatureMeetingsListDto,

    /**
     * The SpeechesDto model constructor.
     * @property {module:model/SpeechesDto}
     */
    SpeechesDto,

    /**
     * The TopicSearchResultDto model constructor.
     * @property {module:model/TopicSearchResultDto}
     */
    TopicSearchResultDto,

    /**
     * The TypeOfSpeechCountDto model constructor.
     * @property {module:model/TypeOfSpeechCountDto}
     */
    TypeOfSpeechCountDto,

    /**
    * The SpeechesMetaDataApi service constructor.
    * @property {module:api/SpeechesMetaDataApi}
    */
    SpeechesMetaDataApi
};
