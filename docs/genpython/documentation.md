---
title: Python Documentation
parent: General Python
nav_order: 6
---

# {{ page.title }}

There are various options, summarized at the [documentation tools](https://wiki.python.org/moin/DocumentationTools) page. Only a subset will be mentioned below. See also a [comparison of Python documentation generators](https://medium.com/@peterkong/comparison-of-python-documentation-generators-660203ca3804) for some opinions.

In practice, Pythonistas mostly seems to use Sphinx, the wider software community (especially C++) favors Doxygen.

## Sphinx

Used for Python's own documentation, plus most of the important packages. Closely tied to Read the Docs, so output from Sphinx is very familiar to every Python programmer.

Links: [docs](https://www.sphinx-doc.org/en/master/index.html), [GitHub](https://github.com/sphinx-doc/sphinx), [Read the Docs](https://docs.readthedocs.io/en/stable/index.html)

Takes input mainly from reStructuredText (reST) files, and (via autodoc) from docstrings in the code. Output is to HTML, LaTex, PDF, etc. There are converters for a variety of other input formats.

A criticism of Sphinx is that setup is relatively complicated, using Makefiles.

## Doxygen

Supports many languages, especially C++ but also Python.

Links: [docs](http://www.doxygen.nl/), [GitHub](https://github.com/doxygen/doxygen)

Often criticised for producing ugly output.

## pdoc/pdoc3

The original is pdoc (still available), while pdoc3 is a fork of it that dropped Python 2 support and is more actively developed. Lighter and simpler than Sphinx so aimed at smaller projects.

Links: [docs](https://pdoc3.github.io/pdoc/doc/pdoc/) [GitHub](https://github.com/pdoc3/pdoc)

## pydoctor

From the Twisted project. Got good reviews for its capabilities and ease of use. The problem is that in 2020 it still doesn't support Python 3, when Python 2 is already officially dead.
