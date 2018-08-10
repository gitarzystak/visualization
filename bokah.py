
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
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource, Div
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure

# Set up data
N = 200
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))
source1 = ColumnDataSource(data=dict(x=x, y=y))
source2 = ColumnDataSource(data=dict(x=x, y=y))

#Description
desc = Div(text=open(join(dirname(__file__), "description.html")).read(), width=800)

# Set up plot
plot = figure(plot_height=400, plot_width=400, title="Interferencja 1D",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

plot1 = figure(plot_height=400, plot_width=400, title="Fala 1",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

plot1.line('x', 'y', source=source1, line_width=3, line_alpha=0.6)

plot2 = figure(plot_height=400, plot_width=400, title="Fala 2",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

plot2.line('x', 'y', source=source2, line_width=3, line_alpha=0.6)

# change the axes labels
xlabel="X"
ylabel="E"
plot.xaxis.axis_label = xlabel
plot1.xaxis.axis_label = xlabel
plot2.xaxis.axis_label = xlabel

plot.yaxis.axis_label = ylabel
plot1.yaxis.axis_label = ylabel
plot2.yaxis.axis_label = ylabel


# Set up widgets
#text = TextInput(title="title", value='my sine wave')
offset1 = Slider(title="offset 1", value=0.0, start=-5.0, end=5.0, step=0.1)
amplitude1 = Slider(title="amplitude 1", value=1.0, start=-5.0, end=5.0, step=0.1)
phase1 = Slider(title="phase 1", value=0.0, start=0.0, end=2*np.pi)
freq1 = Slider(title="frequency 1", value=1.0, start=0.1, end=5.1, step=0.1)

offset2 = Slider(title="offset 2", value=0.0, start=-5.0, end=5.0, step=0.1)
amplitude2 = Slider(title="amplitude 2", value=1.0, start=-5.0, end=5.0, step=0.1)
phase2 = Slider(title="phase 2", value=0.0, start=0.0, end=2*np.pi)
freq2 = Slider(title="frequency 2", value=1.0, start=0.1, end=5.1, step=0.1)

# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value

#text.on_change('value', update_title)

def update_data(attrname, old, new):

    # Get the current slider values
    a1 = amplitude1.value
    b1 = offset1.value
    w1 = phase1.value
    k1 = freq1.value

    # Get the current slider values
    a2 = amplitude2.value
    b2 = offset2.value
    w2 = phase2.value
    k2 = freq2.value

    # Generate the new curve
    x = np.linspace(0, 4*np.pi, N)
    y = a1*np.sin(k1*x + w1) + b1 + a2*np.sin(k2*x + w2) + b2
    y1 = a1*np.sin(k1*x + w1) + b1 
    y2 = a2*np.sin(k2*x + w2) + b2
    source.data = dict(x=x, y=y)
    source1.data = dict(x=x, y=y1)
    source2.data = dict(x=x, y=y2)        

for w in [offset1, amplitude1, phase1, freq1, offset2, amplitude2, phase2, freq2]:
    w.on_change('value', update_data)


# Set up layouts and add to document
#inputs = widgetbox(text, offset1, amplitude1, phase1, freq1, offset2, amplitude2, phase2, freq2)
inputs = widgetbox(offset1, amplitude1, phase1, freq1, offset2, amplitude2, phase2, freq2)

curdoc().add_root(column(desc,row(inputs, plot1, plot2, plot, width=800)))
#curdoc().add_root(row(inputs, plot1, plot2, plot, width=800))
curdoc().title = "Interferencja 1D"
