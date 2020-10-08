from motion_detector_app import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df['start_string'] = df['Start'].dt.strftime("%Y-%m-%d %H:%M:%S")
df['end_string'] = df['End'].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type = 'datetime', height = 250, width = 1200, title = "Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks=1

# Adding the hover object
hover = HoverTool(tooltips=[("Start", "@start_string"), ('End', '@end_string')])
p.add_tools(hover)

q = p.quad(left = 'Start', right = 'End', bottom = 0, top = 1, color = 'blue', source=cds)

path = 'C:\\Users\\derek\\Desktop\\MIDS Program\\python_apps_udemy\\13_webcam_motion_detector\\webcam_graph.html' 

output_file(path)
show(p)