// utils.js

/**
 * @module Utils
 * @description A module containing utility functions.
 */
const Utils = {
  /**
   * Performs a calculation based on the type.
   * Rounds a and b before performing the operation.
   * @param {string} type - The type of operation ('SUM', 'SUBTRACT', 'DIVIDE').
   * @param {number} a - The first number.
   * @param {number} b - The second number.
   * @returns {number|string} The result of the operation, or 'Error' if dividing by zero.
   */
  calculateNumber(type, a, b) {
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);

    if (type === 'SUM') {
      return roundedA + roundedB;
    }
    if (type === 'SUBTRACT') {
      return roundedA - roundedB;
    }
    if (type === 'DIVIDE') {
      if (roundedB === 0) {
        return 'Error';
      }
      return roundedA / roundedB;
    }
    // It's good practice to handle unknown types,
    // though not strictly required by the prompt for this specific test.
    throw new Error('Invalid calculation type');
  }
};

module.exports = Utils;