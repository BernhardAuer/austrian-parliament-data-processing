/*
 * WebApi
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.41
 *
 * Do not edit the class manually.
 *
 */
import {ApiClient} from '../ApiClient';

/**
 * The LegislatureMeetingsListDto model module.
 * @module model/LegislatureMeetingsListDto
 * @version 1.0
 */
export class LegislatureMeetingsListDto {
  /**
   * Constructs a new <code>LegislatureMeetingsListDto</code>.
   * @alias module:model/LegislatureMeetingsListDto
   * @class
   */
  constructor() {
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
      if (data.hasOwnProperty('legislature'))
        obj.legislature = ApiClient.convertToType(data['legislature'], 'String');
      if (data.hasOwnProperty('meetings'))
        obj.meetings = ApiClient.convertToType(data['meetings'], ['Number']);
    }
    return obj;
  }
}

/**
 * @member {String} legislature
 */
LegislatureMeetingsListDto.prototype.legislature = undefined;

/**
 * @member {Array.<Number>} meetings
 */
LegislatureMeetingsListDto.prototype.meetings = undefined;
