from flask import Flask, render_template

app = Flask(__name__)

# Adding a menu
@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime

    import pandas as pd
    import numpy as np

    from math import pi

    # Importing
    from bokeh.plotting import figure
    from bokeh.io import output_file, show
    from bokeh.embed import components 
    from bokeh.resources import CDN 

    # https://pandas-datareader.readthedocs.io/en/latest/index.html

    start = datetime.datetime(2020,1,4)
    end = datetime.datetime(2020,3,4)

    df = data.DataReader(name = "GOOG", data_source = 'yahoo', start = start, end = end)

    df = df.reset_index()

    # Filtering where close higher than open and vice versa
    inc = df.Close > df.Open
    dec = df.Open > df.Close
    w = 12*60*60*1000 # half day in ms

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

    p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "Google Candlestick", sizing_mode='scale_width')
    p.xaxis.major_label_orientation = pi/4
    p.grid.grid_line_alpha=0.3

    p.segment(df.Date, df.High, df.Date, df.Low, color="black")
    p.vbar(df.Date[inc], w, df.Open[inc], df.Close[inc], fill_color="#D5E1DD", line_color="black")
    p.vbar(df.Date[dec], w, df.Open[dec], df.Close[dec], fill_color="#F2583E", line_color="black")

    script1, div1 =  components(p)
    cdn_js = CDN.js_files[0]
    return render_template('plot.html', script1 = script1, 
    div1 = div1, cdn_js = cdn_js)

# Wesite at http://localhost:5000/
# Homepage
@app.route('/')
def home():
    return render_template('homepage.html')

# About Page
@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)