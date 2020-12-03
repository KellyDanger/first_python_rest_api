# import flask
from flask import Flask

# set up application, referencing this file
app = Flask(__name__)

# creates route @ used for Flask
@app.route('/')
# define the function for this route
def index():
  return "Hullooooo Wurld!"

if __name__ == "__main__":
  app.run(debug=True)