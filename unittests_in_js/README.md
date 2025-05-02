<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Resources

## Table of Contents :

  - [0. Basic test with Mocha and Node assertion library](#subparagraph0)
  - [1. Combining descriptions](#subparagraph1)
  - [2. Basic test using Chai assertion library](#subparagraph2)
  - [3. Spies](#subparagraph3)
  - [4. Stubs](#subparagraph4)
  - [5. Hooks](#subparagraph5)
  - [6. Async tests with done](#subparagraph6)
  - [7. Skip](#subparagraph7)
  - [8. Basic Integration testing](#subparagraph8)
  - [9. Regex integration testing](#subparagraph9)
  - [10. Deep equality & Post integration testing](#subparagraph10)

## Resources
### Read or watch:
* [Mocha documentation](https://mochajs.org/)
* [Chai](https://www.chaijs.com/api/)
* [Sinon](https://sinonjs.org/#get-started)
* [Express](https://expressjs.com/en/guide/routing.html)
* [Request](https://www.npmjs.com/package/request)
* [How to Test NodeJS Apps using Mocha, Chai and SinonJS](https://www.digitalocean.com/community)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* How to use Mocha to write a test suite
* How to use different assertion libraries (Node or Chai)
* How to present long test suites
* When and how to use spies
* When and how to use stubs
* What are hooks and when to use them
* Unit testing with Async functions
* How to write integration tests with a small node server

## Requirements
### General
* All of your code will be executed on Ubuntu 20.04 using Node 20.x.x
* Allowed editors:vi,vim,emacs,Visual Studio Code
* All your files should end with a new line
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use thejsextension
* When running every test withnpm run test *.test.js, everything should pass correctly without any warning or error

## Task
### 0. Basic test with Mocha and Node assertion library <a name='subparagraph0'></a>

<strong>Install Mocha using npm:</strong>

* Set up a scripts in your <code>package.json</code> to quickly run Mocha using <code>npm test</code>
* You have to use <code>assert</code>

<strong>Create a new file named <code>0-calcul.js</code>:</strong>

* Create a function named <code>calculateNumber</code>. It should accepts two arguments (number) <code>a</code> and <code>b</code>
* The function should round <code>a</code> and <code>b</code> and return the sum of it

<strong>Test cases</strong>

* Create a file <code>0-calcul.test.js</code> that contains test cases of this function
* You can assume <code>a</code> and <code>b</code> are always number
* Tests should be around the “rounded” part

<strong>Tips:</strong>

* For the sake of the example, this test suite is slightly extreme and probably not needed
* However, remember that your tests should not only verify what a function is supposed to do, but also the edge cases

<strong>Requirements:</strong>

* You have to use <code>assert</code>
* You should be able to run the test suite using <code>npm test 0-calcul.test.js</code>
* Every test should pass without any warning

<strong>Expected output</strong>

```
> const calculateNumber = require("./0-calcul.js");
> calculateNumber(1, 3)
4
> calculateNumber(1, 3.7)
5
> calculateNumber(1.2, 3.7)
5
> calculateNumber(1.5, 3.7)
6
>
```

<strong>Run test</strong>

```
bob@dylan:~$ npm test 0-calcul.test.js 

> [email protected] test /root
> ./node_modules/mocha/bin/mocha "0-calcul.test.js"

  calculateNumber
    ✓ ...
    ✓ ...
    ✓ ...
    ...

  130 passing (35ms)
bob@dylan:~$
```

---

### 1. Combining descriptions <a name='subparagraph1'></a>

<strong>Create a new file named <code>1-calcul.js</code>:</strong>

* Upgrade the function you created in the previous task (<code>0-calcul.js</code>)
* Add a new argument named <code>type</code> at first argument of the function. <code>type</code> can be <code>SUM</code>, <code>SUBTRACT</code>, or <code>DIVIDE</code> (string)
* When type is <code>SUM</code>, round the two numbers, and add <code>a</code> from <code>b</code>
* When type is <code>SUBTRACT</code>, round the two numbers, and subtract <code>b</code> from <code>a</code>
* When type is <code>DIVIDE</code>, round the two numbers, and divide <code>a</code> with <code>b</code> - if the rounded value of <code>b</code> is equal to 0, return the string <code>Error</code>

<strong>Test cases</strong>

* Create a file <code>1-calcul.test.js</code> that contains test cases of this function
* You can assume <code>a</code> and <code>b</code> are always number
* Usage of <code>describe</code> will help you to organize your test cases

<strong>Tips:</strong>

* For the sake of the example, this test suite is slightly extreme and probably not needed
* However, remember that your tests should not only verify what a function is supposed to do, but also the edge cases

<strong>Requirements:</strong>

* You have to use <code>assert</code>
* You should be able to run the test suite using <code>npm test 1-calcul.test.js</code>
* Every test should pass without any warning

<strong>Expected output</strong>

```
> const calculateNumber = require("./1-calcul.js");
> calculateNumber('SUM', 1.4, 4.5)
6
> calculateNumber('SUBTRACT', 1.4, 4.5)
-4
> calculateNumber('DIVIDE', 1.4, 4.5)
0.2
> calculateNumber('DIVIDE', 1.4, 0)
'Error'
```

---

### 2. Basic test using Chai assertion library <a name='subparagraph2'></a>

While using Node assert library is completely valid, a lot of developers prefer to have a behavior driven development style. This type being easier to read and therefore to maintain.

<strong>Let’s install Chai with npm:</strong>

* Copy the file <code>1-calcul.js</code> in a new file <code>2-calcul_chai.js</code> (same content, same behavior)
* Copy the file <code>1-calcul.test.js</code> in a new file <code>2-calcul_chai.test.js</code>
* Rewrite the test suite, using <code>expect</code> from <code>Chai</code>

<strong>Tips:</strong>

* Remember that test coverage is always difficult to maintain. Using an easier style for your tests will help you
* The easier your tests are to read and understand, the more other engineers will be able to fix them when they are modifying your code

<strong>Requirements:</strong>

* You should be able to run the test suite using <code>npm test 2-calcul_chai.test.js</code>
* Every test should pass without any warning

---

### 3. Spies <a name='subparagraph3'></a>

Spies are a useful wrapper that will execute the wrapped function, and log useful information (e.g. was it called, with what arguments). Sinon is a library allowing you to create spies.

<strong>Let’s install Sinon with npm:</strong>

* Create a new file named <code>utils.js</code>
* Create a new module named <code>Utils</code>
* Create a property named <code>calculateNumber</code> and paste your previous code in the function
* Export the Utils module

<strong>Create a new file named <code>3-payment.js</code>:</strong>

* Create a new function named <code>sendPaymentRequestToApi</code>. The function takes two argument <code>totalAmount</code>, and <code>totalShipping</code>
* The function calls the <code>Utils.calculateNumber</code> function with type <code>SUM</code>, <code>totalAmount</code> as <code>a</code>, <code>totalShipping</code> as <code>b</code> and display in the console the message <code>The total is: &lt;result of the sum&gt;</code>

<strong>Create a new file named <code>3-payment.test.js</code> and add a new suite named <code>sendPaymentRequestToApi</code>:</strong>

* By using <code>sinon.spy</code>, make sure the math used for <code>sendPaymentRequestToApi(100, 20)</code> is the same as <code>Utils.calculateNumber('SUM', 100, 20)</code> (validate the usage of the <code>Utils</code> function)

<strong>Requirements:</strong>

* You should be able to run the test suite using <code>npm test 3-payment.test.js</code>
* Every test should pass without any warning
* You should use a <code>spy</code> to complete this exercise

<strong>Tips:</strong>

* Remember to always restore a spy after using it in a test, it will prevent you from having weird behaviors
* Spies are really useful and allow you to focus only on what your code is doing and not the downstream APIs or functions
* Remember that integration test is different from unit test. Your unit test should test your code, not the code of a different function

---

### 4. Stubs <a name='subparagraph4'></a>

Stubs are similar to spies. Except that you can provide a different implementation of the function you are wrapping. Sinon can be used as well for stubs.

<strong>Create a new file <code>4-payment.js</code>, and copy the code from <code>3-payment.js</code></strong> (same content, same behavior)

<strong>Create a new file <code>4-payment.test.js</code>, and copy the code from <code>3-payment.test.js</code></strong>

* Imagine that calling the function <code>Utils.calculateNumber</code> is actually calling an API or a very expensive method. You don’t necessarily want to do that on every test run
* Stub the function <code>Utils.calculateNumber</code> to always return the same number <code>10</code>
* Verify that the stub is being called with <code>type = SUM</code>, <code>a = 100</code>, and <code>b = 20</code>
* Add a spy to verify that <code>console.log</code> is logging the correct message <code>The total is: 10</code>

<strong>Requirements:</strong>

* You should be able to run the test suite using <code>npm test 4-payment.test.js</code>
* Every test should pass without any warning
* You should use a <code>stub</code> to complete this exercise
* Do not forget to restore the spy and the stub

<strong>Tips:</strong>

* Using stubs allows you to greatly speed up your test. When executing thousands of tests, saving a few seconds is important
* Using stubs allows you to control specific edge case (e.g a function throwing an error or returning a specific result like a number or a timestamp)

---

### 5. Hooks <a name='subparagraph5'></a>

Hooks are useful functions that can be called before execute one or all tests in a suite

<strong>Copy the code from <code>4-payment.js</code> into a new file <code>5-payment.js</code>:</strong> (same content/same behavior)

<strong>Create a new file <code>5-payment.test.js</code>:</strong>

* Inside the same <code>describe</code>, create 2 tests:


  * The first test will call <code>sendPaymentRequestToAPI</code> with 100, and 20:


    * Verify that the console is logging the string <code>The total is: 120</code>
    * Verify that the console is only called once
  * The second test will call <code>sendPaymentRequestToAPI</code> with 10, and 10:


    * Verify that the console is logging the string <code>The total is: 20</code>
    * Verify that the console is only called once

<strong>Requirements:</strong>

* You should be able to run the test suite using <code>npm test 5-payment.test.js</code>
* Every test should pass without any warning
* You should use only one <code>spy</code> to complete this exercise
* You should use a <code>beforeEach</code> and a <code>afterEach</code> hooks to complete this exercise

---

### 6. Async tests with done <a name='subparagraph6'></a>

Look into how to support async testing, for example when waiting for the answer of an API or from a Promise

<strong>Create a new file <code>6-payment_token.js</code>:</strong>

* Create a new function named <code>getPaymentTokenFromAPI</code>
* The function will take an argument called <code>success</code> (boolean)
* When <code>success</code> is true, it should return a resolved promise with the object <code>{data: 'Successful response from the API' }</code>
* Otherwise, the function is doing nothing.

<strong>Create a new file <code>6-payment_token.test.js</code> and write a test suite named <code>getPaymentTokenFromAPI</code></strong>

* How to test the result of <code>getPaymentTokenFromAPI(true)</code>?

<strong>Tips:</strong>

* You should be extremely careful when working with async testing. Without calling <code>done</code> properly, your test could be always passing even if what you are actually testing is never executed

<strong>Requirements:</strong>

* You should be able to run the test suite using <code>npm test 6-payment_token.test.js</code>
* Every test should pass without any warning
* You should use the <code>done</code> callback to execute this test

---

### 7. Skip <a name='subparagraph7'></a>

When you have a long list of tests, and you can’t figure out why a test is breaking, avoid commenting out a test, or removing it. <strong>Skip</strong> it instead, and file a ticket to come back to it as soon as possible

You will be using this file, conveniently named <code>7-skip.test.js</code>

```
const { expect } = require('chai');

describe('Testing numbers', () => {
  it('1 is equal to 1', () => {
    expect(1 === 1).to.be.true;
  });

  it('2 is equal to 2', () => {
    expect(2 === 2).to.be.true;
  });

  it('1 is equal to 3', () => {
    expect(1 === 3).to.be.true;
  });

  it('3 is equal to 3', () => {
    expect(3 === 3).to.be.true;
  });

  it('4 is equal to 4', () => {
    expect(4 === 4).to.be.true;
  });

  it('5 is equal to 5', () => {
    expect(5 === 5).to.be.true;
  });

  it('6 is equal to 6', () => {
    expect(6 === 6).to.be.true;
  });

  it('7 is equal to 7', () => {
    expect(7 === 7).to.be.true;
  });
});
```

<strong>Using the file <code>7-skip.test.js</code>:</strong>

* Make the test suite pass <strong>without</strong> fixing or removing the failing test
* <code>it</code> description <strong>must stay</strong> the same

<strong>Tips:</strong>

* Skipping is also very helpful when you only want to execute the test in a particular case (specific environment, or when an API is not behaving correctly)

<strong>Requirements:</strong>

* You should be able to run the test suite using <code>npm test 7-skip.test.js</code>
* Every test should pass without any warning

---

### 8. Basic Integration testing <a name='subparagraph8'></a>

In a folder <code>8-api</code> located at the root of the project directory, copy this <code>package.json</code> over.

```
{
  "name": "8-api",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "./node_modules/mocha/bin/mocha"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  }
}
```

<strong>Create a new file <code>api.js</code>:</strong>

* By using <code>express</code>, create an instance of <code>express</code> called <code>app</code>
* Listen to port 7865 and log <code>API available on localhost port 7865</code> to the browser console when the <code>express</code> server is started
* For the route <code>GET /</code>, return the message <code>Welcome to the payment system</code>

<strong>Create a new file <code>api.test.js</code>:</strong>

* Create one suite for the index page: 


  * Correct status code?
  * Correct result?
  * Other?

<strong>Server</strong>

Terminal 1

```
bob@dylan:~/8-api$  node api.js
API available on localhost port 7865
```

Terminal 2

```
bob@dylan:~/8-api$  curl http://localhost:7865 ; echo ""
Welcome to the payment system
bob@dylan:~/8-api$  
bob@dylan:~/8-api$ npm test api.test.js

> [email protected] test /root/8-api
> ./node_modules/mocha/bin/mocha "api.test.js"



  Index page
    ✓ ...
    ✓ ...
    ...

  23 passing (256ms)

bob@dylan:~/8-api$
```

<strong>Tips:</strong>

* Since this is an integration test, you will need to have your node server running for the test to pass
* You can use the module <code>request</code>

<strong>Requirements:</strong>

* You should be able to run the test suite using <code>npm test api.test.js</code>
* Every test should pass without any warnings

---

### 9. Regex integration testing <a name='subparagraph9'></a>

In a folder <code>9-api</code>, reusing the previous project in <code>8-api</code> (<code>package.json</code>, <code>api.js</code> and <code>api.test.js</code>)

<strong>Modify the file <code>api.js</code>:</strong>

* Add a new endpoint: <code>GET /cart/:id</code>
* <code>:id</code> must be only a number (validation must be in the route definition)
* When access, the endpoint should return <code>Payment methods for cart :id</code>

<strong>Modify the file <code>api.test.js</code>:</strong>

* Add a new test suite for the cart page:


  * Correct status code when <code>:id</code> is a number?
  * Correct status code when <code>:id</code> is NOT a number (=> 404)?
  * etc.

<strong>Server</strong>

Terminal 1

```
bob@dylan:~$ node api.js
API available on localhost port 7865
```

Terminal 2

```
bob@dylan:~$ curl http://localhost:7865/cart/12 ; echo ""
Payment methods for cart 12
bob@dylan:~$ 
bob@dylan:~$ curl http://localhost:7865/cart/hello -v
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 7865 (#0)
> GET /cart/hello HTTP/1.1
> Host: localhost:7865
> User-Agent: curl/7.58.0
> Accept: */*
> 
< HTTP/1.1 404 Not Found
< X-Powered-By: Express
< Content-Security-Policy: default-src 'none'
< X-Content-Type-Options: nosniff
< Content-Type: text/html; charset=utf-8
< Content-Length: 149
< Date: Wed, 15 Jul 2020 08:33:44 GMT
< Connection: keep-alive
< 
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>Cannot GET /cart/hello</pre>
</body>
</html>
* Connection #0 to host localhost left intact
bob@dylan:~$
```

<strong>Tips:</strong>

* You will need to add a small regex in your path to support the usecase

<strong>Requirements:</strong>

* You should be able to run the test suite using <code>npm test api.test.js</code>
* Every test should pass without any warning

---

### 10. Deep equality & Post integration testing <a name='subparagraph10'></a>

In a folder <code>10-api</code>, reusing the previous project in <code>9-api</code> (<code>package.json</code>, <code>api.js</code> and <code>api.test.js</code>)

<strong>Modify the file <code>api.js</code>:</strong>

* Add an endpoint <code>GET /available_payments</code> that returns an object with the following structure:

```
{
  payment_methods: {
    credit_cards: true,
    paypal: false
  }
}
```

* Add an endpoint <code>POST /login</code> that returns the message <code>Welcome :username</code> where <code>:username</code> is the value of the body variable <code>userName</code>.

<strong>Modify the file <code>api.test.js</code>:</strong>

* Add a test suite for the <code>/login</code> endpoint
* Add a test suite for the <code>/available_payments</code> endpoint

<strong>Server</strong>

Terminal 1

```
bob@dylan:~$ node api.js
API available on localhost port 7865
```

Terminal 2

```
bob@dylan:~$ curl http://localhost:7865/available_payments ; echo ""
{"payment_methods":{"credit_cards":true,"paypal":false}}
bob@dylan:~$ 
bob@dylan:~$ curl -XPOST http://localhost:7865/login -d '{ "userName": "Betty" }' -H 'Content-Type: application/json' ; echo ""
Welcome Betty
bob@dylan:~$
```

<strong>Tips:</strong>

* Look at deep equality to compare objects

<strong>Requirements:</strong>

* You should be able to run the test suite using <code>npm test api.test.js</code>
* Every test should pass without any warning
* Your server should not display any error

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
