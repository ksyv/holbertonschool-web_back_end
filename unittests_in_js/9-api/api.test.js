const request = require('request');
const { expect } = require('chai');

const API_URL = 'http://localhost:7865';

describe('Index page', () => {
  // Note: For these tests to pass, the server in api.js MUST be running.
  // You would typically start it in one terminal with `node api.js`
  // and then run `npm test api.test.js` in another terminal within the 9-api directory.

  it('should return status code 200 for GET /', (done) => {
    request.get(`${API_URL}/`, (error, response, body) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct result for GET /', (done) => {
    request.get(`${API_URL}/`, (error, response, body) => {
      if (error) return done(error);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should handle other properties correctly (e.g., content type for GET /)', (done) => {
    request.get(`${API_URL}/`, (error, response, body) => {
      if (error) return done(error);
      expect(response.headers['content-type']).to.include('text/html');
      done();
    });
  });
});

describe('Cart page', () => {
  it('should return status code 200 and correct message for GET /cart/:id when :id is a number', (done) => {
    const cartId = 12;
    request.get(`${API_URL}/cart/${cartId}`, (error, response, body) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal(`Payment methods for cart ${cartId}`);
      done();
    });
  });

  it('should return status code 404 for GET /cart/:id when :id is NOT a number', (done) => {
    const cartId = 'hello'; // Non-numeric ID
    request.get(`${API_URL}/cart/${cartId}`, (error, response, body) => {
      if (error) return done(error);
      // Because the route itself has a regex (\\d+), an invalid :id
      // will not match the route, leading Express to return a 404 for "Cannot GET /cart/hello"
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return status code 404 for GET /cart/ with no id', (done) => {
    request.get(`${API_URL}/cart/`, (error, response, body) => {
        if (error) return done(error);
        expect(response.statusCode).to.equal(404);
        done();
    });
  });

  // Additional test: what if id is a negative number? (should still be caught by \\d+ as valid if not further restricted)
  it('should return status code 200 for GET /cart/:id when :id is a valid number string like "47"', (done) => {
    const cartId = '47';
    request.get(`${API_URL}/cart/${cartId}`, (error, response, body) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal(`Payment methods for cart ${cartId}`);
      done();
    });
  });

  // Additional test: what if id is zero?
   it('should return status code 200 for GET /cart/:id when :id is 0', (done) => {
    const cartId = 0;
    request.get(`${API_URL}/cart/${cartId}`, (error, response, body) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal(`Payment methods for cart ${cartId}`);
      done();
    });
  });
});