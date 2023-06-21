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
 * The TopicSearchResultDto model module.
 * @module model/TopicSearchResultDto
 * @version 1.0
 */
class TopicSearchResultDto {
    /**
     * Constructs a new <code>TopicSearchResultDto</code>.
     * @alias module:model/TopicSearchResultDto
     */
    constructor() { 
        
        TopicSearchResultDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TopicSearchResultDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TopicSearchResultDto} obj Optional instance to populate.
     * @return {module:model/TopicSearchResultDto} The populated <code>TopicSearchResultDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TopicSearchResultDto();

            if (data.hasOwnProperty('topic')) {
                obj['topic'] = ApiClient.convertToType(data['topic'], 'String');
            }
            if (data.hasOwnProperty('topNr')) {
                obj['topNr'] = ApiClient.convertToType(data['topNr'], 'String');
            }
            if (data.hasOwnProperty('meetingNr')) {
                obj['meetingNr'] = ApiClient.convertToType(data['meetingNr'], 'Number');
            }
            if (data.hasOwnProperty('legislature')) {
                obj['legislature'] = ApiClient.convertToType(data['legislature'], 'String');
            }
            if (data.hasOwnProperty('textMatchScore')) {
                obj['textMatchScore'] = ApiClient.convertToType(data['textMatchScore'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TopicSearchResultDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TopicSearchResultDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['topic'] && !(typeof data['topic'] === 'string' || data['topic'] instanceof String)) {
            throw new Error("Expected the field `topic` to be a primitive type in the JSON string but got " + data['topic']);
        }
        // ensure the json data is a string
        if (data['topNr'] && !(typeof data['topNr'] === 'string' || data['topNr'] instanceof String)) {
            throw new Error("Expected the field `topNr` to be a primitive type in the JSON string but got " + data['topNr']);
        }
        // ensure the json data is a string
        if (data['legislature'] && !(typeof data['legislature'] === 'string' || data['legislature'] instanceof String)) {
            throw new Error("Expected the field `legislature` to be a primitive type in the JSON string but got " + data['legislature']);
        }

        return true;
    }


}



/**
 * @member {String} topic
 */
TopicSearchResultDto.prototype['topic'] = undefined;

/**
 * @member {String} topNr
 */
TopicSearchResultDto.prototype['topNr'] = undefined;

/**
 * @member {Number} meetingNr
 */
TopicSearchResultDto.prototype['meetingNr'] = undefined;

/**
 * @member {String} legislature
 */
TopicSearchResultDto.prototype['legislature'] = undefined;

/**
 * @member {Number} textMatchScore
 */
TopicSearchResultDto.prototype['textMatchScore'] = undefined;






export default TopicSearchResultDto;

