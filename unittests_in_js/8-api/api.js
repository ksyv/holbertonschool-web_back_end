const express = require('express');

// Create an instance of express
const app = express();
const PORT = 7865;

// Define the GET / route
app.get('/', (req, res) => {
  // Return the welcome message
  res.send('Welcome to the payment system');
});

// Start the server and listen on the specified port
// We only start listening if the module is run directly (not required by a test file)
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
  });
}

// Export the app for testing purposes or for requiring in other modules
module.exports = app;
