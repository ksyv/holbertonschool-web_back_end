// 3-payment.test.js

const sinon = require('sinon');
const { expect } = require('chai'); // Using expect assertion style from Chai
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

/**
 * Test suite for the sendPaymentRequestToApi function.
 */
describe('sendPaymentRequestToApi', () => {
  let consoleSpy;

  // Before each test, spy on console.log to suppress output during tests
  // and allow us to check if it was called (though not required by this specific prompt)
  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });

  // After each test, restore the spy to its original state
  afterEach(() => {
    consoleSpy.restore();
  });

  /**
   * Test case to verify the usage of Utils.calculateNumber.
   * It checks if Utils.calculateNumber is called with the correct arguments
   * when sendPaymentRequestToApi is invoked.
   */
  it('should call Utils.calculateNumber with SUM, 100, and 20', () => {
    // Create a spy on the Utils.calculateNumber method
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');

    // Call the function we are testing
    sendPaymentRequestToApi(100, 20);

    // Assert that the spy (Utils.calculateNumber) was called exactly once
    expect(calculateNumberSpy.calledOnce).to.be.true;

    // Assert that the spy was called with the correct arguments
    // sinon.assert.calledWith() is another way to do this:
    // sinon.assert.calledWithExactly(calculateNumberSpy, 'SUM', 100, 20);
    // Or using Chai with Sinon-Chai (if installed) or checking args directly:
    expect(calculateNumberSpy.calledWith('SUM', 100, 20)).to.be.true;

    // Restore the spy to its original state to avoid interference with other tests
    calculateNumberSpy.restore();
  });

  it('should log the correct total to the console', () => {
    // Call the function we are testing
    sendPaymentRequestToApi(100, 20);

    // Assert that console.log was called with the correct message
    // This also implicitly tests that Utils.calculateNumber returned the correct sum (120)
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
    expect(consoleSpy.calledOnce).to.be.true; // Ensure it's only called once
  });
});