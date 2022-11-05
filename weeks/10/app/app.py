"""

This a streamlit app that retrieves the latest Metaflow local run, displays data rows
and make available a simple interactive UI for people to test the model!

Documenting your model, through cards, and make its predictions easily accessible
is a fundamental component of building trust in your model across your organization! 

"""

# import libraries
import streamlit as st
from metaflow import Flow
from metaflow import get_metadata, metadata
import matplotlib.pyplot as plt
# make sure we point the app to the flow folder
# NOTE: MAKE SURE TO RUN THE FLOW AT LEAST ONE BEFORE THIS ;-)
FLOW_NAME = 'MyRegressionFlow' # name of the target class
# Set the metadata provider as the src folder in the project,
# which should contains /.metaflow
metadata('../src')
# Fetch currently configured metadata provider - check it's local!
print(get_metadata())

# build up the dashboard
st.markdown("# Regression playground")
st.write("This application shows the dataset and predictions made by our model!")
    
@st.cache
def get_latest_successful_run(flow_name: str):
    "Gets the latest successfull run."
    for r in Flow(flow_name).runs():
        if r.successful: 
            return r

# get artifacts from latest run, using Metaflow Client API
latest_run = get_latest_successful_run(FLOW_NAME)
latest_model = latest_run.data.modecd .l
latest_X_train = latest_run.data.X_train
y_predicted = latest_run.data.y_predicted
y_test = latest_run.data.y_test

# show dataset
st.markdown("## Dataset")
st.write("First 10 Xs in the training set:")
st.write(latest_X_train[:3])

# show predictions
st.markdown("## Predictions")
st.write("Model coeff: {}, intercept: {}".format(
    latest_model.coef_[0], latest_model.intercept_
))
fig, ax = plt.subplots()
ax.scatter(y_predicted, y_test, edgecolors=(0, 0, 1))
ax.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--', lw=3)
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')
plt.tight_layout()
st.pyplot(fig)

# play with the model
st.markdown("## Model")
_x = st.text_input('Input value (float):', '10.0')
val = latest_model.predict([[float(_x)]])
st.write('Input is {}, prediction is {}'.format(_x, val))