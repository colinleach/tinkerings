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

**Book:** VanderPlas, "Python Data Science Handbook", chapter 4

This is a must-read for anyone wanting to dig deeper into Matplotlib. The printed version is relatively affordable, and the entire text is also freely available in [Jupyter notebook format](https://github.com/jakevdp/PythonDataScienceHandbook) and [HTML format](https://jakevdp.github.io/PythonDataScienceHandbook/)

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

### ggplot/ggpy

The version from yhat. Various websites are still live, but there appears to be no active development of this under either name since about 2016.

### plotnine

Another ggplot2-like package, which appears to have an active development community (late 2019). 

Links: [docs](https://plotnine.readthedocs.io/en/latest/), [Github](https://github.com/has2k1/plotnine)

### Altair

Newer than plotnine, different internals and somewhat different syntax, but firmly in the spirit of the grammar of graphics. Also an interestingly different implementation: Python code is translated to JSON, then passed to Vega Lite, a Javascript package which does the actual rendering. 

Links: [docs](), [GitHub]()

## Interactive packages for web browsers

These (like Altair, above) are built on top of Javascript libraries. Client-side code allows interactive pan, zoom, tooltips, file save and other user controls.

### Bokeh

Describes itself as 'an interactive visualization library for modern web browsers'. A NumFocus open-source project (like NumPy, Pandas, Jupyter, Astropy...) so takes integration seriously.

Links: [docs](https://docs.bokeh.org/en/latest/index.html), [GitHub](https://github.com/bokeh/bokeh)

Blogs:
- Data Visualization with Bokeh in Python [part 1](https://towardsdatascience.com/data-visualization-with-bokeh-in-python-part-one-getting-started-a11655a467d4), [part 2](https://towardsdatascience.com/data-visualization-with-bokeh-in-python-part-ii-interactions-a4cf994e2512), [part 3]
(https://towardsdatascience.com/data-visualization-with-bokeh-in-python-part-iii-a-complete-dashboard-dc6a86aa6e23). Though the author has also written that he [prefers Plotly](https://medium.com/@williamkoehrsen/the-plotly-syntax-is-more-intuitive-than-bokeh-which-means-plots-are-quicker-to-make-and-you-have-cd2598e8bcbd)! More efficient syntax and superior documentation, in his view.
- [Interactive Data Visualization in Python With Bokeh](https://realpython.com/python-data-visualization-bokeh/)
- [Visualizing Data with Bokeh and Pandas](https://programminghistorian.org/en/lessons/visualizing-with-bokeh)

### Plotly, etc

Plotly is a charting library built on top of d3.js. It is largely commercial but with an open-source Python version. The website will keep trying to sell you stuff but don't feel distracted - the important things are free.

Working with Pandas dataframes (and who wouldn't?) has been fraught and complex in the past. The recommendation used to be cufflinks as an add-in package, but Plotly API changes kept breaking it. I hated the whole mess and stuck to Bokeh as a more stable alternative.

Since mid-2019 it looks like the way to go is Plotly Express, described as 'a terse, consistent, high-level API for rapid data exploration and figure generation'. Thus, ignore anything on the web that talks about cufflinks, express or plotly_express, which is pretty much *everything* on the web. These are all now superceded by Plotly Express within Plotly 4.x. All clear?

They say Seaborn is an inspiration for Plotly Express, and it feels that way. Prettier and much more interactive, though.

Plotly: [docs](https://plot.ly/python/), [GitHub](https://github.com/plotly/plotly.py)

Plotly Express: [docs](https://plot.ly/python/plotly-express/). No idea about GitHub.

Blogs:
- [Introducing Plotly Express](https://medium.com/plotly/introducing-plotly-express-808df010143d?). Written by Plotly, so very positive.
- [Plotly Express: the Good, the Bad, and the Ugly](https://towardsdatascience.com/plotly-express-the-good-the-bad-and-the-ugly-dc941649687c). Leans positive, but points out some rough edges in this new/immature package.
- [The Next Level of Data Visualization in Python](https://towardsdatascience.com/the-next-level-of-data-visualization-in-python-dd6e99039d5e). Pre-Express but still makes some good points.
