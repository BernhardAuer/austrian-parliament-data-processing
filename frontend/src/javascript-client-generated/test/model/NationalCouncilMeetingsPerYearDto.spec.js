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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.WebApiVersion1000CultureneutralPublicKeyTokennull);
  }
}(this, function(expect, WebApiVersion1000CultureneutralPublicKeyTokennull) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.NationalCouncilMeetingsPerYearDto();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('NationalCouncilMeetingsPerYearDto', function() {
    it('should create an instance of NationalCouncilMeetingsPerYearDto', function() {
      // uncomment below and update the code to test NationalCouncilMeetingsPerYearDto
      //var instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.NationalCouncilMeetingsPerYearDto();
      //expect(instance).to.be.a(WebApiVersion1000CultureneutralPublicKeyTokennull.NationalCouncilMeetingsPerYearDto);
    });

    it('should have the property month (base name: "month")', function() {
      // uncomment below and update the code to test the property month
      //var instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.NationalCouncilMeetingsPerYearDto();
      //expect(instance).to.be();
    });

    it('should have the property count (base name: "count")', function() {
      // uncomment below and update the code to test the property count
      //var instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.NationalCouncilMeetingsPerYearDto();
      //expect(instance).to.be();
    });

  });

}));
