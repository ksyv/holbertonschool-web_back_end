const { expect } = require('chai'); // Using CommonJS require for Chai v4
const getPaymentTokenFromAPI = require('./6-payment_token');

/**
 * Test suite for the getPaymentTokenFromAPI function.
 */
describe('getPaymentTokenFromAPI', () => {
  /**
   * Test case for when success is true.
   * It verifies that the promise resolves with the correct data.
   * Uses the 'done' callback to handle asynchronous behavior.
   * @param {function} done - Mocha's done callback to signal test completion.
   */
  it('should return a resolved promise with success data when success is true', (done) => {
    // Call the function with success = true
    const promise = getPaymentTokenFromAPI(true);

    // Check if the returned value is indeed a Promise
    // This is a good practice, though not strictly required by the prompt for this specific test.
    expect(promise).to.be.an.instanceof(Promise);

    // Handle the promise resolution
    promise.then((response) => {
      // Verify the structure and content of the resolved object
      expect(response).to.deep.equal({ data: 'Successful response from the API' });
      // Call done() to signal that the asynchronous test has completed successfully
      done();
    }).catch((error) => {
      // If the promise is rejected (which it shouldn't be in this case),
      // fail the test by passing the error to done.
      done(error);
    });
  });
});