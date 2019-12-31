---
title: Python Virtual Environments
parent: General Python
nav_order: 2
---

# {{ page.title }}

Python dependencies can get complicated quickly. They can also tangle together and trample on each other. Developer best practice is to start each new project in its own virtual environment. To prevent things becoming too simple there are several, usually with quite similar names. Check out [one 2019 comparison](https://towardsdatascience.com/comparing-python-virtual-environment-tools-9a6543643a44). This is a confusing topic that doesn't seem close to consensus.

The one thing all experienced developers agree on ***don't mess with your system Python***. For Linux/Mac users that can mean you suddenly have no working OS and need to reinstall on a clean disk partition.

## virtualenv and virtualenv-wrapper
Familiar to Python 2 programmers (current and former) but largely obsolete since Python 3.3. I used it back in the day, but found it confusing (especially file locations).

## venv
Built into all recent versions of Python and supported by the Python core team. 

Create a new environment with `python3 -m venv /path/to/new/virtual/environment`

Website: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)

## pyenv and pyenv-virtualenv
**pyenv** is a Python version manager (ported from Ruby's rbenv). Ignore the confusingly-named *pyvenv*, which is now deprecated.

**pyenv-virtualenv** is a pyenv plugin to support virtualenvs: originally using virtualenv but now it defaults to venv if available. Not essential, but many developers find it makes life easier.

Websites:
- [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)
- [https://github.com/pyenv/pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

Blog posts:
- [Managing virtual environments with pyenv](https://towardsdatascience.com/managing-virtual-environment-with-pyenv-ae6f3fb835f8)
- [pyenv Tutorial](https://amaral.northwestern.edu/resources/guides/pyenv-tutorial)
- [Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/)
- [How to manage multiple Python versions and virtual environments](https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/)

## Pipenv
Sort of a higher-level replacement for pip. Opinion in the Python developer community seems divided ([sometimes fiercely](https://chriswarrick.com/blog/2018/07/17/pipenv-promises-a-lot-delivers-very-little/)) on pipenv vs venv/pyenv. Bundled with and [supported by](https://www.activestate.com/blog/why-pipenv-venv/) ActiveState Python.

Blog posts:
- [Python virtual environments](https://medium.com/@sjones_47524/python-virtual-environments-7de63c405d9f)
- [Why you should use pyenv + Pipenv for your Python projects](https://medium.com/hackernoon/reaching-python-development-nirvana-bb5692adf30c)

## conda
Most familiar to scientists. Windows users really need this to manage the NumPy/SciPy ecosystem, which can otherwise be a nightmare. Linux/Mac users may have more choices.

conda is two things in one: a package installer (sort of like pip but separate) and a virtual environment manager (sort of like venv but separate).

conda is great most of the time but can be a bit brittle: when it goes wrong without warning it can be a nightmare to fix. Said with feeling - I've been there. Some developers suggest Anaconda/Miniconda should only be installed *within* virtual environments and never at a system level, turning the `conda env` idea on its head..

## Conclusions
Well, it's complicated...

One very detailed view: [A guide to Python virtual environments](https://medium.com/swlh/a-guide-to-python-virtual-environments-8af34aa106ac). Long, opinionated, well worth reading

I largely followed a cheatsheet from the same author and made a [Linux version]({% link ./pyenv_cheat_sheet_linux.md %})
