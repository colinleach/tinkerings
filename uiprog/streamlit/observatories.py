import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation
from astropy.time import Time
# from IPython.display import Image

from urllib.parse import urlencode
from urllib.request import urlretrieve

sites = [
 'Apache Point',
 'Catalina Observatory',
 'Discovery Channel Telescope',
#  'Hale Telescope',
 'Kitt Peak',
#  'Large Binocular Telescope',
 'Lick Observatory',
 'Lowell Observatory',
 'Mt Graham',
#  'Multiple Mirror Telescope',
 'Palomar',
#  'Sacramento Peak',
 'Very Large Array',
 'Whipple Observatory',
]

@st.cache
def get_locations():
    return [EarthLocation.of_site(s) for s in sites]

locations = get_locations()

@st.cache
def make_locations_df():
    locations = [EarthLocation.of_site(s) for s in sites]

    # lats = [loc.lat.value for loc in locations]
    # lons = [loc.lon.value for loc in locations]
    df = pd.DataFrame()
    df['name'] = sites
    df['lat'] = [loc.lat.value for loc in locations]
    df['lon'] = [loc.lon.value for loc in locations]
    return df

df = make_locations_df()
# Adding code so we can have map default to the center of the data
midpoint = (np.average(df['lat']), np.average(df['lon']))

st.deck_gl_chart(
            viewport={
                'latitude': midpoint[0],
                'longitude':  midpoint[1],
                'zoom': 5,
                # 'pitch': 50,
            },
            layers=[{
                'type': 'ScatterplotLayer',
                'data': df,
                'radiusScale': 150,
                'radiusMinPixels': 5,
                # 'elevationScale': 4,
                # 'elevationRange': [0, 1000],
                'getFillColor': [248, 24, 148],
                'pickable': True,
                # 'extruded': True,
            },
                {
                "type": "TextLayer",
                "data": df,
                "getText": "name",
                "getColor": [0, 0, 200, 200],
                "getSize": 15,
            },
]
        )
