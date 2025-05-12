const sinon = require('sinon');
const { expect } = require('chai'); // Using CommonJS require for Chai v4
const Utils = require('./utils'); // We still need Utils to stub its method
const sendPaymentRequestToApi = require('./4-payment');

/**
 * Test suite for the sendPaymentRequestToApi function, using a stub.
 */
describe('sendPaymentRequestToApi', () => {
  let calculateNumberStub;
  let consoleSpy;

  // Before each test in this suite
  beforeEach(() => {
    // Stub Utils.calculateNumber to always return 10
    // This prevents the actual Utils.calculateNumber from being called.
    calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Spy on console.log to verify its output
    consoleSpy = sinon.spy(console, 'log');
  });

  // After each test, restore the stub and the spy
  afterEach(() => {
    calculateNumberStub.restore();
    consoleSpy.restore();
  });

  /**
   * Test case to verify the stubbed Utils.calculateNumber and console.log.
   */
  it('should call Utils.calculateNumber with SUM, 100, 20 and log "The total is: 10"', () => {
    // Call the function we are testing
    sendPaymentRequestToApi(100, 20);

    // Verify that the stub (Utils.calculateNumber) was called exactly once
    expect(calculateNumberStub.calledOnce).to.be.true;

    // Verify that the stub was called with the correct arguments
    // Even though it's stubbed, we can still check what it was called with.
    expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true;

    // Verify that console.log was called exactly once
    expect(consoleSpy.calledOnce).to.be.true;

    // Verify that console.log was called with the correct message
    // The message should reflect the stubbed return value (10)
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
  });
});
