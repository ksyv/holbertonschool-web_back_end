<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>


## Table of Contents :

  - [0. Parameterize a unit test](#subparagraph0)
  - [1. Parameterize a unit test](#subparagraph1)
  - [2. Mock HTTP calls](#subparagraph2)
  - [3. Parameterize and patch](#subparagraph3)
  - [4. Parameterize and patch as decorators](#subparagraph4)
  - [5. Mocking a property](#subparagraph5)
  - [6. More patching](#subparagraph6)
  - [7. Parameterize](#subparagraph7)
  - [8. Integration test: fixtures](#subparagraph8)

## Resources
### Read or watch:
* [unittest — Unit testing framework](https://docs.python.org/fr/3.13/library/unittest.html#test-discovery)
* [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
* [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
* [parameterized](https://pypi.org/project/parameterized/)
* [Memoization](https://fr.wikipedia.org/wiki/M%C3%A9mo%C3%AFsation)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* The difference between unit and integration tests.
* Common testing patterns such as mocking, parametrizations and fixtures

## Requirements
### General
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS usingpython3(version 3.9)
* All your files should end with a new line
* The first line of all your files should be exactly#!/usr/bin/env python3
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use thepycodestylestyle (version 2.5)
* All your files must be executable
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'andpython3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

## Task
### 0. Parameterize a unit test <a name='subparagraph0'></a>

Familiarize yourself with the <code>utils.access_nested_map</code> function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for <code>utils.access_nested_map</code>.

Create a <code>TestAccessNestedMap</code> class that inherits from <code>unittest.TestCase</code>.

Implement the <code>TestAccessNestedMap.test_access_nested_map</code> method to test that the method returns what it is supposed to.

Decorate the method with <code>@parameterized.expand</code> to test the function for following inputs:

```
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
```

For each of these inputs, test with <code>assertEqual</code> that the function returns the expected result.

The body of the test method should not be longer than 2 lines.

---

### 1. Parameterize a unit test <a name='subparagraph1'></a>

Implement <code>TestAccessNestedMap.test_access_nested_map_exception</code>. Use the <code>assertRaises</code> context manager to test that a <code>KeyError</code> is raised for the following inputs (use <code>@parameterized.expand</code>):

```
nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
```

Also make sure that the exception message is as expected.

---

### 2. Mock HTTP calls <a name='subparagraph2'></a>

Familiarize yourself with the <code>utils.get_json</code> function.

Define the <code>TestGetJson(unittest.TestCase)</code> class and implement the <code>TestGetJson.test_get_json</code> method to test that <code>utils.get_json</code> returns the expected result.

We don’t want to make any actual external HTTP calls. Use <code>unittest.mock.patch</code> to patch <code>requests.get</code>. Make sure it returns a <code>Mock</code> object with a <code>json</code> method that returns <code>test_payload</code> which you parametrize alongside the <code>test_url</code> that you will pass to <code>get_json</code> with the following inputs:

```
test_url="http://example.com", test_payload={"payload": True}
test_url="http://holberton.io", test_payload={"payload": False}
```

Test that the mocked <code>get</code> method was called exactly once (per input) with <code>test_url</code> as argument.

Test that the output of <code>get_json</code> is equal to <code>test_payload</code>.

---

### 3. Parameterize and patch <a name='subparagraph3'></a>

Read about memoization and familiarize yourself with the <code>utils.memoize</code> decorator.

Implement the <code>TestMemoize(unittest.TestCase)</code> class with a <code>test_memoize</code> method.

Inside <code>test_memoize</code>, define following class

```
class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()
```

Use <code>unittest.mock.patch</code> to mock <code>a_method</code>. Test that when calling <code>a_property</code> twice, the correct result is returned but <code>a_method</code> is only called once using <code>assert_called_once</code>.

---

### 4. Parameterize and patch as decorators <a name='subparagraph4'></a>

Familiarize yourself with the <code>client.GithubOrgClient</code> class.

In a new <code>test_client.py</code> file, declare the <code>TestGithubOrgClient(unittest.TestCase)</code> class and implement the <code>test_org</code> method.

This method should test that <code>GithubOrgClient.org</code> returns the correct value.

Use <code>@patch</code> as a decorator to make sure <code>get_json</code> is called once with the expected argument but make sure it is not executed.

Use <code>@parameterized.expand</code> as a decorator to parametrize the test with a couple of <code>org</code> examples to pass to <code>GithubOrgClient</code>, in this order:

* <code>google</code>
* <code>abc</code>

Of course, no external HTTP calls should be made.

---

### 5. Mocking a property <a name='subparagraph5'></a>

<code>memoize</code> turns methods into properties. Read up on how to mock a property (see resource).

Implement the <code>test_public_repos_url</code> method to unit-test <code>GithubOrgClient._public_repos_url</code>.

Use <code>patch</code> as a context manager to patch <code>GithubOrgClient.org</code> and make it return a known payload.

Test that the result of <code>_public_repos_url</code> is the expected one based on the mocked payload.

---

### 6. More patching <a name='subparagraph6'></a>

Implement <code>TestGithubOrgClient.test_public_repos</code> to unit-test <code>GithubOrgClient.public_repos</code>.

Use <code>@patch</code> as a decorator to mock <code>get_json</code> and make it return a payload of your choice.

Use <code>patch</code> as a context manager to mock <code>GithubOrgClient._public_repos_url</code> and return a value of your choice.

Test that the list of repos is what you expect from the chosen payload.

Test that the mocked property and the mocked <code>get_json</code> was called once.

---

### 7. Parameterize <a name='subparagraph7'></a>

Implement <code>TestGithubOrgClient.test_has_license</code> to unit-test <code>GithubOrgClient.has_license</code>.

Parametrize the test with the following inputs

```
repo={"license": {"key": "my_license"}}, license_key="my_license"
repo={"license": {"key": "other_license"}}, license_key="my_license"
```

You should also parameterize the expected returned value.

---

### 8. Integration test: fixtures <a name='subparagraph8'></a>

We want to test the <code>GithubOrgClient.public_repos</code> method in an integration test. That means that we will only mock code that sends external requests.

Create the <code>TestIntegrationGithubOrgClient(unittest.TestCase)</code> class and implement the <code>setUpClass</code> and <code>tearDownClass</code> which are part of the <code>unittest.TestCase</code> API.

Use <code>@parameterized_class</code> to decorate the class and parameterize it with fixtures found in <code>fixtures.py</code>. The file contains the following fixtures:

```
org_payload, repos_payload, expected_repos, apache2_repos
```

The <code>setupClass</code> should mock <code>requests.get</code> to return example payloads found in the fixtures.

Use <code>patch</code> to start a patcher named <code>get_patcher</code>, and use <code>side_effect</code> to make sure the mock of <code>requests.get(url).json()</code> returns the correct fixtures for the various values of <code>url</code> that you anticipate to receive.

Implement the <code>tearDownClass</code> class method to stop the patcher.

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
