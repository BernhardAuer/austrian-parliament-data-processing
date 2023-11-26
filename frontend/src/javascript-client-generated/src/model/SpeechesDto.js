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
 * The SpeechesDto model module.
 * @module model/SpeechesDto
 * @version 1.0
 */
class SpeechesDto {
    /**
     * Constructs a new <code>SpeechesDto</code>.
     * @alias module:model/SpeechesDto
     */
    constructor() { 
        
        SpeechesDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SpeechesDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SpeechesDto} obj Optional instance to populate.
     * @return {module:model/SpeechesDto} The populated <code>SpeechesDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SpeechesDto();

            if (data.hasOwnProperty('nameOfSpeaker')) {
                obj['nameOfSpeaker'] = ApiClient.convertToType(data['nameOfSpeaker'], 'String');
            }
            if (data.hasOwnProperty('typeOfSpeech')) {
                obj['typeOfSpeech'] = ApiClient.convertToType(data['typeOfSpeech'], 'String');
            }
            if (data.hasOwnProperty('lengthOfSpeechInSec')) {
                obj['lengthOfSpeechInSec'] = ApiClient.convertToType(data['lengthOfSpeechInSec'], 'Number');
            }
            if (data.hasOwnProperty('topNr')) {
                obj['topNr'] = ApiClient.convertToType(data['topNr'], 'String');
            }
            if (data.hasOwnProperty('topic')) {
                obj['topic'] = ApiClient.convertToType(data['topic'], 'String');
            }
            if (data.hasOwnProperty('politicalPartie')) {
                obj['politicalPartie'] = ApiClient.convertToType(data['politicalPartie'], 'String');
            }
            if (data.hasOwnProperty('speechSneakPeak')) {
                obj['speechSneakPeak'] = ApiClient.convertToType(data['speechSneakPeak'], 'String');
            }
            if (data.hasOwnProperty('speechNrInDebate')) {
                obj['speechNrInDebate'] = ApiClient.convertToType(data['speechNrInDebate'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SpeechesDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SpeechesDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['nameOfSpeaker'] && !(typeof data['nameOfSpeaker'] === 'string' || data['nameOfSpeaker'] instanceof String)) {
            throw new Error("Expected the field `nameOfSpeaker` to be a primitive type in the JSON string but got " + data['nameOfSpeaker']);
        }
        // ensure the json data is a string
        if (data['typeOfSpeech'] && !(typeof data['typeOfSpeech'] === 'string' || data['typeOfSpeech'] instanceof String)) {
            throw new Error("Expected the field `typeOfSpeech` to be a primitive type in the JSON string but got " + data['typeOfSpeech']);
        }
        // ensure the json data is a string
        if (data['topNr'] && !(typeof data['topNr'] === 'string' || data['topNr'] instanceof String)) {
            throw new Error("Expected the field `topNr` to be a primitive type in the JSON string but got " + data['topNr']);
        }
        // ensure the json data is a string
        if (data['topic'] && !(typeof data['topic'] === 'string' || data['topic'] instanceof String)) {
            throw new Error("Expected the field `topic` to be a primitive type in the JSON string but got " + data['topic']);
        }
        // ensure the json data is a string
        if (data['politicalPartie'] && !(typeof data['politicalPartie'] === 'string' || data['politicalPartie'] instanceof String)) {
            throw new Error("Expected the field `politicalPartie` to be a primitive type in the JSON string but got " + data['politicalPartie']);
        }
        // ensure the json data is a string
        if (data['speechSneakPeak'] && !(typeof data['speechSneakPeak'] === 'string' || data['speechSneakPeak'] instanceof String)) {
            throw new Error("Expected the field `speechSneakPeak` to be a primitive type in the JSON string but got " + data['speechSneakPeak']);
        }

        return true;
    }


}



/**
 * @member {String} nameOfSpeaker
 */
SpeechesDto.prototype['nameOfSpeaker'] = undefined;

/**
 * @member {String} typeOfSpeech
 */
SpeechesDto.prototype['typeOfSpeech'] = undefined;

/**
 * @member {Number} lengthOfSpeechInSec
 */
SpeechesDto.prototype['lengthOfSpeechInSec'] = undefined;

/**
 * @member {String} topNr
 */
SpeechesDto.prototype['topNr'] = undefined;

/**
 * @member {String} topic
 */
SpeechesDto.prototype['topic'] = undefined;

/**
 * @member {String} politicalPartie
 */
SpeechesDto.prototype['politicalPartie'] = undefined;

/**
 * @member {String} speechSneakPeak
 */
SpeechesDto.prototype['speechSneakPeak'] = undefined;

/**
 * @member {Number} speechNrInDebate
 */
SpeechesDto.prototype['speechNrInDebate'] = undefined;






export default SpeechesDto;

