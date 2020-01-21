import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.io.misc import yaml
from astropy.time import Time
# from IPython.display import Image

# from urllib.parse import urlencode
# from urllib.request import urlretrieve

class Observatories():
    """

    """

    def __init__(self):
        with open('obs.yaml', 'r') as file:
            self.loc = yaml.load(file)
        self.df = pd.read_csv('observatories.csv')
        self.regions = list(self.df.region.unique())
        self.curr_region = 'NorthAmerica'

    def get_region(self):
        self.curr_region = st.sidebar.radio("Choose a region", self.regions)
        st.sidebar.markdown(
            "There is currently a [bug in streamlit]" +
            "(https://github.com/streamlit/streamlit/issues/475) " +
            "which prevents the map scrolling automatically to the new region")
        st.sidebar.markdown("For now, use the mouse to pan and zoom - sorry")
        self.get_site()

    def get_site(self):
        st.markdown(self.curr_region)
        self.sites = list(self.df[self.df.region == self.curr_region].name)
        self.curr_site = st.sidebar.selectbox("Sites in this region", self.sites)
        self.show_loc()

    def get_midpoint(self):
        # Adding code so we can have map default to the center of the data
        # Currently viewport only set on initial load: accepted as bug 
        region_df = self.df[self.df.region == self.curr_region]
        return (np.average(region_df['lat']), np.average(region_df['lon']))

    def show_chart(self):
        midpoint = self.get_midpoint()
        st.deck_gl_chart(
                    viewport={
                        'latitude': midpoint[0],
                        'longitude':  midpoint[1],
                        'zoom': 2,
                    },
                    layers=[{
                        'type': 'ScatterplotLayer',
                        'data': self.df,
                        'radiusScale': 150,
                        'radiusMinPixels': 5,
                        'getFillColor': [248, 24, 148],
                        'pickable': True,
                    },
                        {
                        "type": "TextLayer",
                        "data": self.df,
                        "getText": "name",
                        "getColor": [0, 0, 200, 200],
                        "getSize": 15,
                    },
                ]
            )

    def show_loc(self):
        st.markdown(f"## {self.curr_site}")
        self.observing_location = self.loc[self.curr_site]
        here = self.df.loc[self.df['name'] == self.curr_site].iloc[0]
        st.markdown(f"Latitude: {self.observing_location.lat:.2f}, " +
                    f"Longitude: {self.observing_location.lon:.2f}, " +
                    f"Height: {self.observing_location.height:.0f}")

    def show_sky_coord(self, obs_time=Time.now()):
        aa_now = AltAz(location=self.observing_location, obstime=obs_time)

        sky_coords = {}
        obj_names = st.sidebar.text_input('Sky object names (comma separated)', 'm31, vega')
        st.markdown(f'### Current sky positions from {self.curr_site}')
        for obj_name in obj_names.split(','):
            try:
                obj = SkyCoord.from_name(obj_name)
            except:
                st.markdown(f'**{obj_name}:** not found in Sesame')
                continue
            sky_coords[obj_name] = obj.transform_to(aa_now)
            st.markdown(f"**{obj_name}:** Alt = {sky_coords[obj_name].alt:.2f}, " +
                                        f"Az = {sky_coords[obj_name].az:.2f}")

    def show_interface(self):
        self.get_region()
        self.show_chart()
        self.show_sky_coord()

if __name__ == "__main__":
    obs = Observatories()
    obs.show_interface()

