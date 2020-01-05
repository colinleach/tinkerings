---
title: Plotting Packages
nav_order: 2
parent: Data Visualization
---

# {{ page.title }}

There are lots of options in Python, which can be an advantage or just confusing. This page tries to categorize them and provide lots of links.

See also these thoughtful and detailed discussions:
- [Python Plotting for Exploratory Analysis](https://pythonplot.com)
- [A Dramatic Tour through Python’s Data Visualization Landscape)](https://dsaber.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/)

## Matplotlib (MPL)

Daddy of them all, sometimes literally. Complex, infinitely versatile, data-agnostic. Although it can do more or less anything, it may need lots of declarative code telling it what to do.

Beware, there are two APIs with confusingly different syntax. The 'Matlab' version is simple to use but not very customizable. The 'object oriented' version needs a bit more code up front but there have been [persuasive arguments](https://pbpython.com/effective-matplotlib.html) that any data scientist should always use this from the start.

## Packages based on MPL

Since MPL is relatively low-level but ultra-flexible, there are various approaches to adding an interface layer on top. These add more domain-appropriate defaults and useful, easy to use functions.

### Pandas plot

Any complex data is probably already in a Pandas dataframe, so it is useful to have a quick-and-dirty plot function built in. However, these are MPL plots under the hood, so it is common to
- pass in the axes of an existing MPL figure
- use MPL to add further customization to the Pandas plot

### Seaborn

Conceptually similar to the Pandas plot but much more statistically oriented. Excellent defaults and a variety of plot types that are otherwise hard to create.

Seaborn isn't general-purpose, but it can be excellent at what it chooses to focus on.

## Packages based on 'the language of graphics'

It was [Hadley Wickham](http://hadley.nz) who started it, an R programmer who created ggplot2 and wrote a [famous book](https://smile.amazon.com/gp/product/331924275X) about it. Data scientists working in Python often refer to 'ggplot envy', and there have been various attempts to pythonize the concepts.

### ggplot
