# cosmic-python

Follow up the book **Architecture Patterns with Python**.

May refer to [source code repo](https://github.com/cosmicpython/code)

## Chapter 1 - Domain model

In this chapter, you will learn how to create abstracted layers from requirements and design domain models.

About Python, can learn about dataclass, pytest and magic methods.

## Chapter 2 - Repository pattern

In this chapter, you will learn how to abstract and create repository.

The repository layer is between ORM and Application layer and every DB job works through domain objects.

Additionally, can learn about Sqhlalchemy.

## Chapter 3 - Coupling and Abstraction

In this chapter, you will breifly learn about how to make good abstraction and relation between test and abstraction.

There is an example that explain how to achieve a given requirement - a file system.

Additionally, can learn about edge-to-edge test and test codes which use Python unittest.mock has code smell.

Instead, it is recommended to use fakes (fake objects or etc).

How about doing [kata](http://www.peterprovost.org/blog/2012/05/02/kata-the-only-way-to-learn-tdd/)?

## Chapter 4 - API app and Service Layer.

In this chapter, you will learn how to apply API endpoints to build MVP and how to add service layer.

When we apply API endpoints, it looks very **heavy** and do lots of orchestration. Also e2e test code is ugly and long.

_Orchestration_ is jobs fetching stuff out of our repository, validating our input against database state, handling errors, and committing in the happy path.

API endpoints responsibility is doing "web stuff" such as parsing JSON and producing the right HTTP codes for happy or unhappy cases.

> "web stuff" is translated to "standard web function" in Korean.

The service layer takes orchestration from API endpoints.
