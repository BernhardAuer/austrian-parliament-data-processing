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

import ApiClient from '../ApiClient';

/**
 * The SpeechSourceLinksDto model module.
 * @module model/SpeechSourceLinksDto
 * @version 1.0
 */
class SpeechSourceLinksDto {
    /**
     * Constructs a new <code>SpeechSourceLinksDto</code>.
     * @alias module:model/SpeechSourceLinksDto
     */
    constructor() { 
        
        SpeechSourceLinksDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SpeechSourceLinksDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SpeechSourceLinksDto} obj Optional instance to populate.
     * @return {module:model/SpeechSourceLinksDto} The populated <code>SpeechSourceLinksDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SpeechSourceLinksDto();

            if (data.hasOwnProperty('videoUrl')) {
                obj['videoUrl'] = ApiClient.convertToType(data['videoUrl'], 'String');
            }
            if (data.hasOwnProperty('speechUrl')) {
                obj['speechUrl'] = ApiClient.convertToType(data['speechUrl'], 'String');
            }
            if (data.hasOwnProperty('nameOfSpeaker')) {
                obj['nameOfSpeaker'] = ApiClient.convertToType(data['nameOfSpeaker'], 'String');
            }
            if (data.hasOwnProperty('topic')) {
                obj['topic'] = ApiClient.convertToType(data['topic'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SpeechSourceLinksDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SpeechSourceLinksDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['videoUrl'] && !(typeof data['videoUrl'] === 'string' || data['videoUrl'] instanceof String)) {
            throw new Error("Expected the field `videoUrl` to be a primitive type in the JSON string but got " + data['videoUrl']);
        }
        // ensure the json data is a string
        if (data['speechUrl'] && !(typeof data['speechUrl'] === 'string' || data['speechUrl'] instanceof String)) {
            throw new Error("Expected the field `speechUrl` to be a primitive type in the JSON string but got " + data['speechUrl']);
        }
        // ensure the json data is a string
        if (data['nameOfSpeaker'] && !(typeof data['nameOfSpeaker'] === 'string' || data['nameOfSpeaker'] instanceof String)) {
            throw new Error("Expected the field `nameOfSpeaker` to be a primitive type in the JSON string but got " + data['nameOfSpeaker']);
        }
        // ensure the json data is a string
        if (data['topic'] && !(typeof data['topic'] === 'string' || data['topic'] instanceof String)) {
            throw new Error("Expected the field `topic` to be a primitive type in the JSON string but got " + data['topic']);
        }

        return true;
    }


}



/**
 * @member {String} videoUrl
 */
SpeechSourceLinksDto.prototype['videoUrl'] = undefined;

/**
 * @member {String} speechUrl
 */
SpeechSourceLinksDto.prototype['speechUrl'] = undefined;

/**
 * @member {String} nameOfSpeaker
 */
SpeechSourceLinksDto.prototype['nameOfSpeaker'] = undefined;

/**
 * @member {String} topic
 */
SpeechSourceLinksDto.prototype['topic'] = undefined;






export default SpeechSourceLinksDto;

