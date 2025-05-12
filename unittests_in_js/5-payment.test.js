const sinon = require('sinon');
const { expect } = require('chai'); // Using CommonJS require for Chai v4
// We don't need to require Utils here if we are not stubbing or spying on its methods directly.
// const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

/**
 * Test suite for the sendPaymentRequestToApi function, using beforeEach and afterEach hooks.
 */
describe('sendPaymentRequestToApi', () => {
  let consoleSpy; // Declare the spy variable in the describe scope

  // Before each test in this suite, set up the spy on console.log
  beforeEach(() => {
    // Create a new spy on console.log before each test
    consoleSpy = sinon.spy(console, 'log');
  });

  // After each test in this suite, restore the spy
  afterEach(() => {
    // Restore the spy to its original state after each test
    consoleSpy.restore();
  });

  /**
   * Test case for sendPaymentRequestToApi(100, 20).
   */
  it('should log "The total is: 120" to the console when called with 100 and 20', () => {
    // Call the function we are testing
    sendPaymentRequestToApi(100, 20);

    // Verify that console.log was called with the correct message
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;

    // Verify that console.log was called exactly once during this test
    expect(consoleSpy.calledOnce).to.be.true;
  });

  /**
   * Test case for sendPaymentRequestToApi(10, 10).
   */
  it('should log "The total is: 20" to the console when called with 10 and 10', () => {
    // Call the function we are testing
    sendPaymentRequestToApi(10, 10);

    // Verify that console.log was called with the correct message
    expect(consoleSpy.calledWith('The total is: 20')).to.be.true;

    // Verify that console.log was called exactly once during this test
    expect(consoleSpy.calledOnce).to.be.true;
  });
});