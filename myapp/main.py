from bokeh.plotting import figure,output_file,save
from bokeh.io import curdoc,show

x=[1,2,3,4,5]
y=[3,4,5,6,7]

fig=figure(plot_height=500,plot_width=1000, tools="save", x_range=[0,10], y_range=[0,10],toolbar_location="below")
fig.line(x=x,y=y)
fig.image_url(url=["myapp/static/images/base.png"],x=0,y=0,w=100,h=100,anchor="bottom_left")
show(fig)
