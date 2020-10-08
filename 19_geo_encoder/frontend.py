from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func    
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd
import datetime

from lat_lon_conversion import address_conversion

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
        df = pd.read_csv(file) # changed from file
        df1 = address_conversion(df)
        filename=datetime.datetime.now().strftime("sample_files/%Y-%m-%d-%H-%M-%S-%f"+".csv")
        df1.to_csv(filename,index=None)
        return render_template("index.html", btn="download.html") 

@app.route("/download")
def download():
    # print(file.shape)
    return send_file(filename, attachment_filename="download.xlsx", as_attachment=True)
    return file

if __name__ == '__main__':
    app.debug = True
    app.run()

