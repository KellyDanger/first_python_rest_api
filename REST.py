# import flask
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# set up application, referencing this file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///test.db'
# initialize the db
db = SQLAlchemy(app)

# https://www.youtube.com/watch?v=Z1RJmh_OqeA 
# at 18:37
# Need to figure out how to do this with postgres

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(200), nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow)



# creates route @ used for Flask
@app.route('/')
# define the function for this route
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)