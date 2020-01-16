# Python standard library
import time
import warnings

# Third-party software
import numpy as np

# Astropy
from astropy import coordinates as coord
from astropy import units as u
from astropy.table import Table

# Astroquery. This tutorial requires 0.3.5 or greater.
import astroquery
from astroquery.simbad import Simbad
from astroquery.vo_conesearch import conf, conesearch, vos_catalog

# Set up matplotlib
import matplotlib.pyplot as plt

import streamlit as st

st.title('Conesearch Examples')
sbar_text = 'This page uses the `astroquery.vo_conesearch` package '
sbar_text += 'and borrows heavily from an astropy-tutorials demo.'
st.sidebar.markdown(sbar_text)


# options = {'angular diameter': angular_diameter,
#             'lookback time: Matplotlib':lookback_mpl,
#             'lookback time: Altair': lookback_altair,
#             'lookback time: Bokeh': lookback_bokeh,
#             'lookback time: Plotly': lookback_plotly,
#             }
# to_plot = st.sidebar.radio("Type of plot", list(options.keys()), 0)

st.markdown('## Catalogs available')
st.write(conesearch.list_catalogs())

target = st.sidebar.text_input('Astronomical object:', value='m31')
st.markdown('## Target object')
st.markdown(target)
c = coord.SkyCoord.from_name(target, frame='icrs')
st.write(c)

result = conesearch.conesearch(c, 0.1 * u.degree)
st.markdown(f'First non-empty table returned by {result.url}')
st.markdown(f'Number of rows is {result.nrows}')
