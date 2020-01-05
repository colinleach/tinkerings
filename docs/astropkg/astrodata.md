---
title: Astronomy Data Visualization and Manipulation
nav_order: 3
parent: Astronomy-related packages
---

# {{ page.title }}

This can include sky maps such as WWT on a PC (see below) or Google's version on my phone. Much of the professional software is for handling FITS files. This can be done in a general way with AstroPy, but there are also domain-specific tools, These sometimes have Python wrappers, sometimes not.

## Worldwide Telescope

Essentially, planetarium software for your home. There is a [web version](http://worldwidetelescope.com/webclient/) of the WWT and various [web resources for developers](http://worldwidetelescope.com/GetInvolved/Develop) for the JavaScript-literate.

It is now open source but originally came from Microsoft Research. The full desktop app is still Windows-only, and pywwt is a rare example of an open-source Python package that has more capability on Windows then on *nix. Whatever, it's pretty unique and valuable.

### ds9

SAO ds9 (Deep Space 9, as in Star Trek) is an astronomical image viewer and manipulator. 

Links: [website](http://ds9.si.edu/site/Home.html), [Astrobite](https://astrobites.org/2011/03/09/how-to-use-sao-ds9-to-examine-astronomical-images/)

## GAIA

The Graphical Astronomy and Image Analysis Tool. It is a derivative of the [Skycat](https://www.eso.org/sci/observing/tools/skycat.html) catalog and is distributed as part of the [Starlink](http://starlink.eao.hawaii.edu/starlink/WelcomePage) package.
 
Links: [website](http://star-www.dur.ac.uk/~pdraper/gaia/gaia.html), [download](http://starlink.eao.hawaii.edu/starlink)

### SExtractor

Source Extractor, a program that operates on a FITS image to automatically detect objects.  Once sources have been identified, a variety of measurements are made including source size, shape and magnitude.  

Links: [website](http://www.astromatic.net/software/sextractor), PDF guide, [SExtractor for Dummies](http://astroa.physics.metu.edu.tr/MANUALS/sextractor/Guide2source_extractor.pdf).

### Sherpa and other CIAO software

CIAO is the software suite developed by the Chandra X-Ray Center for analysing data from the Chandra X-ray Telescope. It can also be used with data from other Astronomical observatories, whether ground or space based.

CIAO: [homepage](http://cxc.cfa.harvard.edu/ciao/)

Sherpa performs forward fitting of models to data in N dimensions, and is a central part of CIAO: [website](http://cxc.cfa.harvard.edu/sherpa/)

ds9 is used for visualization.

### TOPCAT 

This is an interactive graphical viewer and editor for tabular data. Its aim is to provide most of the facilities that astronomers need for analysis and manipulation of source catalogues and other tables, though it can be used for non-astronomical data as well. It understands a number of different astronomically important formats (including FITS, VOTable and CDF) and more formats can be added.

Written in Java and currently needs Java 8 installed.

Links: [website](http://www.star.bris.ac.uk/~mbt/topcat/)
