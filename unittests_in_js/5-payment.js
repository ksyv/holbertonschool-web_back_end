const Utils = require('./utils');

/**
 * @function sendPaymentRequestToApi
 * @description Calculates the total cost (amount + shipping) using Utils.calculateNumber
 * and logs the result to the console.
 * @param {number} totalAmount - The base amount of the payment.
 * @param {number} totalShipping - The shipping cost.
 */
function sendPaymentRequestToApi(totalAmount, totalShipping) {
  // Call Utils.calculateNumber with type SUM
  // The actual Utils.calculateNumber will be executed in this version.
  const total = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  // Display the message in the console
  console.log(`The total is: ${total}`);
}

module.exports = sendPaymentRequestToApi;