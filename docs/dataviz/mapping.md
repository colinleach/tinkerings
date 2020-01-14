---
title: Mapping Geographic Data
nav_order: 10
parent: Data Visualization
---

# {{ page.title }}

This page is very much a work in progress as I try to get my head round a complex and unfamiliar topic.

## Map Sources

Very commercial and competitive, but most have useful free entry levels. Typically you have to register and get a personal token.

### ESRI: ArcGIS

Esri is the company, ArcGIS the suite of products. A serious business with serious prices. Not really aimed at individuals who want to dabble, but there is a free [Developer plan](https://developers.arcgis.com/pricing/) for non-commercial use.

### QGIS

Free and open-source. Linked to OpenStreeMap. Opinions vary on how it compares with ArcGIS, but recent releases get good reviews and you can't beat the price. There are installers for Windows, Mac and many Linux distro.

Link: [homepage](https://qgis.org/en/site/index.html)

The desktop GUI can be extended with Python, and there are Python bindings for use in your own applications.

Blog: [PyQGIS in Jupyter Notebook](https://lerryws.xyz/posts/PyQGIS-in-Jupyter-Notebook)

### Mapbox

Commercial but with a decent free tier. You need your own API key.

Link: [homepage](https://www.mapbox.com/)

### TomTom

Commercial but with a decent free tier. You need your own API key.

Link: [homepage](https://developer.tomtom.com/)

Blogs:
- [Introduction to a Mapping API: TomTom](https://blog.goodaudience.com/python-tomtom-api-7c16d9fd7605)

There is a [Geocoding API for Python](https://geocoder.readthedocs.io/providers/TomTom.html)

### Geocoder

A wrapper for many other services, intended to give a more consistent interface.

Link: [docs](https://geocoder.readthedocs.io/index.html)

### Google Maps

Has a reputation as a [big-budget option](https://hackingandslacking.com/geographical-data-visualization-with-mapbox-6ef564ebc51e) for developers. I haven't used the API.

Link: [Google Maps Platform](https://cloud.google.com/maps-platform/)

## Data Sources

This is *really* complicated, so the list below barely scratches the surface.

### BigQuery

From Google, but more affordable than the maps platform.

Link: [](https://cloud.google.com/bigquery/)

## Data Handling

### GeoPandas

Extends the datatypes used by pandas to allow spatial operations on geometric types.

links: [docs](http://geopandas.org/)

### Iris

An iterface for working with mult-dimensional earth science data. Sort of a bridge between NumPy and Cartopy.

Links: [docs](https://scitools.org.uk/iris/docs/latest/index.html), [GitHub](https://github.com/SciTools/iris)

### Cartopy

A Python package 'designed to make drawing maps for data analysis and visualisation easy'. Emphasizes accuracy over large areas, rather than street-level detail. Open source but large chunks came from the UK Met Office.

Cartopy (more or less) replaces basemap, which is no longer maintained. It typically generates static maps in Matplotlib.

Links: [docs](https://scitools.org.uk/cartopy/docs/latest/), [GitHub](https://github.com/SciTools/cartopy). The docs are strong on example code. The API reference is quite spread around.

## Viewers

### Folium

A Python package built on leaflet.js visualization.

Links: [docs](https://python-visualization.github.io/folium/), [GitHub](https://github.com/python-visualization/folium)

Critical blog: [You Probably Shouldn’t Be Using Folium](https://medium.com/@cjriggio3/you-probably-shouldnt-be-using-folium-94913e16797a). Recommends geopandas + Bokeh.

### Bokeh and Plotly Express

Covered in more detail under plotting, both can produce a variety of interactive maps.

### ipyleaflet

A Jupyter widget for GIS.

Links: [docs](https://ipyleaflet.readthedocs.io/en/latest/), [GitHub](https://github.com/jupyter-widgets/ipyleaflet)

Blogs:
- [Interactive GIS in Jupyter with ipyleaflet](https://blog.jupyter.org/interactive-gis-in-jupyter-with-ipyleaflet-52f9657fa7a)

### geoplot

https://residentmario.github.io/geoplot/quickstart/quickstart.html

### geoplotlib

https://github.com/andrea-cuttone/geoplotlib

### Jupyter-gmaps

https://github.com/pbugnion/gmaps
