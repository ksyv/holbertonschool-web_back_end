const request = require('request');
const { expect } = require('chai');

const API_URL = 'http://localhost:7865';

describe('Index page', () => {
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
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Login endpoint', () => {
  it('should return status code 200 and welcome message for POST /login', (done) => {
    const userName = 'Betty';
    const options = {
      url: `${API_URL}/login`,
      method: 'POST',
      json: { // Automatically sets Content-Type to application/json and stringifies the body
        userName: userName
      }
    };

    request(options, (error, response, body) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      // 'body' will be automatically parsed if the server sends 'application/json'
      // and 'json: true' is used in request options.
      // However, our server sends text/html by default for .send()
      expect(body).to.equal(`Welcome ${userName}`);
      done();
    });
  });

  it('should return status code 400 if userName is missing for POST /login', (done) => {
    const options = {
      url: `${API_URL}/login`,
      method: 'POST',
      json: {} // Sending an empty JSON object
    };

    request(options, (error, response, body) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(400);
      expect(body).to.equal('userName is required');
      done();
    });
  });
});

describe('Available Payments endpoint', () => {
  it('should return status code 200 for GET /available_payments', (done) => {
    request.get(`${API_URL}/available_payments`, (error, response, body) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct payment methods object for GET /available_payments', (done) => {
    const expectedResponse = {
      payment_methods: {
        credit_cards: true,
        paypal: false
      }
    };

    request.get(`${API_URL}/available_payments`, (error, response, body) => {
      if (error) return done(error);
      // The body will be a string, so we need to parse it as JSON
      const parsedBody = JSON.parse(body);
      expect(parsedBody).to.deep.equal(expectedResponse);
      done();
    });
  });

  it('should have Content-Type application/json for GET /available_payments', (done) => {
     request.get(`${API_URL}/available_payments`, (error, response, body) => {
      if (error) return done(error);
      expect(response.headers['content-type']).to.include('application/json');
      done();
    });
  });
});
