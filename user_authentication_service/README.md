<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Resources

## Table of Contents :

  - [0. User model](#subparagraph0)
  - [1. create user](#subparagraph1)
  - [2. Find user](#subparagraph2)
  - [3. update user](#subparagraph3)
  - [4. Hash password](#subparagraph4)
  - [5. Register user](#subparagraph5)
  - [6. Basic Flask app](#subparagraph6)
  - [7. Register user](#subparagraph7)
  - [8. Credentials validation](#subparagraph8)
  - [9. Generate UUIDs](#subparagraph9)
  - [10. Get session ID](#subparagraph10)
  - [11. Log in](#subparagraph11)
  - [12. Find user by session ID](#subparagraph12)
  - [13. Destroy session](#subparagraph13)
  - [14. Log out](#subparagraph14)
  - [15. User profile](#subparagraph15)
  - [16. Generate reset password token](#subparagraph16)
  - [17. Get reset password token](#subparagraph17)
  - [18. Update password](#subparagraph18)
  - [19. Update password end-point](#subparagraph19)

## Resources
### Read or watch:
* [Flask documentation](https://flask.palletsprojects.com/en/stable/quickstart/)
* [Requests module](https://requests.kennethreitz.org/en/latest/user/quickstart/)
* [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* How to declare API routes in a Flask app
* How to get and set cookies
* How to retrieve request form data
* How to return various HTTP status codes

## Requirements
### General
* Allowed editors:vi,vim,emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS usingpython3(version 3.9)
* All your files should end with a new line
* The first line of all your files should be exactly#!/usr/bin/env python3
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use thepycodestylestyle (version 2.5)
* You should useSQLAlchemy
* All your files must be executable
* The length of your files will be tested usingwc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'andpython3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions should be type annotated
* The flask app should only interact withAuthand never withDBdirectly.
* Only public methods ofAuthandDBshould be used outside these classes

## Task
### 0. User model <a name='subparagraph0'></a>

In this task you will create a SQLAlchemy model named <code>User</code> for a database table named <code>users</code> (by using the <a href="/rltoken/GfLP1eOPDGnc6J9hkw0CeA" target="_blank" title="mapping declaration">mapping declaration</a> of SQLAlchemy).

The model will have the following attributes:

* <code>id</code>, the integer primary key
* <code>email</code>, a non-nullable string
* <code>hashed_password</code>, a non-nullable string
* <code>session_id</code>, a nullable string
* <code>reset_token</code>, a nullable string

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))

bob@dylan:~$ python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
bob@dylan:~$
```

---

### 1. create user <a name='subparagraph1'></a>

In this task, you will complete the <code>DB</code> class provided below to implement the <code>add_user</code> method.

```
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
```

Note that <code>DB._session</code> is a private property and hence should NEVER be used from outside the <code>DB</code> class.

Implement the <code>add_user</code> method, which has two required string arguments: <code>email</code> and <code>hashed_password</code>, and returns a <code>User</code> object. The method should save the user to the database. No validations are required at this stage.

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("[email protected]", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("[email protected]", "SuperHashedPwd1")
print(user_2.id)

bob@dylan:~$ python3 main.py
1
2
bob@dylan:~$
```

---

### 2. Find user <a name='subparagraph2'></a>

In this task you will implement the <code>DB.find_user_by</code> method. This method takes in arbitrary keyword arguments and returns the first row found in the <code>users</code> table as filtered by the method’s input arguments. No validation of input arguments required at this point.

Make sure that SQLAlchemy’s <code>NoResultFound</code> and <code>InvalidRequestError</code> are raised when no results are found, or when wrong query arguments are passed, respectively.

<strong>Warning:</strong>

* <code>NoResultFound</code> has been moved from <code>sqlalchemy.orm.exc</code> to <code>sqlalchemy.exc</code> between the version 1.3.x and 1.4.x of SQLAchemy - please make sure you are importing it from <code>sqlalchemy.orm.exc</code>

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

user = my_db.add_user("[email protected]", "PwdHashed")
print(user.id)

find_user = my_db.find_user_by(email="[email protected]")
print(find_user.id)

try:
    find_user = my_db.find_user_by(email="[email protected]")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="[email protected]")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")        

bob@dylan:~$ python3 main.py
1
1
Not found
Invalid
bob@dylan:~$
```

---

### 3. update user <a name='subparagraph3'></a>

In this task, you will implement the <code>DB.update_user</code> method that takes as argument a required <code>user_id</code> integer and arbitrary keyword arguments, and returns <code>None</code>.

The method will use <code>find_user_by</code> to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database.

If an argument that does not correspond to a user attribute is passed, raise a <code>ValueError</code>.

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

email = '[email protected]'
hashed_password = "hashedPwd"

user = my_db.add_user(email, hashed_password)
print(user.id)

try:
    my_db.update_user(user.id, hashed_password='NewPwd')
    print("Password updated")
except ValueError:
    print("Error")

bob@dylan:~$ python3 main.py
1
Password updated
bob@dylan:~$
```

---

### 4. Hash password <a name='subparagraph4'></a>

In this task you will define a <code>_hash_password</code> method that takes in a <code>password</code> string arguments and returns bytes.

The returned bytes is a salted hash of the input password, hashed with <code>bcrypt.hashpw</code>.

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from auth import _hash_password

print(_hash_password("Hello Holberton"))

bob@dylan:~$ python3 main.py
b'$2b$12$eUDdeuBtrD41c8dXvzh95ehsWYCCAi4VH1JbESzgbgZT.eMMzi.G2'
bob@dylan:~$
```

---

### 5. Register user <a name='subparagraph5'></a>

In this task, you will implement the <code>Auth.register_user</code> in the <code>Auth</code> class provided below:

```
from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
```

Note that <code>Auth._db</code> is a private property and should NEVER be used from outside the class.

<code>Auth.register_user</code> should take mandatory <code>email</code> and <code>password</code> string arguments and return a <code>User</code> object.

If a user already exist with the passed email, raise a <code>ValueError</code> with the message <code>User &lt;user's email&gt; already exists</code>.

If not, hash the password with <code>_hash_password</code>, save the user to the database using <code>self._db</code> and return the <code>User</code> object.

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = '[email protected]'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))        

bob@dylan:~$ python3 main.py
successfully created a new user!
could not create a new user: User [email protected] already exists
bob@dylan:~$
```

---

### 6. Basic Flask app <a name='subparagraph6'></a>

In this task, you will set up a basic Flask app.

Create a Flask app that has a single <code>GET</code> route (<code>"/"</code>) and use <code>flask.jsonify</code> to return a JSON payload of the form:

```
{"message": "Bienvenue"}
```

Add the following code at the end of the module:

```
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
```

---

### 7. Register user <a name='subparagraph7'></a>

In this task, you will implement the end-point to register a user. Define a <code>users</code> function that implements the <code>POST /users</code> route.

Import the <code>Auth</code> object and instantiate it at the root of the module as such:

```
from auth import Auth


AUTH = Auth()
```

The end-point should expect two form data fields: <code>"email"</code> and <code>"password"</code>. If the user does not exist, the end-point should register it and respond with the following JSON payload:

```
{"email": "<registered email>", "message": "user created"}
```

If the user is already registered, catch the exception and return a JSON payload of the form

```
{"message": "email already registered"}
```

and return a 400 status code

Remember that you should only use <code>AUTH</code> in this app. <code>DB</code> is a lower abstraction that is proxied by <code>Auth</code>.

<em>Terminal 1:</em>

```
bob@dylan:~$ python3 app.py 
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Terminal 2:

```
bob@dylan:~$ curl -XPOST localhost:5000/users -d '[email protected]' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /users HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> Content-Length: 40
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 40 out of 40 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 52
< Server: Werkzeug/1.0.1 Python/3.7.3
< Date: Wed, 19 Aug 2020 00:03:18 GMT
< 
{"email":"[email protected]","message":"user created"}

bob@dylan:~$
bob@dylan:~$ curl -XPOST localhost:5000/users -d '[email protected]' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /users HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> Content-Length: 40
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 40 out of 40 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 400 BAD REQUEST
< Content-Type: application/json
< Content-Length: 39
< Server: Werkzeug/1.0.1 Python/3.7.3
< Date: Wed, 19 Aug 2020 00:03:33 GMT
< 
{"message":"email already registered"}
bob@dylan:~$
```

---

### 8. Credentials validation <a name='subparagraph8'></a>

In this task, you will implement the <code>Auth.valid_login</code> method. It should expect <code>email</code> and <code>password</code> required arguments and return a boolean.

Try locating the user by email. If it exists, check the password with <code>bcrypt.checkpw</code>. If it matches return <code>True</code>. In any other case, return <code>False</code>.

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = '[email protected]'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.valid_login(email, password))

print(auth.valid_login(email, "WrongPwd"))

print(auth.valid_login("unknown@email", password))

bob@dylan:~$ python3 main.py
True
False
False
bob@dylan:~$
```

---

### 9. Generate UUIDs <a name='subparagraph9'></a>

In this task you will implement a <code>_generate_uuid</code> function in the <code>auth</code> module. The function should return a string representation of a new UUID. Use the <code>uuid</code> module.

Note that the method is private to the <code>auth</code> module and should <strong>NOT</strong> be used outside of it.

---

### 10. Get session ID <a name='subparagraph10'></a>

In this task, you will implement the <code>Auth.create_session</code> method. It takes an <code>email</code> string argument and returns the session ID as a string.

The method should find the user corresponding to the email, generate a new UUID and store it in the database as the user’s <code>session_id</code>, then return the session ID.

Remember that only public methods of <code>self._db</code> can be used.

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = '[email protected]'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.create_session(email))
print(auth.create_session("[email protected]"))

bob@dylan:~$ python3 main.py
5a006849-343e-4a48-ba4e-bbd523fcca58
None
bob@dylan:~$
```

---

### 11. Log in <a name='subparagraph11'></a>

In this task, you will implement a <code>login</code> function to respond to the <code>POST /sessions</code> route.

The request is expected to contain form data with <code>"email"</code> and a <code>"password"</code> fields.

If the login information is incorrect, use <code>flask.abort</code> to respond with a 401 HTTP status.

Otherwise, create a new session for the user, store it the session ID as a cookie with key <code>"session_id"</code> on the response and return a JSON payload of the form

```
{"email": "<user email>", "message": "logged in"}
```

```
bob@dylan:~$ curl -XPOST localhost:5000/users -d '[email protected]' -d 'password=mySuperPwd'
{"email":"[email protected]","message":"user created"}
bob@dylan:~$ 
bob@dylan:~$  curl -XPOST localhost:5000/sessions -d '[email protected]' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /sessions HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> Content-Length: 37
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 37 out of 37 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 46
< Set-Cookie: session_id=163fe508-19a2-48ed-a7c8-d9c6e56fabd1; Path=/
< Server: Werkzeug/1.0.1 Python/3.7.3
< Date: Wed, 19 Aug 2020 00:12:34 GMT
< 
{"email":"[email protected]","message":"logged in"}
* Closing connection 0
bob@dylan:~$ 
bob@dylan:~$ curl -XPOST localhost:5000/sessions -d '[email protected]' -d 'password=BlaBla' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /sessions HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> Content-Length: 34
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 34 out of 34 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 401 UNAUTHORIZED
< Content-Type: text/html; charset=utf-8
< Content-Length: 338
< Server: Werkzeug/1.0.1 Python/3.7.3
< Date: Wed, 19 Aug 2020 00:12:45 GMT
< 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>401 Unauthorized</title>
<h1>Unauthorized</h1>
<p>The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required.</p>
* Closing connection 0
bob@dylan:~$
```

---

### 12. Find user by session ID <a name='subparagraph12'></a>

In this task, you will implement the <code>Auth.get_user_from_session_id</code> method. It takes a single <code>session_id</code> string argument and returns the corresponding <code>User</code> or <code>None</code>.

If the session ID is <code>None</code> or no user is found, return <code>None</code>. Otherwise return the corresponding user.

Remember to only use public methods of <code>self._db</code>.

---

### 13. Destroy session <a name='subparagraph13'></a>

In this task, you will implement <code>Auth.destroy_session</code>. The method takes a single <code>user_id</code> integer argument and returns <code>None</code>.

The method updates the corresponding user’s session ID to <code>None</code>.

Remember to only use public methods of <code>self._db</code>.

---

### 14. Log out <a name='subparagraph14'></a>

In this task, you will implement a <code>logout</code> function to respond to the <code>DELETE /sessions</code> route.

The request is expected to contain the session ID as a cookie with key <code>"session_id"</code>.

Find the user with the requested session ID. If the user exists destroy the session and redirect the user to <code>GET /</code>. If the user does not exist, respond with a 403 HTTP status.

---

### 15. User profile <a name='subparagraph15'></a>

In this task, you will implement a <code>profile</code> function to respond to the <code>GET /profile</code> route.

The request is expected to contain a <code>session_id</code> cookie. Use it to find the user. If the user exist, respond with a 200 HTTP status and the following JSON payload:

```
{"email": "<user email>"}
```

If the session ID is invalid or the user does not exist, respond with a 403 HTTP status.

```
bob@dylan:~$ curl -XPOST localhost:5000/sessions -d '[email protected]' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /sessions HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> Content-Length: 37
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 37 out of 37 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 46
< Set-Cookie: session_id=75c89af8-1729-44d9-a592-41b5e59de9a1; Path=/
< Server: Werkzeug/1.0.1 Python/3.7.3
< Date: Wed, 19 Aug 2020 00:15:57 GMT
< 
{"email":"[email protected]","message":"logged in"}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl -XGET localhost:5000/profile -b "session_id=75c89af8-1729-44d9-a592-41b5e59de9a1"
{"email": "[email protected]"}
bob@dylan:~$ 
bob@dylan:~$ curl -XGET localhost:5000/profile -b "session_id=nope" -v
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET /profile HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> Cookie: session_id=75c89af8-1729-44d9-a592-41b5e59de9a
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 403 FORBIDDEN
< Content-Type: text/html; charset=utf-8
< Content-Length: 234
< Server: Werkzeug/1.0.1 Python/3.7.3
< Date: Wed, 19 Aug 2020 00:16:43 GMT
< 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>403 Forbidden</title>
<h1>Forbidden</h1>
<p>You don't have the permission to access the requested resource. It is either read-protected or not readable by the server.</p>
* Closing connection 0

bob@dylan:~$
```

---

### 16. Generate reset password token <a name='subparagraph16'></a>

In this task, you will implement the <code>Auth.get_reset_password_token</code> method. It take an <code>email</code> string argument and returns a string.

Find the user corresponding to the email. If the user does not exist, raise a <code>ValueError</code> exception. If it exists, generate a UUID and update the user’s <code>reset_token</code> database field. Return the token.

---

### 17. Get reset password token <a name='subparagraph17'></a>

In this task, you will implement a <code>get_reset_password_token</code> function to respond to the <code>POST /reset_password</code> route.

The request is expected to contain form data with the <code>"email"</code> field.

If the email is not registered, respond with a 403 status code. Otherwise, generate a token and respond with a 200 HTTP status and the following JSON payload:

```
{"email": "<user email>", "reset_token": "<reset token>"}
```

---

### 18. Update password <a name='subparagraph18'></a>

In this task, you will implement the <code>Auth.update_password</code> method. It takes <code>reset_token</code> string argument and a <code>password</code> string argument and returns <code>None</code>.

Use the <code>reset_token</code> to find the corresponding user. If it does not exist, raise a <code>ValueError</code> exception.

Otherwise, hash the password and update the user’s <code>hashed_password</code> field with the new hashed password and the <code>reset_token</code> field to <code>None</code>.

---

### 19. Update password end-point <a name='subparagraph19'></a>

In this task you will implement the <code>update_password</code> function in the <code>app</code> module to respond to the <code>PUT /reset_password</code> route.

The request is expected to contain form data with fields <code>"email"</code>, <code>"reset_token"</code> and <code>"new_password"</code>.

Update the password. If the token is invalid, catch the exception and respond with a 403 HTTP code.

If the token is valid, respond with a 200 HTTP code and the following JSON payload:

```
{"email": "<user email>", "message": "Password updated"}
```

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
