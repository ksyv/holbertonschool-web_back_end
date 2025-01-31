Vous avez raison !  J'ai accidentellement supprimé les balises de code markdown à partir de la tâche 2.  Voici la version corrigée, entièrement en markdown, prête pour le copier-coller:

Markdown

 <div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div> 

 # Personal Data 

 ## Table of Contents : 

 - [Resources](#Resources) 
 - [Learning Objectives](#Learning-Objectives) 
 - [Requirements](#Requirements) 
 - [Tasks](#Tasks) 
     - [0. Regex-ing](#subparagraph1) 
     - [1. Log formatter](#subparagraph2) 
     - [2. Create logger](#subparagraph3) 
     - [3. Connect to secure database](#subparagraph4) 
     - [4. Read and filter data](#subparagraph5) 
     - [5. Encrypting passwords](#subparagraph6) 
     - [6. Check valid password](#subparagraph7)
 - [Authors](#Authors) 

 ## Resources 
 ### Read or watch: 
 * [What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-non-pii-and-personal-data/) 
 * [logging documentation](https://docs.python.org/3/library/logging.html) 
 * [bcrypt package](https://pypi.org/project/bcrypt/) 
 * [Logging to Files, Setting Levels, and Formatting](https://docs.python.org/3/howto/logging.html#logging-to-a-file)
 * [Uncovering Password Habits](https://www.netiq.com/communities/cool-solutions/uncovering-password-habits/)

 ## Learning Objectives 
 At the end of this project, you are expected to be able to explain to anyone, without the help of Google: 
 * Examples of Personally Identifiable Information (PII) 
 * How to implement a log filter that will obfuscate PII fields 
 * How to encrypt a password and check the validity of an input password 
 * How to authenticate to a database using environment variables 

 ## Requirements 
 ### Python Scripts 
 * All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9) 
 * All your files should end with a new line 
 * The first line of all your files should be exactly #!/usr/bin/env python3 
 * A README.md file, at the root of the folder of the project, is mandatory 
 * Your code should use the pycodestyle style (version 2.5) 
 * All your files must be executable 
 * The length of your files will be tested using wc 
 * All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)') 
 * All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)') 
 * All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)') 
 * A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified) 
 * All your functions should be type annotated 

 ## Tasks 
 ### 0. Regex-ing <a name="subparagraph1"></a> 

 Write a function called `filter_datum` that returns the log message obfuscated: 

 * Arguments:
    * `fields`: a list of strings representing all fields to obfuscate 
    * `redaction`: a string representing by what the field will be obfuscated 
    * `message`: a string representing the log line 
    * `separator`: a string representing by which character is separating all fields in the log line (message) 
 * The function should use a regex to replace occurrences of certain field values. 
 * `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex. 

 ### 1. Log formatter <a name="subparagraph2"></a> 

 Update the class `RedactingFormatter` to accept a list of strings `fields` in the constructor argument. 
 Implement the `format` method to filter values in incoming log records using `filter_datum`. Values for fields in `fields` should be filtered.
 DO NOT extrapolate `FORMAT` manually. The `format` method should be less than 5 lines long. 

 ```python
 class RedactingFormatter(logging.Formatter): 
     """ Redacting Formatter class 
         """ 

     REDACTION = "***" 
     FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s" 
     SEPARATOR = ";" 

     def __init__(self, fields: list):
         super(RedactingFormatter, self).__init__(self.FORMAT)
         self.fields = fields

     def format(self, record: logging.LogRecord) -> str: 
         NotImplementedError 
```

### 2. Create logger <a name="subparagraph3"></a>
Implement a get_logger function that takes no arguments and returns a logging.Logger object.

The logger should be named "user_data" and only log up to logging.INFO level. It should not propagate messages to other loggers. It should have a StreamHandler with RedactingFormatter as formatter.
Create a tuple PII_FIELDS constant at the root of the module containing the 5 fields from user_data.csv that are considered PII : name, email, phone, ssn, password. Use it to parameterize the formatter.


### 3. Connect to secure database <a name="subparagraph4"></a>
Implement a get_db function that returns a connector to the database (mysql.connector.connection.MySQLConnection object).

Use the os module to obtain credentials from the environment:
PERSONAL_DATA_DB_USERNAME (default: "root")
PERSONAL_DATA_DB_PASSWORD (default: "")
PERSONAL_DATA_DB_HOST (default: "localhost")
The database name is stored in PERSONAL_DATA_DB_NAME.
Use the module mysql-connector-python to connect to the MySQL database.

### 4. Read and filter data <a name="subparagraph5"></a>
Implement a main function that takes no arguments and returns nothing.

The function will obtain a database connection using get_db and retrieve all rows in the users table and display each row under a filtered format:

[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);

Filtered fields:

name
email
phone
ssn
password
Only 1  your main function should run when the module is executed.   
1.
github.com
github.com

### 5. Encrypting passwords <a name="subparagraph6"></a>
Implement a hash_password function that expects one string argument name password and returns a salted, hashed password, which is a byte string.
Use the bcrypt package to perform the hashing (with hashpw).

### 6. Check valid password <a name="subparagraph7"></a>
Implement an is_valid function that expects 2 arguments and returns a boolean.
Arguments:

hashed_password: bytes type
password: string type Use bcrypt to validate that the provided password matches the hashed password.
Authors
Kevin Y. ksyv