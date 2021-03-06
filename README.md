# Bokeh: Maluuba FigureQA Fork

## Introduction

This fork of Bokeh gets the bounding boxes of drawn primitives. 

It is based on Bokeh version **0.12.6**.

Bokeh is very easy to use and extend, and has **no dependency on matplotlib**.

At a high-level, here's how the library works:

- The figure is defined in Python. Source code lives in the Bokeh Python library (**bokeh/bokeh**).
  - Make sure you add `name` attributes to the different parts of your figure.
  - Use the `export_png_and_data` function from bokeh.io to get the PNG and a Python dict of the bounding box data.
  - See the examples in `bokeh/bokeh/example_graphs`.

- The Bokeh Python library calls the Bokeh JavaScript library (**bokeh/bokehjs**) which renders the plot to a canvas using a headless browser, then exports this to a PNG.
  - The Python lib generates an HTML file with JSON defining the figure.
  - The JS lib takes the HTML file and renders it in a headless browser (PhantomJS).
  - The JS lib renders the figure (model-view coffeescript, like Backbone.js) and performs the drawing to canvas.
  - While drawing, the JS lib calculates bounding boxes, associates them with names defined in the Python figure, and saves these annotations to localStorage in PhantomJS.
  - The Python lib then grabs the data from the PhantomJS webdriver's localStorage.

## Prerequisites and Installation

Note: there's no need to install the requirements from `requirements.txt` if you run `setup.py`.

1. If on Linux, install these packages:
    - `libfontconfig` (e.g. `sudo apt-get install libfontconfig`).
    - `zlib` (e.g. `sudo apt-get install zlib1g-dev`)
    - `libjpeg` (e.g. `sudo apt-get install libjpeg-dev`)
1. Install NodeJS LTS from [here](https://nodejs.org/en/download/). These instructions are based on Node version **6.11.4**.
1. `npm install -g phantomjs-prebuilt` to install PhantomJS globally. This may have to be done in `sudo` or `Administrator` mode.
    - Note if you are using npm >= 5.x add `--unsafe-perm` to the command (see [here](https://github.com/Medium/phantomjs/issues/707)).
    - If you have trouble on Windows, try `npm cache clean --force`. A full list of troubleshooting tips can be found [here](https://github.com/Medium/phantomjs#troubleshooting).
1. Make sure the PhantomJS executable is on your PATH. On Windows, I found mine in `C:\Users\<user>\AppData\Roaming\npm\node_modules\phantomjs-prebuilt\lib\phantom\bin`.
1. Clone this repo or unzip the source from the release page.
1. `cd bokeh/bokehjs`.
1. `npm install`.
1. `cd ../bokeh`.
1. `python setup.py install --build-js`

## Development

See the Bokeh developer guide [here](https://bokeh.pydata.org/en/0.12.6/docs/dev_guide.html).

### Python + JS

To use changes to both the Bokeh Python and JS libs, you need to run either
- `python setup.py develop --build-js` (to build the JS bundle fresh and include it in the Python library)
or
- `python setup.py develop --install-js` (to use the last built JS bundle)

**every time** you want to use new Bokeh JS changes with the Bokeh Python library.

I.e. if you've made changes to the JS files and want to test them with the Python lib, you need to run `python setup.py develop --build-js` again to package the latest JS lib into the Python lib.

### Python Only

If you've made changes to the Python files only, and run `python setup.py develop --build-js/--install-js` once, you don't need to do anything more.

Your Bokeh Python changes will be picked up immediately.

### JS Only

1. `cd bokeh/bokehjs`
1. `gulp watch` if you want to recompile on new changes, or `gulp dev-build` to build an un-minified bundle.

#### Workflow

You can run `gulp watch` to rebuild the library in dev mode everytime bokeh/bokehjs/src files are modified. 

To use this bundle right away, you can use a modified HTML file generated by the Python lib. This can be done with a reference to the generated bundle in the build directory using a script tag like `<script type="text/javascript" src="build/js/bokeh.js"></script>`. This will pick up the latest bundle genenerated by gulp.

This lets you analyze console errors and debug faster than rebuilding the whole Bokeh library every time.

See the samples in the `bokeh/bokeh/example_graphs` directory to see how you can generate one of these files.

## Usage and Examples

Some examples are provided in `bokeh/bokeh/example_graphs`.

# Stuff from original Bokeh README

<table>
<tr>
  <td>Latest Release</td>
  <td><img src="https://badge.fury.io/gh/bokeh%2Fbokeh.svg" alt="latest release" /></td>
</tr>
<tr>
  <td>License</td>
  <td>
    <a href="https://github.com/bokeh/bokeh/blob/master/LICENSE.txt">
    <img src="https://img.shields.io/github/license/bokeh/bokeh.svg" alt="Bokeh license" />
    </a>
  </td>
</tr>
<tr>
  <td>Build Status</td>
  <td>
    <a href="https://travis-ci.org/bokeh/bokeh">
    <img src="https://travis-ci.org/bokeh/bokeh.svg?branch=master" alt="build status" />
    </a>
  </td>
</tr>
<tr>
  <td>Conda</td>
  <td>
    <a href="http://bokeh.pydata.org/en/latest/docs/installation.html">
    <img src="http://pubbadges.s3-website-us-east-1.amazonaws.com/pkgs-downloads-bokeh.png" alt="conda downloads" />
    </a>
  </td>
</tr>
<tr>
  <td>PyPI</td>
  <td>
    <img src="http://bokeh.pydata.org/pip-bokeh-badge.png" />
  </td>
</tr>
<tr>
  <td>Gitter</td>
  <td>
    <a href="https://gitter.im/bokeh/bokeh?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge">
    <img src="https://badges.gitter.im/bokeh/bokeh.svg" />
    </a>
  </td>
</tr>
<tr>
  <td>Twitter</td>
  <td>
    <a href="https://https://twitter.com/BokehPlots">
    <img src="https://img.shields.io/twitter/follow/bokehplots.svg?style=social&label=Follow" />
    </a>
  </td>
</tr>
</table>

Bokeh, a Python interactive visualization library, enables beautiful and
meaningful visual presentation of data in modern web browsers. With Bokeh,
you can quickly and easily create interactive plots, dashboards, and data
applications.

Bokeh helps provide elegant, concise construction of novel graphics in the
style of D3.js, while also delivering **high-performance** interactivity over
very large or streaming datasets.

[Interactive gallery](http://bokeh.pydata.org/en/latest/docs/gallery.html)
---------------------------------------------------------------------------

<p>
<table cellspacing="20">
<tr>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/image.html">
  <img alt="image" src="http://bokeh.pydata.org/en/latest/_images/image_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/anscombe.html">
  <img alt="anscombe" src="http://bokeh.pydata.org/en/latest/_images/anscombe_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/stocks.html">
  <img alt="stocks" src="http://bokeh.pydata.org/en/latest/_images/stocks_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/lorenz.html">
  <img alt="lorenz" src="http://bokeh.pydata.org/en/latest/_images/lorenz_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/candlestick.html">
  <img alt="candlestick" src="http://bokeh.pydata.org/en/latest/_images/candlestick_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/color_scatter.html">
  <img alt="scatter" src="http://bokeh.pydata.org/en/latest/_images/scatter_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/iris_splom.html">
  <img alt="splom" src="http://bokeh.pydata.org/en/latest/_images/splom_t.png" />
  </a>
  </td>

</tr>
<tr>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/iris.html">
  <img alt="iris" src="http://bokeh.pydata.org/en/latest/_images/iris_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/histogram.html">
  <img alt="histogram" src="http://bokeh.pydata.org/en/latest/_images/histogram_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/periodic.html">
  <img alt="periodic" src="http://bokeh.pydata.org/en/latest/_images/periodic_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/texas.html">
  <img alt="choropleth" src="http://bokeh.pydata.org/en/latest/_images/choropleth_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/burtin.html">
  <img alt="burtin" src="http://bokeh.pydata.org/en/latest/_images/burtin_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/streamline.html">
  <img alt="streamline" src="http://bokeh.pydata.org/en/latest/_images/streamline_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/image_rgba.html">
  <img alt="image_rgba" src="http://bokeh.pydata.org/en/latest/_images/image_rgba_t.png" />
  </a>
  </td>

</tr>
<tr>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/brewer.html">
  <img alt="stacked" src="http://bokeh.pydata.org/en/latest/_images/stacked_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/quiver.html">
  <img alt="quiver" src="http://bokeh.pydata.org/en/latest/_images/quiver_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/elements.html">
  <img alt="elements" src="http://bokeh.pydata.org/en/latest/_images/elements_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/boxplot.html">
  <img alt="boxplot" src="http://bokeh.pydata.org/en/latest/_images/boxplot_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/categorical.html">
  <img alt="categorical" src="http://bokeh.pydata.org/en/latest/_images/categorical_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/unemployment.html">
  <img alt="unemployment" src="http://bokeh.pydata.org/en/latest/_images/unemployment_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/les_mis.html">
  <img alt="les_mis" src="http://bokeh.pydata.org/en/latest/_images/les_mis_t.png" />
  </a>
  </td>

</tr>
</table>
</p>

Documentation
-------------
Visit the [Bokeh web page](http://bokeh.pydata.org/en/latest) for information and full documentation.

Contribute to Bokeh
-------------------
To contribute to Bokeh, please review the [Developer Guide](http://bokeh.pydata.org/en/latest/docs/dev_guide.html).

Follow us
---------
Follow us on Twitter [@bokehplots](https://twitter.com/BokehPlots) and on [YouTube](https://www.youtube.com/channel/UCK0rSk29mmg4UT4bIOvPYhw).
