# import flask
from flask import Flask, render_template

# set up application, referencing this file
app = Flask(__name__)

# creates route @ used for Flask
@app.route('/')
# define the function for this route
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)