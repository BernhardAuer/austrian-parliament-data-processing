/*
 * WebApi
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.40
 *
 * Do not edit the class manually.
 *
 */
(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.WebApi);
  }
}(this, function(expect, WebApi) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('SpeechesMetaData', function() {
      beforeEach(function() {
        instance = new WebApi.SpeechesMetaData();
      });

      it('should create an instance of SpeechesMetaData', function() {
        // TODO: update the code to test SpeechesMetaData
        expect(instance).to.be.a(WebApi.SpeechesMetaData);
      });

      it('should have the property id (base name: "id")', function() {
        // TODO: update the code to test the property id
        expect(instance).to.have.property('id');
        // expect(instance.id).to.be(expectedValueLiteral);
      });

      it('should have the property nameOfSpeaker (base name: "nameOfSpeaker")', function() {
        // TODO: update the code to test the property nameOfSpeaker
        expect(instance).to.have.property('nameOfSpeaker');
        // expect(instance.nameOfSpeaker).to.be(expectedValueLiteral);
      });

      it('should have the property nrOfSpeechInDebate (base name: "nrOfSpeechInDebate")', function() {
        // TODO: update the code to test the property nrOfSpeechInDebate
        expect(instance).to.have.property('nrOfSpeechInDebate');
        // expect(instance.nrOfSpeechInDebate).to.be(expectedValueLiteral);
      });

      it('should have the property nrOfSpeechByThisPerson (base name: "nrOfSpeechByThisPerson")', function() {
        // TODO: update the code to test the property nrOfSpeechByThisPerson
        expect(instance).to.have.property('nrOfSpeechByThisPerson');
        // expect(instance.nrOfSpeechByThisPerson).to.be(expectedValueLiteral);
      });

      it('should have the property typeOfSpeech (base name: "typeOfSpeech")', function() {
        // TODO: update the code to test the property typeOfSpeech
        expect(instance).to.have.property('typeOfSpeech');
        // expect(instance.typeOfSpeech).to.be(expectedValueLiteral);
      });

      it('should have the property startDateTime (base name: "startDateTime")', function() {
        // TODO: update the code to test the property startDateTime
        expect(instance).to.have.property('startDateTime');
        // expect(instance.startDateTime).to.be(expectedValueLiteral);
      });

      it('should have the property timeLimitInSec (base name: "timeLimitInSec")', function() {
        // TODO: update the code to test the property timeLimitInSec
        expect(instance).to.have.property('timeLimitInSec');
        // expect(instance.timeLimitInSec).to.be(expectedValueLiteral);
      });

      it('should have the property isVoluntaryTimeLimit (base name: "isVoluntaryTimeLimit")', function() {
        // TODO: update the code to test the property isVoluntaryTimeLimit
        expect(instance).to.have.property('isVoluntaryTimeLimit');
        // expect(instance.isVoluntaryTimeLimit).to.be(expectedValueLiteral);
      });

      it('should have the property lengthOfSpeechInSec (base name: "lengthOfSpeechInSec")', function() {
        // TODO: update the code to test the property lengthOfSpeechInSec
        expect(instance).to.have.property('lengthOfSpeechInSec');
        // expect(instance.lengthOfSpeechInSec).to.be(expectedValueLiteral);
      });

      it('should have the property nationalCouncilMeetingTitle (base name: "nationalCouncilMeetingTitle")', function() {
        // TODO: update the code to test the property nationalCouncilMeetingTitle
        expect(instance).to.have.property('nationalCouncilMeetingTitle');
        // expect(instance.nationalCouncilMeetingTitle).to.be(expectedValueLiteral);
      });

      it('should have the property topic (base name: "topic")', function() {
        // TODO: update the code to test the property topic
        expect(instance).to.have.property('topic');
        // expect(instance.topic).to.be(expectedValueLiteral);
      });

      it('should have the property hasSpeechFinished (base name: "hasSpeechFinished")', function() {
        // TODO: update the code to test the property hasSpeechFinished
        expect(instance).to.have.property('hasSpeechFinished');
        // expect(instance.hasSpeechFinished).to.be(expectedValueLiteral);
      });

    });
  });

}));
