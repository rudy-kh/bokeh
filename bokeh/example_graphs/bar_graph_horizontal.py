#!/usr/bin/python

import io
import json
import os

from bokeh.io import export_png_and_data    # Custom function
from bokeh.plotting import figure, save, show, output_file, curdoc

if __name__ == "__main__":

    output_file('hbar.html')

    # Set up the plot
    p = figure(plot_width=400, plot_height=400, title="title_title", toolbar_location=None)
    p.hbar(y=[1, 2, 3], height=0.5, left=0,
       right=[1.2, 2.5, 3.7], color="firebrick", name="the_bars")
    
    # Set identifiers for the figure elements
    p.xaxis.name = "the_xaxis"
    p.xaxis.axis_label = "xaxis_label"
    p.yaxis.name = "the_yaxis"
    p.yaxis.axis_label = "yaxis_label"
    p.title.name = "the_title"
    if p.grid[0].dimension == 0:
        p.grid[0].name = "the_x_gridlines"
        p.grid[1].name = "the_y_gridlines"
    else:
        p.grid[0].name = "the_y_gridlines"
        p.grid[1].name = "the_x_gridlines"

    # Export to HTML, PNG, and get bbox data
    data = export_png_and_data(p, "hbar.png", "hbar.html")
    print data

    with open("hbar_data.json", "w") as f:
        json.dump(data, f)
