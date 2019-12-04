from bokeh.plotting import figure,output_file,save
from bokeh.io import curdoc,show

x=[1,2,3,4,5]
y=[3,4,5,6,7]

fig=figure(plot_height=500,plot_width=1000)
fig.line(x=x,y=y)
show(fig)
