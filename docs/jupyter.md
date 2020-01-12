---
title: Jupyter
nav_order: 20
---

# {{ page.title }}

## Extensions

Optimizing: https://towardsdatascience.com/optimizing-jupyter-notebook-tips-tricks-and-
nbextensions-26d75d502663

nb-black for prettifying code: https://github.com/dnanhkhoa/nb_black

## nbdev 
For full code development, exporting Python libraries and modules from Jupyter.

Docs:
- Website: [https://www.fast.ai/2019/12/02/nbdev/](https://www.fast.ai/2019/12/02/nbdev/)
- GitHub: [https://github.com/fastai/nbdev/](https://github.com/fastai/nbdev/)

## reviewnb 
For code review on GitHub, it gives better Jupyter diffs to help with merging pull requests. Note that this only runs on GitHub, nothing is local.

Docs: [https://www.reviewnb.com/#features](https://www.reviewnb.com/#features)

## Jupyter Books
 https://jupyterbook.org/intro.html

## RISE 
For slideshows

links: [docs](https://rise.readthedocs.io/en/maint-5.5/index.html)

## Voila 

For web presentations and dashboards. Serve the notebook in a browser with all ipywidgets live but the code either hidden or shown read-only.

Note that it's designed for ipywidgets and generally static content. It won't work for complex packages like Plotly and Bokeh that sort-of-tolerate Jupyter but aren't really designed for that environment.

Links: [docs](https://voila.readthedocs.io/), [GitHub](https://github.com/voila-dashboards/voila)

