---
title: UI Programming
nav_order: 40
has_children: true
---

# {{ page.title }}

## streamlit 
Website: [https://streamlit.io/](https://streamlit.io/)

Blog posts:
- [Turn Python Scripts into Beautiful ML Tools](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace) - by the inventor of streamlit
- [Will streamlit kill off flask?](https://medium.com/swlh/part-1-will-streamlit-kill-off-flask-5ecd75f879c8)
- [Quickly Build and Deploy a Dashboard with Streamlit](https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83)
- [Streamlit 101: An in-depth introduction](https://towardsdatascience.com/streamlit-101-an-in-depth-introduction-fc8aad9492f2)
- [A beginners guide to streamlit: convert Python code into an app](https://analyticsindiamag.com/a-beginners-guide-to-streamlit-convert-python-code-into-an-app/)
- [Turn your data science scripts into websites with Streamlit](https://gilberttanner.com/blog/turn-your-data-science-script-into-websites-with-streamlit)

## PySimpleGUI

Simplifies creating UIs in tkinter, Qt or wxPython on the desktop or via Remi in a browser. Fundamentally single-user mode, it won't serve web pages to a broad community.

Docs: [https://pysimplegui.readthedocs.io/en/latest/](https://pysimplegui.readthedocs.io/en/latest/)
GitHub: [desktop](https://github.com/PySimpleGUI/PySimpleGUI), [browser](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb)

Blog posts:
- [Building a Python UI for Comparing Data](https://towardsdatascience.com/building-a-python-ui-for-comparing-data-13c10693d9e4)

## Qt

Big and complex. It can do pretty much anything, but maybe not easily. In C++ with (confusingly) two competing Python wrappers, one of which has two very different names.

The open-source version works well across Windows/Linux/Mac, with identical source code. The commercial version also supports phones, cars, TVs fridges, toasters, and things I don't even recognize the name of. Probably also space satellites, though I can't be sure.

A full download is probably not necessary but I did it anyway. Be careful, it ends up as many GB on disk.

Main web page: [qt.io/](https://www.qt.io/), but most of us want [open source](https://www.qt.io/download-open-source)

The same company now supplies Python bindings, called [Qt for Python](https://doc.qt.io/qtforpython/) in the docs but PySide2 in pip and in your import statement. 

There is also the (somewhat older?) PyQt from Riverbank Computing. Get it with `pip install PyQt5` and use it with statements similar to `from PyQt5.QtCore import QObject`.

