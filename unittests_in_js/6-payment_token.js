/**
 * @function getPaymentTokenFromAPI
 * @description Simulates fetching a payment token from an API.
 * @param {boolean} success - Determines if the API call is successful.
 * @returns {Promise<object>|undefined} A Promise that resolves with a success object
 * if the input 'success' is true. Otherwise, it does nothing and returns undefined implicitly.
 */
function getPaymentTokenFromAPI(success) {
  if (success) {
    // When success is true, return a resolved promise
    return Promise.resolve({ data: 'Successful response from the API' });
  }
  // When success is false, the function does nothing explicitly,
  // so it implicitly returns undefined.
  // No promise is returned in this case.
}

module.exports = getPaymentTokenFromAPI;