import numpy as np
import pandas as pd
import itertools  

import matplotlib.pyplot as plt
import altair as alt
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.palettes import Dark2_5 as palette
import plotly.express as px

import streamlit as st

import astropy.cosmology as cosm
import astropy.units as u
from astropy.cosmology import z_at_value

# Set up the data in multiple formats
# We could cache these, but recalculation is fast enough
zvals = np.arange(0, 20, 0.1)
cosmologies = cosm.parameters.available

df = pd.DataFrame()
df['zvals'] = zvals
for c in cosmologies:
    cosm_obj = getattr(cosm, c)
    df[c] = cosm_obj.lookback_time(zvals)
df_long = df.melt('zvals', var_name='model', value_name='lookback')

# Define a variety of plot functions

def angular_diameter():
    # In this case we just need to define the matter density 
    # and hubble parameter at z=0.

    # Note the default units for the hubble parameter H0 are km/s/Mpc. 
    # We will pass in a `Quantity` object with the units specified. 

    cosmo = cosm.FlatLambdaCDM(H0=70*u.km/u.s/u.Mpc, Om0=0.3)

    dist = cosmo.angular_diameter_distance(zvals)

    ages = np.array([13, 10, 8, 6, 5, 4, 3, 2, 1.5, 1.2, 1])*u.Gyr
    ageticks = [z_at_value(cosmo.age, age) for age in ages]

    fig = plt.figure(figsize=(6,4))
    ax = fig.add_subplot(111)
    ax.plot(zvals, dist)
    ax2 = ax.twiny() # upper x axis for ages
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

    st.pyplot()

def lookback_mpl():

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

    st.markdown('Note that the plot has been zoomed to high redshift to show the difference between cosmologies')


def lookback_altair():
    chart = alt.Chart(df_long).mark_line().encode(
        x='zvals',
        y='lookback',
        color='model'
    ).properties(width=600, height=600)
    st.altair_chart(chart, width=-1)
    st.markdown('There is a bug in the height setting (https://github.com/streamlit/streamlit/issues/542)')
    st.markdown('Altair charts are static so there is no zoom')

def lookback_bokeh():
    colors = itertools.cycle(palette)    

    p = figure(title='Lookback times', 
                x_axis_label='Redshift z', 
                y_axis_label='Lookback time (GYr)')
    for c in cosmologies:
        p.line(df['zvals'], df[c], legend_label=c, color=next(colors))
    st.bokeh_chart(p)
    st.markdown('Select box zoom or wheel zoom from the menu, then use the mouse')

def lookback_plotly():
    p2 = px.line(df_long, x="zvals", y="lookback", color='model')
    p2.update_xaxes(title_text='Redshift z')
    p2.update_yaxes(title_text='Lookback time (GYr)')

    st.plotly_chart(p2, width=800, height=600)
    st.markdown('The Plotly menu only appears when the mouse pointer is over the plot')
    st.markdown('Box zoom is enabled by default')

# Set up the interface

st.title('Cosmology Examples')

options = {'angular diameter': angular_diameter,
            'lookback time: Matplotlib':lookback_mpl,
            'lookback time: Altair': lookback_altair,
            'lookback time: Bokeh': lookback_bokeh,
            'lookback time: Plotly': lookback_plotly,
            }
to_plot = st.sidebar.radio("Type of plot", list(options.keys()), 0)

# Run the selected function

st.markdown(f'## {to_plot}')
options[to_plot]() # a function call
