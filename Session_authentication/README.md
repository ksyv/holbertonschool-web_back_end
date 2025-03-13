# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Background Context

## Table of Contents :

  - [0. Et moi et moi et moi!](#subparagraph0)
  - [1. Empty session](#subparagraph1)
  - [2. Create a session](#subparagraph2)
  - [3. User ID for Session ID](#subparagraph3)
  - [4. Session cookie](#subparagraph4)
  - [5. Before request](#subparagraph5)
  - [6. Use Session ID for identifying a User](#subparagraph6)
  - [7. New view for Session Authentication](#subparagraph7)
  - [8. Logout](#subparagraph8)

## Resources
### Read or watch:
* [REST API Authentication Mechanisms - Only the session auth part](/rltoken/vyJGpJSSrFRe0LuWasDqCQ)
* [HTTP Cookie](/rltoken/Ry_Fo8MjzSa1KZ2nIijqOA)
* [Flask](/rltoken/02kzIo8IrujZmw79-nG6qw)
* [Flask Cookie](/rltoken/IoM4N_HLGdV1XBrFleMYGA)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* What authentication means
* What session authentication means
* What Cookies are
* How to send Cookies
* How to parse Cookies

## Requirements
### General
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS usingpython3(version 3.9)
* All your files should end with a new line
* The first line of all your files should be exactly#!/usr/bin/env python3
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use thepycodestylestyle (version 2.5)
* All your files must be executable
* The length of your files will be tested usingwc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'andpython3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Task
### 0. Et moi et moi et moi! <a name='subparagraph0'></a>

Copy all your work of the <a href="/rltoken/QpkU4JYjID3B9CWltyMjKQ" target="_blank" title="0x06. Basic authentication">0x06. Basic authentication</a> project in this new folder.

In this version, you implemented a <strong>Basic authentication</strong> for giving you access to all User endpoints:

* <code>GET /api/v1/users</code>
* <code>POST /api/v1/users</code>
* <code>GET /api/v1/users/&lt;user_id&gt;</code>
* <code>PUT /api/v1/users/&lt;user_id&gt;</code>
* <code>DELETE /api/v1/users/&lt;user_id&gt;</code>

Now, you will add a new endpoint:  to retrieve the authenticated  object.

* Copy folders <code>models</code> and <code>api</code> from the previous project <code>0x06. Basic authentication</code>
* Please make sure all mandatory tasks of this previous project are done at 100% because this project (and the rest of this track) will be based on it.
* Update <code>@app.before_request</code> in <code>api/v1/app.py</code>:


  * Assign the result of <code>auth.current_user(request)</code> to <code>request.current_user</code>
* Update method for the route <code>GET /api/v1/users/&lt;user_id&gt;</code> in <code>api/v1/views/users.py</code>:


  * If <code>&lt;user_id&gt;</code> is equal to <code>me</code> and <code>request.current_user</code> is <code>None</code>: <code>abort(404)</code>
  * If <code>&lt;user_id&gt;</code> is equal to <code>me</code> and <code>request.current_user</code> is not <code>None</code>: return the authenticated <code>User</code> in a JSON response (like a normal case of <code>GET /api/v1/users/&lt;user_id&gt;</code> where <code>&lt;user_id&gt;</code> is a valid <code>User</code> ID)
  * Otherwise, keep the same behavior

In the first terminal:

`html
bob@dylan:~$ cat main_0.py
#!/usr/bin/env python3
""" Main 0
"""
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = "[email protected]"
user_clear_pwd = "H0lbertonSchool98!"

user = User()
user.email = user_email
user.password = user_clear_pwd
print("New user: {}".format(user.id))
user.save()

basic_clear = "{}:{}".format(user_email, user_clear_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py 
New user: 9375973a-68c7-46aa-b135-29f79e837495
Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
`

In a second terminal:

`html
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
[
  {
    "created_at": "2017-09-25 01:55:17", 
    "email": "[email protected]", 
    "first_name": null, 
    "id": "9375973a-68c7-46aa-b135-29f79e837495", 
    "last_name": null, 
    "updated_at": "2017-09-25 01:55:17"
  }
]
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "created_at": "2017-09-25 01:55:17", 
  "email": "[email protected]", 
  "first_name": null, 
  "id": "9375973a-68c7-46aa-b135-29f79e837495", 
  "last_name": null, 
  "updated_at": "2017-09-25 01:55:17"
}
bob@dylan:~$
`

---

### 1. Empty session <a name='subparagraph1'></a>

Create a class  that inherits from . For the moment this class will be empty. It’s the first step for creating a new authentication mechanism:

* validate if everything inherits correctly without any overloading
* validate the “switch” by using environment variables

Update  for using  instance for the variable  depending of the value of the environment variable , If  is equal to :

* import <code>SessionAuth</code> from <code>api.v1.auth.session_auth</code>
* create an instance of <code>SessionAuth</code> and assign it to the variable <code>auth</code>

Otherwise, keep the previous mechanism.

In the first terminal:

`html
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
`

In a second terminal:

`html
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status/"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{
  "error": "Forbidden"
}
bob@dylan:~$
`

---

### 2. Create a session <a name='subparagraph2'></a>

Update  class:

* Create a class attribute <code>user_id_by_session_id</code> initialized by an empty dictionary
* Create an instance method <code>def create_session(self, user_id: str = None) -&gt; str:</code> that creates a Session ID for a <code>user_id</code>:


  * Return <code>None</code> if <code>user_id</code> is <code>None</code>
  * Return <code>None</code> if <code>user_id</code> is not a string
  * Otherwise:


    * Generate a Session ID using <code>uuid</code> module and <code>uuid4()</code> like <code>id</code> in <code>Base</code>
    * Use this Session ID as key of the dictionary <code>user_id_by_session_id</code> - the value for this key must be <code>user_id</code>
    * Return the Session ID
  * The same <code>user_id</code> can have multiple Session ID - indeed, the <code>user_id</code> is the value in the dictionary <code>user_id_by_session_id</code>

Now you an “in-memory” Session ID storing. You will be able to retrieve an  id based on a Session ID.

`html
bob@dylan:~$ cat  main_1.py 
#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

print("{}: {}".format(type(sa.user_id_by_session_id), sa.user_id_by_session_id))

user_id = None
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = 89
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "fghij"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_1.py 
<class 'dict'>: {}
None => None: {}
89 => None: {}
abcde => 61997a1b-3f8a-4b0f-87f6-19d5cafee63f: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde'}
fghij => 69e45c25-ec89-4563-86ab-bc192dcc3b4f: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde', '69e45c25-ec89-4563-86ab-bc192dcc3b4f': 'fghij'}
abcde => 02079cb4-6847-48aa-924e-0514d82a43f4: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde', '02079cb4-6847-48aa-924e-0514d82a43f4': 'abcde', '69e45c25-ec89-4563-86ab-bc192dcc3b4f': 'fghij'}
bob@dylan:~$
`

---

### 3. User ID for Session ID <a name='subparagraph3'></a>

Update  class:

Create an instance method  that returns a  ID based on a Session ID:

* Return <code>None</code> if <code>session_id</code> is <code>None</code>
* Return <code>None</code> if <code>session_id</code> is not a string
* Return the value (the User ID) for the key <code>session_id</code> in the dictionary <code>user_id_by_session_id</code>.
* You must use <code>.get()</code> built-in for accessing in a dictionary a value based on key

Now you have 2 methods ( and ) for storing and retrieving a link between a  ID and a Session ID.

`html
bob@dylan:~$ cat main_2.py 
#!/usr/bin/env python3
""" Main 2
"""
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

user_id_1 = "abcde"
session_1 = sa.create_session(user_id_1)
print("{} => {}: {}".format(user_id_1, session_1, sa.user_id_by_session_id))

user_id_2 = "fghij"
session_2 = sa.create_session(user_id_2)
print("{} => {}: {}".format(user_id_2, session_2, sa.user_id_by_session_id))

print("---")

tmp_session_id = None
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = 89
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = "doesntexist"
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

print("---")

tmp_session_id = session_1
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = session_2
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

print("---")

session_1_bis = sa.create_session(user_id_1)
print("{} => {}: {}".format(user_id_1, session_1_bis, sa.user_id_by_session_id))

tmp_user_id = sa.user_id_for_session_id(session_1_bis)
print("{} => {}".format(session_1_bis, tmp_user_id))

tmp_user_id = sa.user_id_for_session_id(session_1)
print("{} => {}".format(session_1, tmp_user_id))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_2.py 
abcde => 8647f981-f503-4638-af23-7bb4a9e4b53f: {'8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
fghij => a159ee3f-214e-4e91-9546-ca3ce873e975: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
---
None => None
89 => None
doesntexist => None
---
8647f981-f503-4638-af23-7bb4a9e4b53f => abcde
a159ee3f-214e-4e91-9546-ca3ce873e975 => fghij
---
abcde => 5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde', '5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee': 'abcde'}
5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee => abcde
8647f981-f503-4638-af23-7bb4a9e4b53f => abcde
bob@dylan:~$
`

---

### 4. Session cookie <a name='subparagraph4'></a>

Update  by adding the method  that returns a cookie value from a request:

* Return <code>None</code> if <code>request</code> is <code>None</code>
* Return the value of the cookie named <code>_my_session_id</code> from <code>request</code> - the name of the cookie must be defined by the environment variable <code>SESSION_NAME</code>
* You must use <code>.get()</code> built-in for accessing the cookie in the request cookies dictionary
* You must use the environment variable <code>SESSION_NAME</code> to define the name of the cookie used for the Session ID

In the first terminal:

`html
bob@dylan:~$ cat main_3.py
#!/usr/bin/env python3
""" Cookie server
"""
from flask import Flask, request
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return "Cookie value: {}\n".format(auth.session_cookie(request))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_3.py 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
`

In a second terminal:

`html
bob@dylan:~$ curl "http://0.0.0.0:5000"
Cookie value: None
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id=Hello"
Cookie value: Hello
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id=C is fun"
Cookie value: C is fun
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id_fake"
Cookie value: None
bob@dylan:~$
`

---

### 5. Before request <a name='subparagraph5'></a>

Update the  method in :

* Add the URL path <code>/api/v1/auth_session/login/</code> in the list of excluded paths of the method <code>require_auth</code> - this route doesn’t exist yet but it should be accessible outside authentication
* If <code>auth.authorization_header(request)</code> and <code>auth.session_cookie(request)</code> return <code>None</code>, <code>abort(401)</code>

In the first terminal:

`html
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
`

In a second terminal:

`html
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" # not found but not "blocked" by an authentication system
{
  "error": "Not found"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh" # Won't work because the environment variable AUTH_TYPE is equal to "session_auth"
{
  "error": "Forbidden"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=5535d4d7-3d77-4d06-8281-495dc3acfe76" # Won't work because no user is linked to this Session ID
{
  "error": "Forbidden"
}
bob@dylan:~$
`

---

### 6. Use Session ID for identifying a User <a name='subparagraph6'></a>

Update  class:

Create an instance method  (overload) that returns a  instance based on a cookie value:

* You must use <code>self.session_cookie(...)</code> and <code>self.user_id_for_session_id(...)</code> to return the User ID based on the cookie <code>_my_session_id</code>
* By using this User ID, you will be able to retrieve a <code>User</code> instance from the database - you can use <code>User.get(...)</code> for retrieving a <code>User</code> from the database.

Now, you will be able to get a User based on his session ID.

In the first terminal:

`html
bob@dylan:~$ cat main_4.py
#!/usr/bin/env python3
""" Main 4
"""
from flask import Flask, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User

""" Create a user test """
user_email = "[email protected]"
user_clear_pwd = "fake pwd"

user = User()
user.email = user_email
user.password = user_clear_pwd
user.save()

""" Create a session ID """
sa = SessionAuth()
session_id = sa.create_session(user.id)
print("User with ID: {} has a Session ID: {}".format(user.id, session_id))

""" Create a Flask app """
app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    request_user = sa.current_user(request)
    if request_user is None:
        return "No user found\n"
    return "User found: {}\n".format(request_user.id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_4.py
User with ID: cf3ddee1-ff24-49e4-a40b-2540333fe992 has a Session ID: 9d1648aa-da79-4692-8236-5f9d7f9e9485
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
`

In a second terminal:

`html
bob@dylan:~$ curl "http://0.0.0.0:5000/"
No user found
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/" --cookie "_my_session_id=Holberton"
No user found
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/" --cookie "_my_session_id=9d1648aa-da79-4692-8236-5f9d7f9e9485"
User found: cf3ddee1-ff24-49e4-a40b-2540333fe992
bob@dylan:~$
`

---

### 7. New view for Session Authentication <a name='subparagraph7'></a>

Create a new Flask view that handles all routes for the Session authentication.

In the file , create a route  (= ):

* Slash tolerant (<code>/auth_session/login</code> == <code>/auth_session/login/</code>)
* You must use <code>request.form.get()</code> to retrieve <code>email</code> and <code>password</code> parameters
* If <code>email</code> is missing or empty, return the JSON <code>{ "error": "email missing" }</code> with the status code <code>400</code>
* If <code>password</code> is missing or empty, return the JSON <code>{ "error": "password missing" }</code> with the status code <code>400</code>
* Retrieve the <code>User</code> instance based on the <code>email</code> - you must use the class method <code>search</code> of <code>User</code> (same as the one used for the <code>BasicAuth</code>)


  * If no <code>User</code> found, return the JSON <code>{ "error": "no user found for this email" }</code> with the status code <code>404</code>
  * If the <code>password</code> is not the one of the <code>User</code> found, return the JSON <code>{ "error": "wrong password" }</code> with the status code <code>401</code> - you must use <code>is_valid_password</code> from the <code>User</code> instance
  * Otherwise, create a Session ID for the <code>User</code> ID:


    * You must use <code>from api.v1.app import auth</code> - <strong>WARNING: please import it only where you need it</strong> - not on top of the file (can generate circular import - and break first tasks of this project)
    * You must use <code>auth.create_session(..)</code> for creating a Session ID
    * Return the dictionary representation of the <code>User</code> - you must use <code>to_json()</code> method from User
    * You must set the cookie to the response - you must use the value of the environment variable <code>SESSION_NAME</code> as cookie name - <a href="/rltoken/FCL4DJLbn05Cd3_G0-8i4g" target="_blank" title="tip">tip</a>

In the file , you must add this new view at the end of the file.

In the first terminal:

`html
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
`

In a second terminal:

`html
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XGET
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
bob@dylan:~$
bob@dylan:~$  curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST
{
  "error": "email missing"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "[email protected]"
{
  "error": "password missing"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "[email protected]" -d "password=test"
{
  "error": "no user found for this email"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "[email protected]" -d "password=test"
{
  "error": "wrong password"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "[email protected]" -d "password=fake pwd"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "[email protected]", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "[email protected]" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/auth_session/login HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> Content-Length: 42
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Set-Cookie: _my_session_id=df05b4e1-d117-444c-a0cc-ba0d167889c4; Path=/
< Access-Control-Allow-Origin: *
< Content-Length: 210
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Mon, 16 Oct 2017 04:57:08 GMT
< 
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "[email protected]", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
* Closing connection 0
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=df05b4e1-d117-444c-a0cc-ba0d167889c4"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "[email protected]", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
`

Now you have an authentication based on a Session ID stored in cookie, perfect for a website (browsers love cookies).

---

### 8. Logout <a name='subparagraph8'></a>

Update the class  by adding a new method  that deletes the user session / logout:

* If the <code>request</code> is equal to <code>None</code>, return <code>False</code>
* If the <code>request</code> doesn’t contain the Session ID cookie, return <code>False</code> - you must use <code>self.session_cookie(request)</code>
* If the Session ID of the request is not linked to any User ID, return <code>False</code> - you must use <code>self.user_id_for_session_id(...)</code>
* Otherwise, delete in <code>self.user_id_by_session_id</code> the Session ID (as key of this dictionary) and return <code>True</code>

Update the file , by adding a new route :

* Slash tolerant
* You must use <code>from api.v1.app import auth</code>
* You must use <code>auth.destroy_session(request)</code> for deleting the Session ID contains in the request as cookie:


  * If <code>destroy_session</code> returns <code>False</code>, <code>abort(404)</code>
  * Otherwise, return an empty JSON dictionary with the status code 200

In the first terminal:

`html
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
`

In a second terminal:

`html
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "[email protected]" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/auth_session/login HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> Content-Length: 42
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Set-Cookie: _my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721; Path=/
< Access-Control-Allow-Origin: *
< Content-Length: 210
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Mon, 16 Oct 2017 04:57:08 GMT
< 
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "[email protected]", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "[email protected]", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721" -XDELETE
{}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
{
  "error": "Forbidden"
}
bob@dylan:~$
`

Login, logout… what’s else?

Now, after getting a Session ID, you can request all protected API routes by using this Session ID, no need anymore to send User email and password every time.

---


## Authors
Ksyv - [Your GitHub Profile](https://github.com/ksyv)
