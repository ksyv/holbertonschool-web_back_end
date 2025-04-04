<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Resources

## Table of Contents :

  - [0. Writing strings to Redis](#subparagraph0)
  - [1. Reading from Redis and recovering original type](#subparagraph1)
  - [2. Incrementing values](#subparagraph2)
  - [3. Storing lists](#subparagraph3)
  - [4. Retrieving lists](#subparagraph4)

## Resources
### Read or watch:
* [Redis commands](https://redis.io/docs/latest/commands/)
* [Redis python client](https://redis-py.readthedocs.io/en/stable/)
* [How to Use Redis With Python](https://realpython.com/python-redis/)
* [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998&themeRefresh=1)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache

## Requirements
### General
* All of your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
* All of your files should end with a new line
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* The first line of all your files should be exactly#!/usr/bin/env python3
* Your code should use thepycodestylestyle (version 2.5)
* All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions and methods should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'andpython3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

## Task
### 0. Writing strings to Redis <a name='subparagraph0'></a>

Create a <code>Cache</code> class. In the <code>__init__</code> method, store an instance of the Redis client as a private variable named <code>_redis</code> (using <code>redis.Redis()</code>) and flush the instance using <code>flushdb</code>.

Create a <code>store</code> method that takes a <code>data</code> argument and returns a string. The method should generate a random key (e.g. using <code>uuid</code>), store the input data in Redis using the random key and return the key.

Type-annotate <code>store</code> correctly. Remember that <code>data</code> can be a <code>str</code>, <code>bytes</code>, <code>int</code> or <code>float</code>.

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

bob@dylan:~$ python3 main.py 
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
bob@dylan:~$
```

---

### 1. Reading from Redis and recovering original type <a name='subparagraph1'></a>

Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store <code>"a"</code> as a UTF-8 string, it will be returned as <code>b"a"</code> when retrieved from the server.

In this exercise we will create a <code>get</code> method that take a <code>key</code> string argument and an optional <code>Callable</code> argument named <code>fn</code>. This callable will be used to convert the data back to the desired format.

Remember to conserve the original <code>Redis.get</code> behavior if the key does not exist.

Also, implement 2 new methods: <code>get_str</code> and <code>get_int</code> that will automatically parametrize <code>Cache.get</code> with the correct conversion function.

The following code should not raise:

```
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```

---

### 2. Incrementing values <a name='subparagraph2'></a>

Familiarize yourself with the <code>INCR</code> command and its python equivalent.

In this task, we will implement a system to count how many times methods of the <code>Cache</code> class are called.

Above <code>Cache</code> define a <code>count_calls</code> decorator that takes a single <code>method</code> <code>Callable</code> argument and returns a <code>Callable</code>.

As a key, use the qualified name of <code>method</code> using the <code>__qualname__</code> dunder method.

Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.

Remember that the first argument of the wrapped function will be <code>self</code> which is the instance itself, which lets you access the Redis instance.

Protip: when defining a decorator it is useful to use <code>functool.wraps</code> to conserve the original function’s name, docstring, etc. Make sure you use it as described <a href="/rltoken/KzeKedfUQXfD6x6u2OmY-A" target="_blank" title="here">here</a>.

Decorate <code>Cache.store</code> with <code>count_calls</code>.

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))

bob@dylan:~$ ./main.py
b'1'
b'3'
bob@dylan:~$
```

---

### 3. Storing lists <a name='subparagraph3'></a>

Familiarize yourself with redis commands <code>RPUSH</code>, <code>LPUSH</code>, <code>LRANGE</code>, etc.

In this task, we will define a <code>call_history</code> decorator to store the history of inputs and outputs for a particular function.

Everytime the original function will be called, we will add its input parameters to one list in redis, and store its output into another list.

In <code>call_history</code>, use the decorated function’s qualified name and append <code>":inputs"</code> and <code>":outputs"</code> to create input and output list keys, respectively.

<code>call_history</code> has a single parameter named <code>method</code> that is a <code>Callable</code> and returns a <code>Callable</code>.

In the new function that the decorator will return, use <code>rpush</code> to append the input arguments. Remember that Redis can only store strings, bytes and numbers. Therefore, we can simply use <code>str(args)</code> to normalize. We can ignore potential <code>kwargs</code> for now.

Execute the wrapped function to retrieve the output. Store the output using <code>rpush</code> in the <code>"...:outputs"</code> list, then return the output.

Decorate <code>Cache.store</code> with <code>call_history</code>.

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))

bob@dylan:~$ ./main.py
04f8dcaa-d354-4221-87f3-4923393a25ad
a160a8a8-06dc-4934-8e95-df0cb839644b
15a8fd87-1f55-4059-86aa-9d1a0d4f2aea
inputs: [b"('first',)", b"('secont',)", b"('third',)"]
outputs: [b'04f8dcaa-d354-4221-87f3-4923393a25ad', b'a160a8a8-06dc-4934-8e95-df0cb839644b', b'15a8fd87-1f55-4059-86aa-9d1a0d4f2aea']
bob@dylan:~$
```

---

### 4. Retrieving lists <a name='subparagraph4'></a>

In this tasks, we will implement a <code>replay</code> function to display the history of calls of a particular function.

Use keys generated in previous tasks to generate the following output:

```
>>> cache = Cache()
>>> cache.store("foo")
>>> cache.store("bar")
>>> cache.store(42)
>>> replay(cache.store)
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
```

Tip: use <code>lrange</code> and <code>zip</code> to loop over inputs and outputs.

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
