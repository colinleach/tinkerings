---
title: Python Testing
parent: General Python
nav_order: 4
---

# {{ page.title }}

At the lowest level, checking that code runs correctly can involve simply adding some `assert()` statements. There are more structured approaches.

## unittest and doctest

A standard part of recent Python versions. Closely based on Java's JUnit, so somewhat verbose in the Java tradition.

## pytest (or py.test)

More concise and pythonic than unittest, this is a separate package that needs to be installed. Very popular.

Links: [docs](https://docs.pytest.org/en/latest/), [GitHub](https://github.com/pytest-dev/pytest)

Books:
- [Python Testing with pytest](https://smile.amazon.com/gp/product/1680502409). Thorough.
- [Serious Python](https://smile.amazon.com/gp/product/1593278780), chapter 6. Not primarily about pytest, this excellent book covers pytest among many other topics.

Blogs:
- [Hypermodern Python 2: Testing](https://medium.com/@cjolowicz/hypermodern-python-2-testing-ae907a920260)
- 

## nose

Sort of an enhanced unittest, it appears to be falling in popularity as pytest becomes the standard.

## tox, nox, etc

Intended to automate and standardize testing in Python, these are virtualenv managers that can run test suites across a variety of environments.

Tox: [docs](https://tox.readthedocs.io/en/latest/)

Dox: [docs](https://nox.thea.codes/en/stable/)

## See also

Testing feeds into continuous integration (CI), which has a separate page.