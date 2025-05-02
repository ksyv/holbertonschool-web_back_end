// Import the assert module for assertions
const assert = require('assert');
// Import the function to be tested
const calculateNumber = require('./0-calcul.js');

// Describe the test suite for the calculateNumber function
describe('calculateNumber', () => {
  // Test case 1: Both numbers are integers
  it('should return 4 when inputs are 1 and 3', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  // Test case 2: One number is float, rounds up
  it('should return 5 when inputs are 1 and 3.7', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  // Test case 3: Both numbers are floats, one rounds down, one rounds up
  it('should return 5 when inputs are 1.2 and 3.7', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  // Test case 4: Both numbers are floats, both round up
  it('should return 6 when inputs are 1.5 and 3.7', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  // Test case 5: One number is integer, one is float rounding down
   it('should return 4 when inputs are 1 and 3.2', () => {
    assert.strictEqual(calculateNumber(1, 3.2), 4);
  });

  // Test case 6: Both numbers are floats, both round down
  it('should return 4 when inputs are 1.2 and 3.2', () => {
    assert.strictEqual(calculateNumber(1.2, 3.2), 4);
  });

  // Test case 7: Edge case with .5 rounding (should round up)
  it('should return 5 when inputs are 1.5 and 3.2', () => {
    assert.strictEqual(calculateNumber(1.5, 3.2), 5); // 2 + 3 = 5
  });

   // Test case 8: Edge case with negative numbers
  it('should return -4 when inputs are -1 and -3', () => {
    assert.strictEqual(calculateNumber(-1, -3), -4);
  });

  // Test case 9: Negative floats
  it('should return -5 when inputs are -1.2 and -3.7', () => {
    assert.strictEqual(calculateNumber(-1.2, -3.7), -5); // -1 + -4 = -5
  });

  // Test case 10: Negative floats rounding up towards zero
  it('should return -4 when inputs are -1.5 and -3.2', () => {
    assert.strictEqual(calculateNumber(-1.5, -3.2), -4); // -1 + -3 = -4
  });

   // Test case 11: Mixed positive and negative
  it('should return 3 when inputs are -1.5 and 3.7', () => {
    assert.strictEqual(calculateNumber(-1.5, 3.7), 3); // -1 + 4 = 3
  });

  // Test case 12: Zero inputs
  it('should return 0 when inputs are 0 and 0', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

   // Test case 13: Zero and positive float
  it('should return 4 when inputs are 0 and 3.7', () => {
    assert.strictEqual(calculateNumber(0, 3.7), 4); // 0 + 4 = 4
  });

  // Test case 14: Zero and negative float
  it('should return -3 when inputs are 0 and -3.2', () => {
    assert.strictEqual(calculateNumber(0, -3.2), -3); // 0 + -3 = -3
  });

  // Test case 15: Large numbers
  it('should handle large numbers correctly', () => {
    assert.strictEqual(calculateNumber(1000000.4, 2000000.6), 3000001); // 1000000 + 2000001
  });

  // Test case 16: Numbers very close to .5 boundary (below)
  it('should round down correctly for numbers just below .5', () => {
    assert.strictEqual(calculateNumber(2.4999999, 3.4999999), 5); // 2 + 3 = 5
  });

   // Test case 18: One number exactly .5
   it('should handle one number exactly at .5 correctly', () => {
    assert.strictEqual(calculateNumber(1, 3.5), 5); // 1 + 4 = 5
  });

});
