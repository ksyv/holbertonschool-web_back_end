<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>


## Table of Contents :

  - [0. Basic Flask app](#subparagraph0)
  - [1. Basic Babel setup](#subparagraph1)
  - [2. Get locale from request](#subparagraph2)
  - [3. Parametrize templates](#subparagraph3)
  - [4. Force locale with URL parameter](#subparagraph4)
  - [5. Mock logging in](#subparagraph5)
  - [6. Use user locale](#subparagraph6)
  - [7. Infer appropriate time zone](#subparagraph7)

## Resources
### Read or watch:
* [Flask-Babel](https://python-babel.github.io/flask-babel/)
* [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
* [pytz](https://pypi.org/project/pytz/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* Learn how to parametrize Flask templates to display different languages
* Learn how to infer the correct locale based on URL parameters, user settings or request headers
* Learn how to localize timestamps

## Requirements
### General
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
* All your files should end with a new line
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5)
* The first line of all your files should be exactly#!/usr/bin/env python3
* All your*.pyfiles should be executable
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions and methods should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'andpython3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

## Task
### 0. Basic Flask app <a name='subparagraph0'></a>

First you will setup a basic Flask app in <code>0-app.py</code>. Create a single <code>/</code> route and an <code>index.html</code> template that simply outputs “Welcome to Holberton” as page title (<code>&lt;title&gt;</code>) and “Hello world” as header (<code>&lt;h1&gt;</code>).

---

### 1. Basic Babel setup <a name='subparagraph1'></a>

Install the Babel Flask extension:

```
$ pip3 install flask_babel
```

Then instantiate the <code>Babel</code> object in your app. Store it in a module-level variable named <code>babel</code>.

In order to configure available languages in our app, you will create a <code>Config</code> class that has a <code>LANGUAGES</code> class attribute equal to <code>["en", "fr"]</code>.

Use <code>Config</code> to set Babel’s default locale (<code>"en"</code>) and timezone (<code>"UTC"</code>).

Use that class as config for your Flask app.

---

### 2. Get locale from request <a name='subparagraph2'></a>

Create a <code>get_locale</code> function and use <code>request.accept_languages</code> to determine the best match with our supported languages.

Use the <code>babel.init_app()</code> method to initialize Flask-Babel with your application. Pass the<code>locale_selector</code> parameter to specify your custom <code>get_locale</code>  function.

---

### 3. Parametrize templates <a name='subparagraph3'></a>

Use the <code>_</code> or <code>gettext</code> function to parametrize your templates. Use the message IDs <code>home_title</code> and <code>home_header</code>.

Create a <code>babel.cfg</code> file containing

```
[python: **.py]
[jinja2: **/templates/**.html]
```

Then initialize your translations with

```
$ pybabel extract -F babel.cfg -o messages.pot .
```

and your two dictionaries with

```
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```

Then edit files <code>translations/[en|fr]/LC_MESSAGES/messages.po</code> to provide the correct value for each message ID for each language. Use the following translations:

Then compile your dictionaries with

```
$ pybabel compile -d translations
```

Reload the home page of your app and make sure that the correct messages show up.

---

### 4. Force locale with URL parameter <a name='subparagraph4'></a>

In this task, you will implement a way to force a particular locale by passing the <code>locale=fr</code> parameter to your app’s URLs.

In your <code>get_locale</code> function, detect if the incoming request contains <code>locale</code> argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting <code>http://127.0.0.1:5000?locale=[fr|en]</code>.

<strong>Visiting <code>http://127.0.0.1:5000/?locale=fr</code> should display this level 1 heading:</strong>
<img alt="" loading="lazy" src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/f958f4a1529b535027ce.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250325%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20250325T141847Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=af0848b4f8a64eca22a9eadba62b41217f1b46d23608390160c3769c64690a91" style=""/>

---

### 5. Mock logging in <a name='subparagraph5'></a>

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in <code>5-app.py</code>.

```
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```

This will mock a database user table. Logging in will be mocked by passing <code>login_as</code> URL parameter containing the user ID to log in as.

Define a <code>get_user</code>  function that returns a user dictionary or <code>None</code> if the ID cannot be found or if <code>login_as</code> was not passed.

Define a <code>before_request</code> function and use the <code>app.before_request</code> decorator to make it be executed before all other functions. <code>before_request</code> should use <code>get_user</code> to find a user if any, and set it as a global on <code>flask.g.user</code>.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

<strong>Visiting <code>http://127.0.0.1:5000/</code> in your browser should display this:</strong>

<img alt="" loading="lazy" src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/2c5b2c8190f88c6b4668.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250325%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20250325T141847Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=21f981d15bacf073e15087589189694435c51458392958ea65386bf974577a0d" style=""/>

<strong>Visiting <code>http://127.0.0.1:5000/?login_as=2</code> in your browser should display this:</strong>
<img alt="" loading="lazy" src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/277f24308c856a09908c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250325%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20250325T141847Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=dd10a9bd44c578d5bfb73c0a2480215b9b8e5e26b790963d4dbbd042a93908a2" style=""/>

---

### 6. Use user locale <a name='subparagraph6'></a>

Change your <code>get_locale</code> function to use a user’s preferred local if it is supported.

The order of priority should be

Test by logging in as different users

<img alt="" loading="lazy" src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/9941b480b0b9d87dc5de.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250325%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20250325T141847Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=d4cdbfb1eb000f9fe7fd5171b131c890c09120a3d869db9d65e2a97d9ad22793" style=""/>

---

### 7. Infer appropriate time zone <a name='subparagraph7'></a>

Define a <code>get_timezone</code> function and in <code>babel.init_app()</code> Pass the<code>timezone_selector</code> parameter to specify your custom <code>get_timezone</code>  function.

The logic should be the same as <code>get_locale</code>:

Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use <code>pytz.timezone</code> and catch the <code>pytz.exceptions.UnknownTimeZoneError</code> exception.

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
