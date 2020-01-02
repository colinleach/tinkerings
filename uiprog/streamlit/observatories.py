import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

from astropy.time import Time
# from IPython.display import Image

from urllib.parse import urlencode
from urllib.request import urlretrieve

southwest = [
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

chile = [
    'ALMA',
    'Cerro Paranal',
    'Cerro Tololo',
    'Gemini South',
    'La Silla Observatory',
    'Las Campanas Observatory',
    # 'Paranal Observatory',
]
regions = {'SouthWestUS': southwest,
            'Chile': chile}
curr_region = st.sidebar.selectbox("Choose a region", list(regions.keys()), 0)
st.sidebar.markdown("There is currently a [bug in streamlit](https://github.com/streamlit/streamlit/issues/475)")
st.sidebar.markdown("This prevents the map scrolling automatically to the new region")
st.sidebar.markdown("For now, use the mouse to pan and zoom - sorry")

sites = regions[curr_region]
curr_site = st.sidebar.radio("Sites in this region", sites)

@st.cache
def get_locations():
    return [EarthLocation.of_site(s) for s in sites]

locations = get_locations()

@st.cache
def make_locations_df():
    df = pd.DataFrame()
    df['name'] = sites
    df['lat'] = [loc.lat.value for loc in locations]
    df['lon'] = [loc.lon.value for loc in locations]
    return df

df = make_locations_df()

# Adding code so we can have map default to the center of the data
# Currently viewport only set on initial load: accepted as bug 
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

st.markdown(f"## {curr_site}")
current_time = Time.now()
observing_location = locations[sites.index(curr_site)]
here = df.loc[df['name'] == curr_site].iloc[0]
st.markdown(f"Latitude: {observing_location.lat:.2f}, Longitude: {observing_location.lon:.2f}")

# st.markdown(f"")
obj_name = 'm31'
vega = SkyCoord.from_name(obj_name)
aa_now = AltAz(location=observing_location, obstime=current_time)
sky_coord = vega.transform_to(aa_now)
st.markdown(f"{obj_name}: currently Alt = {sky_coord.alt:.2f}, Az = {sky_coord.az:.2f}")
