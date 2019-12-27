---
title: Web Programming
nav_order: 3
---

# {{ page.title }}
Big topic! Some things to think about:
- Static website, or with a database, user authentication, etc?
- Needs client-side programming? (React, Angular, Vue, next year's fad)
- Server-side language? (Ruby, Python, JavaScript, PHP)
- Hosting? How much are you willing to pay?

## Static websites

### Old-school
Push some HTML and CSS to a hosting site and you're done.

### jekyll
Adds some sophisticated templating ([liquid](#)) but is built to a static site before deployment. Written in Ruby, but after getting past some setup with Gemfiles the language is well hidden.

Killer advantage: this is the technology behind GitHub Pages, so hosting is free and easy (this page is an example).

Excellent documentation: [https://jekyllrb.com/](https://jekyllrb.com/)

### Abuse a more complex framework
Flask (see below) isn't really designed for static websites, but it can build them if that's all you want.

## Python frameworks
Saying 'scientists use Python' slightly misses the point. More importantly, we use NumPy, SciPy, SymPy, Matplotlib, pandas, scikit-learn, AstroPy, AstroQuery, AstroML, etc...

With that background, sticking with Python for creating the occasional website is obviously convenient.

### Old-school
Preferably not quite as old as CGI, but for the simplest cases it may be enough to put a WSGI wrapper around some existing code.

### Flask
https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-
development-environment

Flask Book: https://flaskbook.com/

SQLAlchemy: https://www.sqlalchemy.org/

### Django

## Other back-end languages

### Ruby on Rails

