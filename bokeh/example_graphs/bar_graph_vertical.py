#!/usr/bin/python

import io
import json
import os

from bokeh.io import export_png_and_data    # Custom function
from bokeh.plotting import figure, save, show, output_file, curdoc

if __name__ == "__main__":

    output_file('vbar.html')

    # Set up the plot
    p = figure(plot_width=400, plot_height=400, title="title_title", toolbar_location=None)
    p.vbar(x=[1, 2, 3], width=0.5, bottom=0,
        top=[1.2, 2.5, 3.7], color="firebrick", name="the_bars")
    
    # Set identifiers for the figure elements
    p.xaxis.name = "the_xaxis"
    p.xaxis.axis_label = "xaxis_labely"
    p.yaxis.name = "the_yaxis"
    p.yaxis.axis_label = "yaxis_label"
    p.title.name = "the_title"

    # Export to HTML, PNG, and get bbox data
    data = export_png_and_data(p, "vbar.png", "vbar.html")
    print data
    
    with open("vbar_data.json", "w") as f:
        json.dump(data, f)
