from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func    
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd
import datetime

from geopy.geocoders import ArcGIS


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    global filename
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_csv(file) 
        nom = ArcGIS()
        l=list(df)

        if 'Address' in l:
            # Geoencoding
            df['Address'] = df['Address'].apply(nom.geocode)
            df['latitude'] = df['Address'].apply(lambda x: x.latitude if x != None else None)
            df['longitude'] = df['Address'].apply(lambda x: x.longitude if x != None else None)

        elif 'address' in l:
            # Geoencoding
            df['address'] = df['address'].apply(nom.geocode)
            df['latitude'] = df['address'].apply(lambda x: x.latitude if x != None else None)
            df['longitude'] = df['address'].apply(lambda x: x.longitude if x != None else None)

        else:
            print("No Address Column Found")

        # filename=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"+".csv") text=df.to_html(), # return file # print(file.shape)
        df.to_csv('uploads/geocoded.csv',index=None)
        return render_template("index.html", btn="download.html") 

@app.route("/download")
def download():
    return send_file('C:\\Users\\derek\\Desktop\\MIDS Program\\python_apps_udemy\\19_geo_encoder\\uploads\\geocoded.csv', attachment_filename="yourfile.csv", as_attachment=True)
    

if __name__ == '__main__':
    app.debug = True
    app.run()

