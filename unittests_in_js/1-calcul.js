
// Rounds two numbers and returns their type operation.

function calculateNumber(type, a, b) {
    // Round both numbers to the nearest integer
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);
  
    // Perform operation based on type
    switch (type) {
      case 'SUM':
        return roundedA + roundedB;
      case 'SUBSTRACT':
        return Math.round(a) - Math.round(b);
      case 'DIVIDE':
        if (roundedB == 0) {
          return 'Error'
        }
        return roundedA / roundedB;
    }
  }   

  // Export the function to make it available for import in other files
  module.exports = calculateNumber;
  