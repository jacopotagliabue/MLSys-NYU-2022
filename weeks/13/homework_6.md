# Homework #6 (due 12/09/2022)

## Task 1: implement a JSON response for a model endpoint (100%)

Let's consider again the Flask app we built in week 11. It did not have a specific route for model predictions, and did not have a structured output (it was returning a simple string to be displayed in HTML).

Following the considerations we discussed in class (and on the slides) on the primary use case for model endpoints - that is, machine-to-machine communication, let's build a new Flask app for the same model that is more suited for machines and not for humans using a browser window. In particular:

* build a new Flask app that retrieves the latest Metaflow model from the Metaflow data store; no front-end needed!
* build a GET prediction function `predict` that will respond to requests such as: `URL/predict?_x=10.0`;
* implement argument parsing in the function and run the model to get the target `y`;
* build a Python dictionary with `data` and `metadata` to structure your response (see the slides!);
* return a JSON object from the function by using Flask [JSONIFY](https://www.educba.com/flask-jsonify/) method.

If you did everything correctly, once you run your Flask app in the usual way, you should be able to open the browser at `URL/predict?_x=10.0`, and visualize the JSON response you prepared in the Python code!



