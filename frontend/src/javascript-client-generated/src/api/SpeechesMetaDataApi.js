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


import ApiClient from "../ApiClient";
import LegislatureMeetingsListDto from '../model/LegislatureMeetingsListDto';
import SpeechesDto from '../model/SpeechesDto';
import TopicSearchResultDto from '../model/TopicSearchResultDto';
import TypeOfSpeechCountDto from '../model/TypeOfSpeechCountDto';

/**
* SpeechesMetaData service.
* @module api/SpeechesMetaDataApi
* @version 1.0
*/
export default class SpeechesMetaDataApi {

    /**
    * Constructs a new SpeechesMetaDataApi. 
    * @alias module:api/SpeechesMetaDataApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }



    /**
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing data of type {@link Array.<module:model/LegislatureMeetingsListDto>} and HTTP response
     */
    apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGetWithHttpInfo() {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['text/plain', 'application/json', 'text/json'];
      let returnType = [LegislatureMeetingsListDto];
      return this.apiClient.callApi(
        '/api/SpeechesMetaData/getLegislaturesAndMeetingNumbers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null
      );
    }

    /**
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with data of type {@link Array.<module:model/LegislatureMeetingsListDto>}
     */
    apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet() {
      return this.apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGetWithHttpInfo()
        .then(function(response_and_data) {
          return response_and_data.data;
        });
    }


    /**
     * @param {Object} opts Optional parameters
     * @param {String} [legislature] 
     * @param {Number} [meetingNumber] 
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing data of type {@link Array.<module:model/SpeechesDto>} and HTTP response
     */
    apiSpeechesMetaDataGetSpeechesGetWithHttpInfo(opts) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'legislature': opts['legislature'],
        'meetingNumber': opts['meetingNumber']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['text/plain', 'application/json', 'text/json'];
      let returnType = [SpeechesDto];
      return this.apiClient.callApi(
        '/api/SpeechesMetaData/getSpeeches', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null
      );
    }

    /**
     * @param {Object} opts Optional parameters
     * @param {String} opts.legislature 
     * @param {Number} opts.meetingNumber 
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with data of type {@link Array.<module:model/SpeechesDto>}
     */
    apiSpeechesMetaDataGetSpeechesGet(opts) {
      return this.apiSpeechesMetaDataGetSpeechesGetWithHttpInfo(opts)
        .then(function(response_and_data) {
          return response_and_data.data;
        });
    }


    /**
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [politicalParty] 
     * @param {String} [legislature] 
     * @param {Number} [meetingNumber] 
     * @param {String} [topic] 
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing data of type {@link Array.<module:model/TypeOfSpeechCountDto>} and HTTP response
     */
    apiSpeechesMetaDataGetTypeOfSpeechesCountListGetWithHttpInfo(opts) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'PoliticalParty': this.apiClient.buildCollectionParam(opts['politicalParty'], 'multi'),
        'Legislature': opts['legislature'],
        'MeetingNumber': opts['meetingNumber'],
        'Topic': opts['topic']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['text/plain', 'application/json', 'text/json'];
      let returnType = [TypeOfSpeechCountDto];
      return this.apiClient.callApi(
        '/api/SpeechesMetaData/getTypeOfSpeechesCountList', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null
      );
    }

    /**
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} opts.politicalParty 
     * @param {String} opts.legislature 
     * @param {Number} opts.meetingNumber 
     * @param {String} opts.topic 
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with data of type {@link Array.<module:model/TypeOfSpeechCountDto>}
     */
    apiSpeechesMetaDataGetTypeOfSpeechesCountListGet(opts) {
      return this.apiSpeechesMetaDataGetTypeOfSpeechesCountListGetWithHttpInfo(opts)
        .then(function(response_and_data) {
          return response_and_data.data;
        });
    }


    /**
     * @param {Object} opts Optional parameters
     * @param {String} [searchTerm] 
     * @param {String} [legislature] 
     * @param {Number} [meetingNumber] 
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing data of type {@link Array.<module:model/TopicSearchResultDto>} and HTTP response
     */
    apiSpeechesMetaDataSearchTopicsGetWithHttpInfo(opts) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'searchTerm': opts['searchTerm'],
        'legislature': opts['legislature'],
        'meetingNumber': opts['meetingNumber']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['text/plain', 'application/json', 'text/json'];
      let returnType = [TopicSearchResultDto];
      return this.apiClient.callApi(
        '/api/SpeechesMetaData/searchTopics', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null
      );
    }

    /**
     * @param {Object} opts Optional parameters
     * @param {String} opts.searchTerm 
     * @param {String} opts.legislature 
     * @param {Number} opts.meetingNumber 
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with data of type {@link Array.<module:model/TopicSearchResultDto>}
     */
    apiSpeechesMetaDataSearchTopicsGet(opts) {
      return this.apiSpeechesMetaDataSearchTopicsGetWithHttpInfo(opts)
        .then(function(response_and_data) {
          return response_and_data.data;
        });
    }


}
