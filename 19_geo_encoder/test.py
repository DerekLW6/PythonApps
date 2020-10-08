import numpy as np
import pandas as pd

from lat_lon_conversion import address_conversion

df = pd.read_csv('test2.csv')
# print(df.columns)

new_df = address_conversion(df)
print(type(new_df))
print(new_df.head())

       # file = request.files['file'] #receiving the file
        # file.save(secure_filename("uploaded_" + file.filename))
        # print(type(file))
        # new_file = address_conversion(file)
        # print(new_file.head())
        # with open("uploaded_" + file.filename, "a") as f:  "uploaded_" + file.filename
        #     f.write("This was added")

        # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password6@localhost/frontend'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jawhvemgopjtct:91b75c231ef1b916b6bc160516906485ce4580f02852bda1ced1044547faf09d@ec2-54-81-37-115.compute-1.amazonaws.com:5432/dbiqfusolvo5jo?sslmode=require'
# db = SQLAlchemy(app) 

# class Data(db.Model):
#     __tablename__ = "data"
#     id = db.Column(db.Integer, primary_key=True)
#     email_ = db.Column(db.String(120), unique=True)
#     height_ = db.Column(db.Integer)

#     def __init__(self, email_, height_):
#         self.email_ = email_
#         self.height_ = height_