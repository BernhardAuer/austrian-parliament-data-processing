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
    describe('TypeOfSpeechCountDto', function() {
      beforeEach(function() {
        instance = new WebApi.TypeOfSpeechCountDto();
      });

      it('should create an instance of TypeOfSpeechCountDto', function() {
        // TODO: update the code to test TypeOfSpeechCountDto
        expect(instance).to.be.a(WebApi.TypeOfSpeechCountDto);
      });

      it('should have the property typeOfSpeech (base name: "typeOfSpeech")', function() {
        // TODO: update the code to test the property typeOfSpeech
        expect(instance).to.have.property('typeOfSpeech');
        // expect(instance.typeOfSpeech).to.be(expectedValueLiteral);
      });

      it('should have the property count (base name: "count")', function() {
        // TODO: update the code to test the property count
        expect(instance).to.have.property('count');
        // expect(instance.count).to.be(expectedValueLiteral);
      });

    });
  });

}));
