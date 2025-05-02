// Import the assert module for assertions
const assert = require('assert');
// Import the function to be tested
const calculateNumber = require('./1-calcul.js');

// Describe the test suite for the calculateNumber function
describe('calculateNumber', () => {
  // Describe the test suite for the calculateNumber function when type is SUM
  describe('type == SUM', () => {
    // Test case 1: Both numbers are integers
    it('should return 4 when inputs are 1 and 3', () => {
      assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    });

    // Test case 2: One number is float, rounds up
    it('should return 5 when inputs are 1 and 3.7', () => {
      assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    });

    // Test case 3: Both numbers are floats, one rounds down, one rounds up
    it('should return 5 when inputs are 1.2 and 3.7', () => {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    });

    // Test case 4: Both numbers are floats, both round up
    it('should return 6 when inputs are 1.5 and 3.7', () => {
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
    });

    // Test case 5: One number is integer, one is float rounding down
    it('should return 4 when inputs are 1 and 3.2', () => {
      assert.strictEqual(calculateNumber('SUM', 1, 3.2), 4);
    });

    // Test case 6: Both numbers are floats, both round down
    it('should return 4 when inputs are 1.2 and 3.2', () => {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.2), 4);
    });

    // Test case 7: Edge case with .5 rounding (should round up)
    it('should return 5 when inputs are 1.5 and 3.2', () => {
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.2), 5); // 2 + 3 = 5
    });

    // Test case 8: Edge case with negative numbers
    it('should return -4 when inputs are -1 and -3', () => {
      assert.strictEqual(calculateNumber('SUM', -1, -3), -4);
    });

    // Test case 9: Negative floats
    it('should return -5 when inputs are -1.2 and -3.7', () => {
      assert.strictEqual(calculateNumber('SUM', -1.2, -3.7), -5); // -1 + -4 = -5
    });

    // Test case 10: Negative floats rounding up towards zero
    it('should return -4 when inputs are -1.5 and -3.2', () => {
      assert.strictEqual(calculateNumber('SUM', -1.5, -3.2), -4); // -1 + -3 = -4
    });

    // Test case 11: Mixed positive and negative
    it('should return 3 when inputs are -1.5 and 3.7', () => {
      assert.strictEqual(calculateNumber('SUM', -1.5, 3.7), 3); // -1 + 4 = 3
    });

    // Test case 12: Zero inputs
    it('should return 0 when inputs are 0 and 0', () => {
      assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
    });

    // Test case 13: Zero and positive float
    it('should return 4 when inputs are 0 and 3.7', () => {
      assert.strictEqual(calculateNumber('SUM', 0, 3.7), 4); // 0 + 4 = 4
    });

    // Test case 14: Zero and negative float
    it('should return -3 when inputs are 0 and -3.2', () => {
      assert.strictEqual(calculateNumber('SUM', 0, -3.2), -3); // 0 + -3 = -3
    });

    // Test case 15: Large numbers
    it('should handle large numbers correctly', () => {
      assert.strictEqual(calculateNumber('SUM', 1000000.4, 2000000.6), 3000001); // 1000000 + 2000001
    });

    // Test case 16: Numbers very close to .5 boundary (below)
    it('should round down correctly for numbers just below .5', () => {
      assert.strictEqual(calculateNumber('SUM', 2.4999999, 3.4999999), 5); // 2 + 3 = 5
    });

    // Test case 17: One number exactly .5
    it('should handle one number exactly at .5 correctly', () => {
      assert.strictEqual(calculateNumber('SUM', 1, 3.5), 5); // 1 + 4 = 5
    });
  });
  // Describe the test suite for the calculateNumber function when type is SUBSTRACT
  describe('type == SUBSTRACT', () => {
    // Test case 1: Both numbers are integers
    it('should return -2 when inputs are 1 and 3', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 1, 3), -2);
    });

    // Test case 2: One number is float, rounds up
    it('should return -3 when inputs are 1 and 3.7', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 1, 3.7), -3);
    });

    // Test case 3: Both numbers are floats, one rounds down, one rounds up
    it('should return -3 when inputs are 1.2 and 3.7', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 1.2, 3.7), -3);
    });

    // Test case 4: Both numbers are floats, both round up
    it('should return -2 when inputs are 1.5 and 3.7', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 1.5, 3.7), -2);
    });

    // Test case 5: One number is integer, one is float rounding down
    it('should return -2 when inputs are 1 and 3.2', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 1, 3.2), -2);
    });

    // Test case 6: Both numbers are floats, both round down
    it('should return -2 when inputs are 1.2 and 3.2', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 1.2, 3.2), -2);
    });

    // Test case 7: Edge case with .5 rounding (should round up)
    it('should return -1 when inputs are 1.5 and 3.2', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 1.5, 3.2), -1);
    });

    // Test case 8: Edge case with negative numbers
    it('should return 2 when inputs are -1 and -3', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', -1, -3), 2);
    });

    // Test case 9: Negative floats
    it('should return 3 when inputs are -1.2 and -3.7', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', -1.2, -3.7), 3); 
    });

    // Test case 10: Negative floats rounding up towards zero
    it('should return 2 when inputs are -1.5 and -3.2', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', -1.5, -3.2), 2); 
    });

    // Test case 11: Mixed positive and negative
    it('should return -5 when inputs are -1.5 and 3.7', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', -1.5, 3.7), -5);
    });

    // Test case 12: Zero inputs
    it('should return 0 when inputs are 0 and 0', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 0, 0), 0);
    });

    // Test case 13: Zero and positive float
    it('should return -4 when inputs are 0 and 3.7', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 0, 3.7), -4);
    });

    // Test case 14: Zero and negative float
    it('should return 3 when inputs are 0 and -3.2', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 0, -3.2), 3);
    });

    // Test case 15: Large numbers
    it('should handle large numbers correctly', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 1000000.4, 2000000.6), -1000001);
    });

    // Test case 16: Numbers very close to .5 boundary (below)
    it('should round down correctly for numbers just below .5', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 2.4999999, 3.4999999), -1);
    });

    // Test case 17: One number exactly .5
    it('should handle one number exactly at .5 correctly', () => {
      assert.strictEqual(calculateNumber('SUBSTRACT', 1, 3.5), -3);
    });
  });
    // Describe the test suite for the calculateNumber function when type is DIVIDE
    describe('type == DIVIDE', () => {
      it('should divide two integers (6 / 3)', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 6, 3), 2);
      });
  
      it('should divide after rounding (1 / 4)', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1, 3.7), 0.25);
      });
  
      it('should divide after rounding both numbers (1 / 4)', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.2, 3.7), 0.25);
      });
  
      it('should divide after rounding both numbers (2 / 4)', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.5, 3.7), 0.5);
      });
  
      it('should divide after rounding both numbers (8 / 2)', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 8.4, 1.5), 4); 
      });
  
      // Crucial test: Division by zero
      it('should return "Error" when dividing by zero (rounded)', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error'); 
      });
  
      it('should return "Error" when dividing by zero (integer)', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 5, 0), 'Error');
      });
  
       it('should return "Error" when dividing by zero (rounded close to zero)', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.2), 'Error'); 
      });
  
       it('should divide negative numbers (-8 / -1)', () => { 
        assert.strictEqual(calculateNumber('DIVIDE', -8.4, -1.5), 8);
       });
    });
})
