
// Rounds two numbers and returns their sum.

function calculateNumber(a, b) {
    // Round both numbers to the nearest integer
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);
  
    // Return the sum of the rounded numbers
    return roundedA + roundedB;
  }
  
  // Export the function to make it available for import in other files
  module.exports = calculateNumber;
  