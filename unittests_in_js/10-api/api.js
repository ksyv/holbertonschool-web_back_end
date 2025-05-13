const express = require('express');

// Create an instance of express
const app = express();
const PORT = 7865;

app.use(express.json())

// Define the GET / route
app.get('/', (req, res) => {
  // Return the welcome message
  res.send('Welcome to the payment system');
});

// Define the GET /cart/:id route
// :id must be a number. The (\\d+) is a regex to match one or more digits.
app.get('/cart/:id(\\d+)', (req, res) => {
  const cartId = req.params.id;
  res.send(`Payment methods for cart ${cartId}`);
});

// Define the GET /available_payments route
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

// Define the POST /login route
app.post('/login', (req, res) => {
  const userName = req.body.userName;
  if (userName) {
    res.send(`Welcome ${userName}`);
  } else {
    // Optional: Handle cases where userName is not provided
    res.status(400).send('userName is required');
  }
});

// Start the server and listen on the specified port
// We only start listening if the module is run directly
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
  });
}

// Export the app for testing purposes or for requiring in other modules
module.exports = app;
