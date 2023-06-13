/*
 * WebApi
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.46
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
    describe('TopicSearchResultDto', function() {
      beforeEach(function() {
        instance = new WebApi.TopicSearchResultDto();
      });

      it('should create an instance of TopicSearchResultDto', function() {
        // TODO: update the code to test TopicSearchResultDto
        expect(instance).to.be.a(WebApi.TopicSearchResultDto);
      });

      it('should have the property topic (base name: "topic")', function() {
        // TODO: update the code to test the property topic
        expect(instance).to.have.property('topic');
        // expect(instance.topic).to.be(expectedValueLiteral);
      });

      it('should have the property topNr (base name: "topNr")', function() {
        // TODO: update the code to test the property topNr
        expect(instance).to.have.property('topNr');
        // expect(instance.topNr).to.be(expectedValueLiteral);
      });

      it('should have the property meetingNr (base name: "meetingNr")', function() {
        // TODO: update the code to test the property meetingNr
        expect(instance).to.have.property('meetingNr');
        // expect(instance.meetingNr).to.be(expectedValueLiteral);
      });

      it('should have the property legislature (base name: "legislature")', function() {
        // TODO: update the code to test the property legislature
        expect(instance).to.have.property('legislature');
        // expect(instance.legislature).to.be(expectedValueLiteral);
      });

      it('should have the property textMatchScore (base name: "textMatchScore")', function() {
        // TODO: update the code to test the property textMatchScore
        expect(instance).to.have.property('textMatchScore');
        // expect(instance.textMatchScore).to.be(expectedValueLiteral);
      });

    });
  });

}));
