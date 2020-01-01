import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import altair as alt
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

import streamlit as st

import astropy.cosmology as cosm
import astropy.units as u

# In this case we just need to define the matter density 
# and hubble parameter at z=0.

# Note the default units for the hubble parameter H0 are km/s/Mpc. 
# We will pass in a `Quantity` object with the units specified. 

cosmo = cosm.FlatLambdaCDM(H0=70*u.km/u.s/u.Mpc, Om0=0.3)

zvals = np.arange(0, 20, 0.1)
dist = cosmo.angular_diameter_distance(zvals)

ages = np.array([13, 10, 8, 6, 5, 4, 3, 2, 1.5, 1.2, 1])*u.Gyr

from astropy.cosmology import z_at_value
ageticks = [z_at_value(cosmo.age, age) for age in ages]

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)
ax.plot(zvals, dist)
ax2 = ax.twiny()
ax2.set_xticks(ageticks)
ax2.set_xticklabels(['{:g}'.format(age) for age in ages.value])
zmin, zmax = 0, 5.9
ax.set_xlim(zmin, zmax)
ax2.set_xlim(zmin, zmax)
ax2.set_xlabel('Time since Big Bang (Gyr)')
ax.set_xlabel('Redshift')
ax.set_ylabel('Angular diameter distance (Mpc)')
ax.set_ylim(0, 1890)
ax.minorticks_on()

st.title('Cosmology')
st.pyplot()

st.markdown('## Next plot')

cosmologies = cosm.parameters.available

fig2 = plt.figure()
for c in cosmologies:
    cosm_obj = getattr(cosm, c)
    lookbacks = cosm_obj.lookback_time(zvals)
    plt.plot(zvals, lookbacks, label=c)

plt.xlim(5, 20)
plt.ylim(12.5, 14)
plt.xlabel('Redshift z')
plt.ylabel('Lookback time (GYr)')
plt.title('Lookback times for various cosmologies')
plt.legend()

st.pyplot()

df = pd.DataFrame()
df['zvals'] = zvals

for c in cosmologies:
    cosm_obj = getattr(cosm, c)
    df[c] = cosm_obj.lookback_time(zvals)

df_long = df.melt('zvals', var_name='model', value_name='lookback')
chart = alt.Chart(df_long).mark_line().encode(
    x='zvals',
    y='lookback',
    color='model'
)

st.altair_chart(chart, width=-1)


# select a palette
from bokeh.palettes import Dark2_5 as palette
# itertools handles the cycling
import itertools  

colors = itertools.cycle(palette)    

p = figure(title='Lookback times', 
            x_axis_label='Redshift z', 
            y_axis_label='Lookback time (GYr)')
for c in cosmologies:
    p.line(df['zvals'], df[c], legend_label=c, color=next(colors))
st.bokeh_chart(p)

import plotly.express as px
p2 = px.line(df_long, x="zvals", y="lookback", color='model')
st.plotly_chart(p2)