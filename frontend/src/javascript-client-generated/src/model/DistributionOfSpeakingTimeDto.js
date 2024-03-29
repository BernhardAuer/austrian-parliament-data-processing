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
 * The DistributionOfSpeakingTimeDto model module.
 * @module model/DistributionOfSpeakingTimeDto
 * @version 1.0
 */
class DistributionOfSpeakingTimeDto {
    /**
     * Constructs a new <code>DistributionOfSpeakingTimeDto</code>.
     * @alias module:model/DistributionOfSpeakingTimeDto
     */
    constructor() { 
        
        DistributionOfSpeakingTimeDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DistributionOfSpeakingTimeDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DistributionOfSpeakingTimeDto} obj Optional instance to populate.
     * @return {module:model/DistributionOfSpeakingTimeDto} The populated <code>DistributionOfSpeakingTimeDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DistributionOfSpeakingTimeDto();

            if (data.hasOwnProperty('politicalParty')) {
                obj['politicalParty'] = ApiClient.convertToType(data['politicalParty'], 'String');
            }
            if (data.hasOwnProperty('speechDurationPercentage')) {
                obj['speechDurationPercentage'] = ApiClient.convertToType(data['speechDurationPercentage'], 'Number');
            }
            if (data.hasOwnProperty('numberOfSpeechesPercentage')) {
                obj['numberOfSpeechesPercentage'] = ApiClient.convertToType(data['numberOfSpeechesPercentage'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DistributionOfSpeakingTimeDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DistributionOfSpeakingTimeDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['politicalParty'] && !(typeof data['politicalParty'] === 'string' || data['politicalParty'] instanceof String)) {
            throw new Error("Expected the field `politicalParty` to be a primitive type in the JSON string but got " + data['politicalParty']);
        }

        return true;
    }


}



/**
 * @member {String} politicalParty
 */
DistributionOfSpeakingTimeDto.prototype['politicalParty'] = undefined;

/**
 * @member {Number} speechDurationPercentage
 */
DistributionOfSpeakingTimeDto.prototype['speechDurationPercentage'] = undefined;

/**
 * @member {Number} numberOfSpeechesPercentage
 */
DistributionOfSpeakingTimeDto.prototype['numberOfSpeechesPercentage'] = undefined;






export default DistributionOfSpeakingTimeDto;

