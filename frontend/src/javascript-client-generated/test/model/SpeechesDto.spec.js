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
    instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesDto();
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

  describe('SpeechesDto', function() {
    it('should create an instance of SpeechesDto', function() {
      // uncomment below and update the code to test SpeechesDto
      //var instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesDto();
      //expect(instance).to.be.a(WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesDto);
    });

    it('should have the property nameOfSpeaker (base name: "nameOfSpeaker")', function() {
      // uncomment below and update the code to test the property nameOfSpeaker
      //var instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesDto();
      //expect(instance).to.be();
    });

    it('should have the property typeOfSpeech (base name: "typeOfSpeech")', function() {
      // uncomment below and update the code to test the property typeOfSpeech
      //var instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesDto();
      //expect(instance).to.be();
    });

    it('should have the property lengthOfSpeechInSec (base name: "lengthOfSpeechInSec")', function() {
      // uncomment below and update the code to test the property lengthOfSpeechInSec
      //var instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesDto();
      //expect(instance).to.be();
    });

    it('should have the property topNr (base name: "topNr")', function() {
      // uncomment below and update the code to test the property topNr
      //var instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesDto();
      //expect(instance).to.be();
    });

    it('should have the property topic (base name: "topic")', function() {
      // uncomment below and update the code to test the property topic
      //var instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesDto();
      //expect(instance).to.be();
    });

    it('should have the property politicalPartie (base name: "politicalPartie")', function() {
      // uncomment below and update the code to test the property politicalPartie
      //var instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesDto();
      //expect(instance).to.be();
    });

    it('should have the property speech (base name: "speech")', function() {
      // uncomment below and update the code to test the property speech
      //var instance = new WebApiVersion1000CultureneutralPublicKeyTokennull.SpeechesDto();
      //expect(instance).to.be();
    });

  });

}));