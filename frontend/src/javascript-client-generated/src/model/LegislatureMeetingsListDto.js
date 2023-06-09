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
 * The LegislatureMeetingsListDto model module.
 * @module model/LegislatureMeetingsListDto
 * @version 1.0
 */
class LegislatureMeetingsListDto {
    /**
     * Constructs a new <code>LegislatureMeetingsListDto</code>.
     * @alias module:model/LegislatureMeetingsListDto
     */
    constructor() { 
        
        LegislatureMeetingsListDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LegislatureMeetingsListDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LegislatureMeetingsListDto} obj Optional instance to populate.
     * @return {module:model/LegislatureMeetingsListDto} The populated <code>LegislatureMeetingsListDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LegislatureMeetingsListDto();

            if (data.hasOwnProperty('legislature')) {
                obj['legislature'] = ApiClient.convertToType(data['legislature'], 'String');
            }
            if (data.hasOwnProperty('legislatureAsInt')) {
                obj['legislatureAsInt'] = ApiClient.convertToType(data['legislatureAsInt'], 'Number');
            }
            if (data.hasOwnProperty('meetings')) {
                obj['meetings'] = ApiClient.convertToType(data['meetings'], ['Number']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LegislatureMeetingsListDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LegislatureMeetingsListDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['legislature'] && !(typeof data['legislature'] === 'string' || data['legislature'] instanceof String)) {
            throw new Error("Expected the field `legislature` to be a primitive type in the JSON string but got " + data['legislature']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['meetings'])) {
            throw new Error("Expected the field `meetings` to be an array in the JSON data but got " + data['meetings']);
        }

        return true;
    }


}



/**
 * @member {String} legislature
 */
LegislatureMeetingsListDto.prototype['legislature'] = undefined;

/**
 * @member {Number} legislatureAsInt
 */
LegislatureMeetingsListDto.prototype['legislatureAsInt'] = undefined;

/**
 * @member {Array.<Number>} meetings
 */
LegislatureMeetingsListDto.prototype['meetings'] = undefined;






export default LegislatureMeetingsListDto;

