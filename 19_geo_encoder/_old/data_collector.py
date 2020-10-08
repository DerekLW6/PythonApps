from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from send_email import send_email
from sqlalchemy.sql import func    

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password6@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jawhvemgopjtct:91b75c231ef1b916b6bc160516906485ce4580f02852bda1ced1044547faf09d@ec2-54-81-37-115.compute-1.amazonaws.com:5432/dbiqfusolvo5jo?sslmode=require'
db = SQLAlchemy(app) 

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height']
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height, 1)
            count = db.session.query(Data.height_).count()
            # send_email(email, height, average_height, count) Here
            return render_template("success.html") 

    return render_template('index.html', text = "Email already in use, try another.") # 

if __name__ == '__main__':
    app.debug = True
    app.run()

