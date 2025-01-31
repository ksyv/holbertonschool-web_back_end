<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Personal data

## Table of Contents:

- [Resources](#Resources)
- [Learning Objectives](#Learning-Objectives)
- [Requirements](#Requirements)
- [Task](#Task)
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
* What Is PII, non-PII, and Personal Data?
* logging documentation
* bcrypt package
* Logging to Files, Setting Levels, and Formatting

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

## Task

### 0. Regex-ing <a name="subparagraph1"></a>
Write a function called `filter_datum` that returns the log message obfuscated:

Arguments:
* fields: a list of strings representing all fields to obfuscate
* redaction: a string representing by what the field will be obfuscated
* message: a string representing the log line
* separator: a string representing by which character is separating all fields in the log line (message)

The function should use a regex to replace occurrences of certain field values.
`filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex.

```bash
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

bob@dylan:~$
bob@dylan:~<span class="math-inline">\./main\.py
name\=egg;email\=eggmin@eggsample\.com;password\=xxx;date\_of\_birth\=xxx;
name\=bob;email\=bob@dylan\.com;password\=xxx;date\_of\_birth\=xxx;
bob@dylan\:\~</span>