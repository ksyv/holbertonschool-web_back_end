<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Resources

## Table of Contents :

  - [0. Install a redis instance](#subparagraph0)
  - [1. Node Redis Client](#subparagraph1)
  - [2. Node Redis client and basic operations](#subparagraph2)
  - [3. Node Redis client and async operations](#subparagraph3)
  - [4. Node Redis client and advanced operations](#subparagraph4)
  - [5. Node Redis client publisher and subscriber](#subparagraph5)
  - [6. Create the Job creator](#subparagraph6)
  - [7. Create the Job processor](#subparagraph7)
  - [8. Track progress and errors with Kue: Create the Job creator](#subparagraph8)
  - [9. Track progress and errors with Kue: Create the Job processor](#subparagraph9)
  - [10. Writing the job creation function](#subparagraph10)
  - [11. Writing the test for job creation](#subparagraph11)
  - [12. In stock?](#subparagraph12)

## Resources
### Read or watch:
* [Redis quick start](https://redis.io/docs/latest/integrate/)
* [Redis client interface](https://redis.io/docs/latest/)
* [Redis client for Node JS](https://github.com/redis/node-redis)
* [Kue(deprecated but still use in the industry)](https://github.com/Automattic/kue)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* How to run a Redis server on your machine
* How to run simple operations with the Redis client
* How to use a Redis client with Node JS for basic operations
* How to store hash values in Redis
* How to deal with async operations with Redis
* How to use Kue as a queue system
* How to build a basic Express app interacting with a Redis server
* How to the build a basic Express app interacting with a Redis server and queue

## Requirements
### General
* All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
* All of your files should end with a new line
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use thejsextension

## Task
### 0. Install a redis instance <a name='subparagraph0'></a>

Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - <a href="/rltoken/CrunG4jBw9YkIIJ9pbFJ2Q" target="_blank" title="https://redis.io/downloads/">https://redis.io/downloads/</a>):

```
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
```

* Start Redis in the background with <code>src/redis-server</code>

```
$ src/redis-server &
```

* Make sure that the server is working with a ping <code>src/redis-cli ping</code>

```
PONG
```

* Using the Redis client again, set the value <code>School</code> for the key <code>Holberton</code>

```
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```

* Kill the server with the process id of the redis-server (hint: use <code>ps</code> and <code>grep</code>)

```
$ kill [PID_OF_Redis_Server]
```

Copy the <code>dump.rdb</code> from the <code>redis-5.0.7</code> directory into the root of the Queuing project.

Requirements:

* Running <code>get Holberton</code> in the client, should return <code>School</code>

---

### 1. Node Redis Client <a name='subparagraph1'></a>

Install <a href="/rltoken/y1WPXQxH-S7Op_P2bh7dPg" target="_blank" title="node_redis">node_redis</a> using npm

Using Babel and ES6, write a script named <code>0-redis_client.js</code>. It should connect to the Redis server running on your machine:

* It should log to the console the message <code>Redis client connected to the server</code> when the connection to Redis works correctly
* It should log to the console the message <code>Redis client not connected to the server: ERROR_MESSAGE</code> when the connection to Redis does not work

<strong>Requirements:</strong>

* To import the library, you need to use the keyword <code>import</code>

```
bob@dylan:~$ ps ax | grep redis-server
 2070 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-redis_client.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
^C
bob@dylan:~$ 
bob@dylan:~$ ./src/redis-server > /dev/null 2>&1 &
[1] 2073
bob@dylan:~$ ps ax | grep redis-server
 2073 pts/0    Sl     0:00 ./src/redis-server *:6379
 2078 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$
bob@dylan:~$ npm run dev 0-redis_client.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client connected to the server
^C
bob@dylan:~$
```

---

### 2. Node Redis client and basic operations <a name='subparagraph2'></a>

In a file <code>1-redis_op.js</code>, copy the code you previously wrote (<code>0-redis_client.js</code>).

Add two functions:

* <code>setNewSchool</code>:


  * It accepts two arguments <code>schoolName</code>, and <code>value</code>.
  * It should set in Redis the value for the key <code>schoolName</code>
  * It should display a confirmation message using <code>redis.print</code>
* <code>displaySchoolValue</code>:


  * It accepts one argument <code>schoolName</code>.
  * It should log to the console the value for the key passed as argument

At the end of the file, call:

* <code>displaySchoolValue('Holberton');</code>
* <code>setNewSchool('HolbertonSanFrancisco', '100');</code>
* <code>displaySchoolValue('HolbertonSanFrancisco');</code>

<strong>Requirements:</strong>

* Use callbacks for any of the operation, we will look at async operations later

```
bob@dylan:~$ npm run dev 1-redis_op.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "1-redis_op.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 1-redis_op.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
```

---

### 3. Node Redis client and async operations <a name='subparagraph3'></a>

In a file <code>2-redis_op_async.js</code>, let’s copy the code from the previous exercise (<code>1-redis_op.js</code>)

Using <code>promisify</code>, modify the function <code>displaySchoolValue</code> to use ES6 <code>async / await</code>

Same result as <code>1-redis_op.js</code>

```
bob@dylan:~$ npm run dev 2-redis_op_async.js

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "2-redis_op_async.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 2-redis_op_async.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
```

---

### 4. Node Redis client and advanced operations <a name='subparagraph4'></a>

In a file named <code>4-redis_advanced_op.js</code>, let’s use the client to store a hash value

Using <code>hset</code>, let’s store the following:

* The key of the hash should be <code>HolbertonSchools</code>
* It should have a value for:


  * <code>Portland=50</code>
  * <code>Seattle=80</code>
  * <code>New York=20</code>
  * <code>Bogota=20</code>
  * <code>Cali=40</code>
  * <code>Paris=2</code>
* Make sure you use <code>redis.print</code> for each <code>hset</code>

Using <code>hgetall</code>, display the object stored in Redis. It should return the following:

<strong>Requirements:</strong>

* Use callbacks for any of the operation, we will look at async operations later

```
bob@dylan:~$ npm run dev 4-redis_advanced_op.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "4-redis_advanced_op.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 4-redis_advanced_op.js`
Redis client connected to the server
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
{
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
}
^C
bob@dylan:~$
```

---

### 5. Node Redis client publisher and subscriber <a name='subparagraph5'></a>

In a file named <code>5-subscriber.js</code>, create a redis client:

* On connect, it should log the message <code>Redis client connected to the server</code>
* On error, it should log the message <code>Redis client not connected to the server: ERROR MESSAGE</code>
* It should subscribe to the channel <code>holberton school channel</code>
* When it receives message on the channel <code>holberton school channel</code>, it should log the message to the console
* When the message is <code>KILL_SERVER</code>, it should unsubscribe and quit

In a file named <code>5-publisher.js</code>, create a redis client:

* On connect, it should log the message <code>Redis client connected to the server</code>
* On error, it should log the message <code>Redis client not connected to the server: ERROR MESSAGE</code>
* Write a function named <code>publishMessage</code>:


  * It will take two arguments: <code>message</code> (string), and <code>time</code> (integer - in ms)
  * After <code>time</code> millisecond:


    * The function should log to the console <code>About to send MESSAGE</code>
    * The function should publish to the channel <code>holberton school channel</code>, the message passed in argument after the time passed in arguments
* At the end of the file, call:

```
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
```

<strong>Requirements:</strong>

* You only need one Redis server to execute the program
* You will need to have two node processes to run each script at the same time

<strong>Terminal 1:</strong>

```
bob@dylan:~$ npm run dev 5-subscriber.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "5-subscriber.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-subscriber.js`
Redis client connected to the server
```

<strong>Terminal 2:</strong>

```
bob@dylan:~$ npm run dev 5-publisher.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "5-publisher.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-publisher.js`
Redis client connected to the server
About to send Holberton Student #1 starts course
About to send Holberton Student #2 starts course
About to send KILL_SERVER
About to send Holberton Student #3 starts course
^C
bob@dylan:~$
```

<strong>And in the same time in Terminal 1:</strong>

```
Redis client connected to the server
Holberton Student #1 starts course
Holberton Student #2 starts course
KILL_SERVER
[nodemon] clean exit - waiting for changes before restart
^C
bob@dylan:~$
```

Now you have a basic Redis-based queuing system where you have a process to generate job and a second one to process it. These 2 processes can be in 2 different servers, which we also call “background workers”.

---

### 6. Create the Job creator <a name='subparagraph6'></a>

In a file named <code>6-job_creator.js</code>:

* Create a queue with <code>Kue</code>
* Create an object containing the Job data with the following format:

```
{
  phoneNumber: string,
  message: string,
}
```

* Create a queue named <code>push_notification_code</code>, and create a job with the object created before
* When the job is created without error, log to the console <code>Notification job created: JOB ID</code>
* When the job is completed, log to the console <code>Notification job completed</code>
* When the job is failing, log to the console <code>Notification job failed</code>

```
bob@dylan:~$ npm run dev 6-job_creator.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 1
```

Nothing else will happen - to process the job, go to the next task!

If you execute multiple time this file, you will see the <code>JOB ID</code> increasing - it means you are storing new job to process…

---

### 7. Create the Job processor <a name='subparagraph7'></a>

In a file named <code>6-job_processor.js</code>:

* Create a queue with <code>Kue</code>
* Create a function named <code>sendNotification</code>:


  * It will take two arguments <code>phoneNumber</code> and <code>message</code>
  * It will log to the console <code>Sending notification to PHONE_NUMBER, with message: MESSAGE</code>
* Write the queue process that will listen to new jobs on <code>push_notification_code</code>:


  * Every new job should call the <code>sendNotification</code> function with the phone number and the message contained within the job data

<strong>Requirements:</strong>

* You only need one Redis server to execute the program
* You will need to have two node processes to run each script at the same time
* You muse use <code>Kue</code> to set up the queue

<strong>Terminal 2:</strong>

```
bob@dylan:~$ npm run dev 6-job_processor.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_processor.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_processor.js`
Sending notification to 4153518780, with message: This is the code to verify your account
```

<strong>Terminal 1:</strong> let’s queue a new job!

```
bob@dylan:~$ npm run dev 6-job_creator.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 2
```

<strong>And in the same time in Terminal 2:</strong>

```
Sending notification to 4153518780, with message: This is the code to verify your account
```

BOOM! same as <code>5-subscriber.js</code> and <code>5-publisher.js</code> but with a module to manage jobs.

---

### 8. Track progress and errors with Kue: Create the Job creator <a name='subparagraph8'></a>

In a file named <code>7-job_creator.js</code>:

Create an array <code>jobs</code> with the following data inside:

```
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];
```

After this array created:

* Create a queue with <code>Kue</code>
* Write a loop that will go through the array <code>jobs</code> and for each object:


  * Create a new job to the queue <code>push_notification_code_2</code> with the current object
  * If there is no error, log to the console <code>Notification job created: JOB_ID</code>
  * On the job completion, log to the console <code>Notification job JOB_ID completed</code>
  * On the job failure, log to the console <code>Notification job JOB_ID failed: ERROR</code>
  * On the job progress, log to the console <code>Notification job JOB_ID PERCENTAGE% complete</code>

<strong>Terminal 1</strong>:

```
bob@dylan:~$ npm run dev 7-job_creator.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "7-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 7-job_creator.js`
Notification job created: 39
Notification job created: 40
Notification job created: 41
Notification job created: 42
Notification job created: 43
Notification job created: 44
Notification job created: 45
Notification job created: 46
Notification job created: 47
Notification job created: 48
Notification job created: 49
```

---

### 9. Track progress and errors with Kue: Create the Job processor <a name='subparagraph9'></a>

In a file named <code>7-job_processor.js</code>:

Create an array that will contain the blacklisted phone numbers. Add in it <code>4153518780</code> and <code>4153518781</code> - these 2 numbers will be blacklisted by our jobs processor.

Create a function <code>sendNotification</code> that takes 4 arguments: <code>phoneNumber</code>, <code>message</code>, <code>job</code>, and <code>done</code>:

* When the function is called, track the progress of the <code>job</code> of <code>0</code> out of <code>100</code>
* If <code>phoneNumber</code> is included in the “blacklisted array”, fail the job with an <code>Error</code> object and the message: <code>Phone number PHONE_NUMBER is blacklisted</code>
* Otherwise: 


  * Track the progress to 50%
  * Log to the console <code>Sending notification to PHONE_NUMBER, with message: MESSAGE</code>

Create a queue with <code>Kue</code> that will proceed job of the queue <code>push_notification_code_2</code> with two jobs at a time.

<strong>Requirements:</strong>

* You only need one Redis server to execute the program
* You will need to have two node processes to run each script at the same time
* You muse use <code>Kue</code> to set up the queue
* Executing the jobs list should log to the console the following:

<strong>Terminal 2:</strong>

```
bob@dylan:~$ npm run dev 7-job_processor.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "7-job_processor.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 7-job_processor.js`
Sending notification to 4153518743, with message: This is the code 4321 to verify your account
Sending notification to 4153538781, with message: This is the code 4562 to verify your account
Sending notification to 4153118782, with message: This is the code 4321 to verify your account
Sending notification to 4153718781, with message: This is the code 4562 to verify your account
Sending notification to 4159518782, with message: This is the code 4321 to verify your account
Sending notification to 4158718781, with message: This is the code 4562 to verify your account
Sending notification to 4153818782, with message: This is the code 4321 to verify your account
Sending notification to 4154318781, with message: This is the code 4562 to verify your account
Sending notification to 4151218782, with message: This is the code 4321 to verify your account
```

<strong>And in the same time in terminal 1:</strong>

```
...
Notification job #39 0% complete
Notification job #40 0% complete
Notification job #39 failed: Phone number 4153518780 is blacklisted
Notification job #40 failed: Phone number 4153518781 is blacklisted
Notification job #41 0% complete
Notification job #41 50% complete
Notification job #42 0% complete
Notification job #42 50% complete
Notification job #41 completed
Notification job #42 completed
Notification job #43 0% complete
Notification job #43 50% complete
Notification job #44 0% complete
Notification job #44 50% complete
Notification job #43 completed
Notification job #44 completed
Notification job #45 0% complete
Notification job #45 50% complete
Notification job #46 0% complete
Notification job #46 50% complete
Notification job #45 completed
Notification job #46 completed
Notification job #47 0% complete
Notification job #47 50% complete
Notification job #48 0% complete
Notification job #48 50% complete
Notification job #47 completed
Notification job #48 completed
Notification job #49 0% complete
Notification job #49 50% complete
Notification job #49 completed
```

---

### 10. Writing the job creation function <a name='subparagraph10'></a>

In a file named <code>8-job.js</code>, create a function named <code>createPushNotificationsJobs</code>:

* It takes into argument <code>jobs</code> (array of objects), and <code>queue</code> (<code>Kue</code> queue)
* If <code>jobs</code> is not an array, it should throw an <code>Error</code> with message: <code>Jobs is not an array</code>
* For each job in <code>jobs</code>, create a job in the queue <code>push_notification_code_3</code>
* When a job is created, it should log to the console <code>Notification job created: JOB_ID</code>
* When a job is complete, it should log to the console <code>Notification job JOB_ID completed</code>
* When a job is failed, it should log to the console <code>Notification job JOB_ID failed: ERROR</code>
* When a job is making progress, it should log to the console <code>Notification job JOB_ID PERCENT% complete</code>

```
bob@dylan:~$ cat 8-job-main.js 
import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const list = [
    {
        phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
    }
];
createPushNotificationsJobs(list, queue);

bob@dylan:~$
bob@dylan:~$ npm run dev 8-job-main.js 

> [email protected] dev /root
> nodemon --exec babel-node --presets @babel/preset-env "8-job-main.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 8-job-main.js`
Notification job created: 51
```

---

### 11. Writing the test for job creation <a name='subparagraph11'></a>

Now that you created a job creator, let’s add tests:

* Import the function <code>createPushNotificationsJobs</code>
* Create a queue with <code>Kue</code>
* Write a test suite for the <code>createPushNotificationsJobs</code> function:


  * Use <code>queue.testMode</code> to validate which jobs are inside the queue
  * etc.

<strong>Requirements:</strong>

* Make sure to enter the test mode without processing the jobs before executing the tests
* Make sure to clear the queue and exit the test mode after executing the tests

```
bob@dylan:~$ npm test 8-job.test.js 

> [email protected] test /root
> mocha --require @babel/register --exit "8-job.test.js"



  createPushNotificationsJobs
    ✓ display a error message if jobs is not an array
Notification job created: 1
Notification job created: 2
    ✓ create two new jobs to the queue
...

  123 passing (417ms)
```

---

### 12. In stock? <a name='subparagraph12'></a>

Create an array <code>listProducts</code> containing the list of the following products:

* Id: 1, name: <code>Suitcase 250</code>, price: 50, stock: 4
* Id: 2, name: <code>Suitcase 450</code>, price: 100, stock: 10
* Id: 3, name: <code>Suitcase 650</code>, price: 350, stock: 2
* Id: 4, name: <code>Suitcase 1050</code>, price: 550, stock: 5

Create a function named <code>getItemById</code>:

* It will take <code>id</code> as argument
* It will return the item from <code>listProducts</code> with the same id

Create an <code>express</code> server listening on the port 1245. (You will start it via: <code>npm run dev 9-stock.js</code>)

Create the route <code>GET /list_products</code> that will return the list of every available product with the following JSON format:

```
bob@dylan:~$ curl localhost:1245/list_products ; echo ""
[{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4},{"itemId":2,"itemName":"Suitcase 450","price":100,"initialAvailableQuantity":10},{"itemId":3,"itemName":"Suitcase 650","price":350,"initialAvailableQuantity":2},{"itemId":4,"itemName":"Suitcase 1050","price":550,"initialAvailableQuantity":5}]
bob@dylan:~$
```

Create a client to connect to the Redis server:

* Write a function <code>reserveStockById</code> that will take <code>itemId</code> and <code>stock</code> as arguments:


  * It will set in Redis the stock for the key <code>item.ITEM_ID</code>
* Write an async function <code>getCurrentReservedStockById</code>, that will take <code>itemId</code> as an argument: 


  * It will return the reserved stock for a specific item

Create the route <code>GET /list_products/:itemId</code>, that will return the current product and the current available stock (by using <code>getCurrentReservedStockById</code>) with the following JSON format:

```
bob@dylan:~$ curl localhost:1245/list_products/1 ; echo ""
{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4,"currentQuantity":4}
bob@dylan:~$
```

If the item does not exist, it should return:

```
bob@dylan:~$ curl localhost:1245/list_products/12 ; echo ""
{"status":"Product not found"}
bob@dylan:~$
```

Create the route <code>GET /reserve_product/:itemId</code>:

* If the item does not exist, it should return:

```
bob@dylan:~$ curl localhost:1245/reserve_product/12 ; echo ""
{"status":"Product not found"}
bob@dylan:~$
```

* If the item exists, it should check that there is at least one stock available. If not it should return:

```
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Not enough stock available","itemId":1}
bob@dylan:~$
```

* If there is enough stock available, it should reserve one item (by using <code>reserveStockById</code>), and return:

```
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Reservation confirmed","itemId":1}
bob@dylan:~$
```

<strong>Requirements:</strong>

* Make sure to use <code>promisify</code> with Redis
* Make sure to use the <code>await</code>/<code>async</code> keyword to get the value from Redis
* Make sure the format returned by the web application is always JSON and not text

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
