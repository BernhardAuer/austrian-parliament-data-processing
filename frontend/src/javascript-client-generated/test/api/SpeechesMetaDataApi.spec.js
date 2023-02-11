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

  beforeEach(function() {
    instance = new WebApi.SpeechesMetaDataApi();
  });

  describe('(package)', function() {
    describe('SpeechesMetaDataApi', function() {
      describe('apiSpeechesMetaDataGet', function() {
        it('should call apiSpeechesMetaDataGet successfully', function(done) {
          // TODO: uncomment apiSpeechesMetaDataGet call and complete the assertions
          /*

          instance.apiSpeechesMetaDataGet(function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            let dataCtr = data;
            expect(dataCtr).to.be.an(Array);
            expect(dataCtr).to.not.be.empty();
            for (let p in dataCtr) {
              let data = dataCtr[p];
              expect(data).to.be.a(WebApi.SpeechesMetaData);
            }

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('apiSpeechesMetaDataGetTypeOfSpeechesCountListGet', function() {
        it('should call apiSpeechesMetaDataGetTypeOfSpeechesCountListGet successfully', function(done) {
          // TODO: uncomment apiSpeechesMetaDataGetTypeOfSpeechesCountListGet call and complete the assertions
          /*

          instance.apiSpeechesMetaDataGetTypeOfSpeechesCountListGet(function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            let dataCtr = data;
            expect(dataCtr).to.be.an(Array);
            expect(dataCtr).to.not.be.empty();
            for (let p in dataCtr) {
              let data = dataCtr[p];
              expect(data).to.be.a(WebApi.TypeOfSpeechCountDto);
            }

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('apiSpeechesMetaDataIdDelete', function() {
        it('should call apiSpeechesMetaDataIdDelete successfully', function(done) {
          // TODO: uncomment, update parameter values for apiSpeechesMetaDataIdDelete call
          /*

          instance.apiSpeechesMetaDataIdDelete(id, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('apiSpeechesMetaDataIdGet', function() {
        it('should call apiSpeechesMetaDataIdGet successfully', function(done) {
          // TODO: uncomment, update parameter values for apiSpeechesMetaDataIdGet call and complete the assertions
          /*

          instance.apiSpeechesMetaDataIdGet(id, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            expect(data).to.be.a(WebApi.SpeechesMetaData);

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('apiSpeechesMetaDataIdPut', function() {
        it('should call apiSpeechesMetaDataIdPut successfully', function(done) {
          // TODO: uncomment, update parameter values for apiSpeechesMetaDataIdPut call
          /*
          var opts = {};

          instance.apiSpeechesMetaDataIdPut(id, opts, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('apiSpeechesMetaDataPost', function() {
        it('should call apiSpeechesMetaDataPost successfully', function(done) {
          // TODO: uncomment, update parameter values for apiSpeechesMetaDataPost call
          /*
          var opts = {};

          instance.apiSpeechesMetaDataPost(opts, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
    });
  });

}));
