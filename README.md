## Learning Objectives

1. The students should be able to understand the fundamental principles of CI/CD to automate the software development process.
2. The students should be able to **understand** the integration of CI/CD with Test-Driven Development (TDD) to ensure code quality.
3. The students should be able to **demonstrate proficiency** in setting up CI/CD pipelines using GitHub Actions for automated testing.

### Continuos Integration/ Continuos Development (CI/CD) Fundamentals

CI/CD is a software development work flow particularly used by our DevOps community. The aim is to shorten the development lifecylce and provide continuous delivery of small, high quality changes.



#### CI:

Continuos integration is the process where devs frequently integrate their code into a central repository, and each integration is verified by automated build and test processes that we can set up in GitHub Actions. 

#### CD:

Is the practice of Automaticall deploying code changes to the production environment after they have passed the tests, and is stage where we monitor the changes and make decisions on what to do next.

![CICD](https://www.mabl.com/hubfs/CICDBlog.png)

### Integrating CI/CD with Test Driven Development (TDD)

Test driven development is a software development approach where tests are written before code is written or implemented (essentially defining a prompt for what the code should be able to do).

Integrating CI/CD with TDD means that as soon as a developer writes code and pushes it, it is automatically tested, and if it passes is integrated into the main codebase and can be deployed to production

### Creating Tests for TDD

![TDD](https://cdn.sanity.io/images/hgftikht/production/4f8ab9993567bb23ad72faad88a8af8cc9fd8f00-1000x659.png)

So the idea here is that we're going to be creating a **VERY** basic API that recieves a POST request and returns a response. Before we do this, if we're following the TDD principle of writing test before code than we need to start with a test.

We'll be writing our tests with the unittest library (something you're probably familiar with from whiteboards)

```
pip install Flask requests faker
```

https://docs.python.org/3/library/unittest.html

#### Mocking and Stubbing Tests

When creating tests we can use two was to generate the test data, either **Stubbing** which is to create a predefined payload and associate response, or **Mocking** which creates mock objects to simulate the behavior of the real ones.

After creating our tests let's push to github to simulate creating Actions to automate testing and deployment.

**Make sure to add venv to your .gitignore before pushing**

