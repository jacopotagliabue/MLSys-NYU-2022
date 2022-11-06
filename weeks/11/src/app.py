"""
    This script runs a small Flask app that displays a simple web form for users to insert some input value
    and retrieve predictions.

    Inspired by: https://medium.com/shapeai/deploying-flask-application-with-ml-models-on-aws-ec2-instance-3b9a1cec5e13
"""

from flask import Flask, render_template, request
import numpy as np
from metaflow import Flow
from metaflow import get_metadata, metadata

#### THIS IS GLOBAL, SO OBJECTS LIKE THE MODEL CAN BE RE-USED ACROSS REQUESTS ####

FLOW_NAME = 'MyRegressionFlow' # name of the target class that generated the model
# Set the metadata provider as the src folder in the project,
# which should contains /.metaflow
metadata('../src')
# Fetch currently configured metadata provider to check it's local!
print(get_metadata())

def get_latest_successful_run(flow_name: str):
    "Gets the latest successfull run."
    for r in Flow(flow_name).runs():
        if r.successful: 
            return r

# get artifacts from latest run, using Metaflow Client API
latest_run = get_latest_successful_run(FLOW_NAME)
latest_model = latest_run.data.model

# We need to initialise the Flask object to run the flask app 
# By assigning parameters as static folder name,templates folder name
app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/',methods=['POST','GET'])
def main():

  # on GET we display the page  
  if request.method=='GET':
    return render_template('index.html', project=FLOW_NAME)
  # on POST we make a prediction over the input text supplied by the user
  if request.method=='POST':
    # debug
    # print(request.form.keys())
    _x = request.form['_x']
    val = latest_model.predict([[float(_x)]])
    #  debug
    print(_x, val)
    # Returning the response to the client	
    return "Predicted Y is {}".format(val)
    

if __name__=='__main__':
  # Run the Flask app to run the server
  app.run(debug=True)