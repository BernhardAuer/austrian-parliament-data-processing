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
import SpeechDto from '../model/SpeechDto';

/**
* Speeches service.
* @module api/SpeechesApi
* @version 1.0
*/
export default class SpeechesApi {

    /**
    * Constructs a new SpeechesApi. 
    * @alias module:api/SpeechesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }



    /**
     * @param {Object} opts Optional parameters
     * @param {String} [legislature] 
     * @param {Number} [meetingNumber] 
     * @param {Number} [speechNrInDebate] 
     * @param {String} [topic] 
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing data of type {@link Array.<module:model/SpeechDto>} and HTTP response
     */
    apiSpeechesGetPureSpeechesGetWithHttpInfo(opts) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'legislature': opts['legislature'],
        'meetingNumber': opts['meetingNumber'],
        'speechNrInDebate': opts['speechNrInDebate'],
        'topic': opts['topic']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['text/plain', 'application/json', 'text/json'];
      let returnType = [SpeechDto];
      return this.apiClient.callApi(
        '/api/Speeches/getPureSpeeches', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null
      );
    }

    /**
     * @param {Object} opts Optional parameters
     * @param {String} opts.legislature 
     * @param {Number} opts.meetingNumber 
     * @param {Number} opts.speechNrInDebate 
     * @param {String} opts.topic 
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with data of type {@link Array.<module:model/SpeechDto>}
     */
    apiSpeechesGetPureSpeechesGet(opts) {
      return this.apiSpeechesGetPureSpeechesGetWithHttpInfo(opts)
        .then(function(response_and_data) {
          return response_and_data.data;
        });
    }


}
