---
title: Astronomy-related packages in Python
nav_order: 1
parent: Astronomy-related packages
---

# {{ page.title }}

## AstroPy

This project, by benign design, is gradually swallowing everything else. This can be direct incorporation if the package is mature and compatible enough, or as [affiliated or coordinated](https://www.astropy.org/affiliated/index.html) packages with a looser relationship.

AstroPy in turn is a [NumFOCUS sponsored project](https://numfocus.org/sponsored-projects) within that wider ecosystem of open-source scientific programming.  Check it out, and please donate some cash if you can afford it -- we all benefit.

- Website: [astropy.org/](https://www.astropy.org/)
- GitHub: [github.com/astropy/astropy](https://github.com/astropy/astropy)
- Tutorials in Jupyter Notebook format (excellent!): [learn.astropy.org/](http://learn.astropy.org/) and [github.com/astropy/astropy-tutorials](https://github.com/astropy/astropy-tutorials)

## Astroquery

Astroquery is a set of tools for querying astronomical web forms and databases (to quote the website). Broad-ranging and versatile, which inevitably makes it a bit confusing for novices like me, but very valuable.

- Docs: [astroquery.readthedocs.io/en/latest/](https://astroquery.readthedocs.io/en/latest/)
- GitHub: [github.com/astropy/astroquery](https://github.com/astropy/astroquery)

## AstroML

Machine learning and data mining for astronomy. 

- Website: [astroml.org/](https://www.astroml.org/)
- GitHub: [https://github.com/astroML/astroML](https://github.com/astroML/astroML)
- Book to accompany the project: [Statistics, Data Mining, and Machine Learning in Astronomy](https://smile.amazon.com/Statistics-Mining-Machine-Learning-Astronomy/dp/0691198306). I have the first edition (2014), which is excellent. An updated edition was released late 2019.

## Astroplan

A toolbox for observation planning.

- Docs: [astroplan.readthedocs.io/en/latest/index.html](https://astroplan.readthedocs.io/en/latest/index.html)
- GitHub: [github.com/astropy/astroplan](https://github.com/astropy/astroplan)

## Astral

A relatively small Python module to calculate things like sunrise/sunset and moon phases. This can be done in Astroplan but Astral may be easier if that's all you need.

- Docs: [astral.readthedocs.io/en/stable/index.html](https://astral.readthedocs.io/en/stable/index.html)
- GitHub: [github.com/sffjunkie/astral](https://github.com/sffjunkie/astral)

## pywwt

A python wrapper for the Worldwide Telescope. It runs in Jupyter notebooks or in a Qt window. 

- Docs: [https://pywwt.readthedocs.io/en/stable/annotations.html](https://pywwt.readthedocs.io/en/stable/annotations.html)
- GitHub: [github.com/WorldWideTelescope/pywwt](https://github.com/WorldWideTelescope/pywwt)

I haven't yet got it working in streamlit. 

## Rebound

Primarily an efficient N-body simulator, but it also does animated displays in Jupyter that are otherwise quite difficult. It has APIs for both C and Python. I like this package!

Links: [docs](https://rebound.readthedocs.io/en/latest/), [GitHub](http://github.com/hannorein/rebound). There are lots of non-trivial examples.