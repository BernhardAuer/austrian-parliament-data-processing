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
 * The NationalCouncilMeetingsPerYearDto model module.
 * @module model/NationalCouncilMeetingsPerYearDto
 * @version 1.0
 */
class NationalCouncilMeetingsPerYearDto {
    /**
     * Constructs a new <code>NationalCouncilMeetingsPerYearDto</code>.
     * @alias module:model/NationalCouncilMeetingsPerYearDto
     */
    constructor() { 
        
        NationalCouncilMeetingsPerYearDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>NationalCouncilMeetingsPerYearDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NationalCouncilMeetingsPerYearDto} obj Optional instance to populate.
     * @return {module:model/NationalCouncilMeetingsPerYearDto} The populated <code>NationalCouncilMeetingsPerYearDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NationalCouncilMeetingsPerYearDto();

            if (data.hasOwnProperty('month')) {
                obj['month'] = ApiClient.convertToType(data['month'], 'Number');
            }
            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NationalCouncilMeetingsPerYearDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NationalCouncilMeetingsPerYearDto</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Number} month
 */
NationalCouncilMeetingsPerYearDto.prototype['month'] = undefined;

/**
 * @member {Number} count
 */
NationalCouncilMeetingsPerYearDto.prototype['count'] = undefined;






export default NationalCouncilMeetingsPerYearDto;

