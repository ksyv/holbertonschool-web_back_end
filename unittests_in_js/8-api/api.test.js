const request = require('request');
const { expect } = require('chai');
// const app = require('./api'); // We don't need to require app if the server is run independently

const API_URL = 'http://localhost:7865';

describe('Index page', () => {
  // Note: For these tests to pass, the server in api.js MUST be running.
  // You would typically start it in one terminal with `node api.js`
  // and then run `npm test api.test.js` in another terminal within the 8-api directory.

  it('should return status code 200 for GET /', (done) => {
    request.get(`${API_URL}/`, (error, response, body) => {
      // Check for errors during the request (e.g., server not running)
      if (error) {
        return done(error); // Signal test failure
      }
      // Assert that the status code is 200
      expect(response.statusCode).to.equal(200);
      done(); // Signal test completion
    });
  });

  it('should return the correct result for GET /', (done) => {
    request.get(`${API_URL}/`, (error, response, body) => {
      if (error) {
        return done(error);
      }
      // Assert that the body of the response is the expected welcome message
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should handle other properties correctly (e.g., content type)', (done) => {
    request.get(`${API_URL}/`, (error, response, body) => {
      if (error) {
        return done(error);
      }

      expect(response.headers['content-type']).to.include('text/html');
      done();
    });
  });
});