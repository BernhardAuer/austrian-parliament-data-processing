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
 * The SpeechDurationDto model module.
 * @module model/SpeechDurationDto
 * @version 1.0
 */
class SpeechDurationDto {
    /**
     * Constructs a new <code>SpeechDurationDto</code>.
     * @alias module:model/SpeechDurationDto
     */
    constructor() { 
        
        SpeechDurationDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SpeechDurationDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SpeechDurationDto} obj Optional instance to populate.
     * @return {module:model/SpeechDurationDto} The populated <code>SpeechDurationDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SpeechDurationDto();

            if (data.hasOwnProperty('politicalParty')) {
                obj['politicalParty'] = ApiClient.convertToType(data['politicalParty'], 'String');
            }
            if (data.hasOwnProperty('speaker')) {
                obj['speaker'] = ApiClient.convertToType(data['speaker'], 'String');
            }
            if (data.hasOwnProperty('durationSumInSec')) {
                obj['durationSumInSec'] = ApiClient.convertToType(data['durationSumInSec'], 'Number');
            }
            if (data.hasOwnProperty('totalNumberOfSpeeches')) {
                obj['totalNumberOfSpeeches'] = ApiClient.convertToType(data['totalNumberOfSpeeches'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SpeechDurationDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SpeechDurationDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['politicalParty'] && !(typeof data['politicalParty'] === 'string' || data['politicalParty'] instanceof String)) {
            throw new Error("Expected the field `politicalParty` to be a primitive type in the JSON string but got " + data['politicalParty']);
        }
        // ensure the json data is a string
        if (data['speaker'] && !(typeof data['speaker'] === 'string' || data['speaker'] instanceof String)) {
            throw new Error("Expected the field `speaker` to be a primitive type in the JSON string but got " + data['speaker']);
        }

        return true;
    }


}



/**
 * @member {String} politicalParty
 */
SpeechDurationDto.prototype['politicalParty'] = undefined;

/**
 * @member {String} speaker
 */
SpeechDurationDto.prototype['speaker'] = undefined;

/**
 * @member {Number} durationSumInSec
 */
SpeechDurationDto.prototype['durationSumInSec'] = undefined;

/**
 * @member {Number} totalNumberOfSpeeches
 */
SpeechDurationDto.prototype['totalNumberOfSpeeches'] = undefined;






export default SpeechDurationDto;
