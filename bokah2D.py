
''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve sliders.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/sliders
in your browser.
'''
import numpy as np

from bokeh.io import curdoc
from os.path import dirname, join
from bokeh.layouts import row, column, widgetbox
from bokeh.models import ColumnDataSource, Div
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure

#define funny wave
def CylWave2D(x,y,k=1):
    xx, yy = np.meshgrid(x, y)
    r=xx**2+yy**2
    #phi=np.atan(yy/xx)
    d = np.real(1/r*np.exp(1j*k*r))
    return d

# Set up the plots

N = 500
x = np.linspace(1, 10, N)
y = np.linspace(1, 10, N)
d = CylWave2D(x,y)

p = figure(x_range=(0, 10), y_range=(0, 10),
           tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")])
# must give a vector of image data for image parameter
p.image(image=[d], x=0, y=0, dw=10, dh=10, palette="Spectral11")

# Set up callbacks

def update_title(attrname, old, new):
    plot.title.text = text.value

#text.on_change('value', update_title)

def update_data(attrname, old, new):

    # Get the current slider values for wave 1
    a1 = amplitude1.value
    b1 = offset1.value
    w1 = phase1.value
    k1 = freq1.value

    # Get the current slider values for wave 2
    a2 = amplitude2.value
    b2 = offset2.value
    w2 = phase2.value
    k2 = freq2.value

    # Generate the new curves
    x = np.linspace(0, 4*np.pi, N)
    y1 = a1*np.sin(k1*x + w1) + b1 
    y2 = a2*np.sin(k2*x + w2) + b2
    y=y1+y2
    source.data = dict(x=x, y=y)
    source1.data = dict(x=x, y=y1)
    source2.data = dict(x=x, y=y2)        

# Set up layouts and add to document
#inputs = widgetbox(text, offset1, amplitude1, phase1, freq1, offset2, amplitude2, phase2, freq2)
#inputs = widgetbox(offset1, amplitude1, phase1, freq1, offset2, amplitude2, phase2, freq2)

curdoc().add_root(p)
#curdoc().add_root(row(inputs, plot1, plot2, plot, width=800))
curdoc().title = "Interferencja 2D"
