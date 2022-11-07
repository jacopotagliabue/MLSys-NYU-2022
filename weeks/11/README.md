# Week 11

## Serving predictions

First, make sure to run the usual `training_flow.py` to produce the model artifacts (the script and the datasets are repeated in this week folder for convenience, but nothing has changed).

After installing the `requirements` in your virtual environment, you can spin up the API and interact with it using `flask run`, and then opening the browser at the url displayed in the terminal (usually `http://127.0.0.1:5000`).

The current endpoint is very barebone - check the slides for suggestions on how to best structure the response!

## Misc. Links

* If you want to try Fast API as an alternative to Flask, start with the [tutorial](https://fastapi.tiangolo.com/tutorial/).
* There are many ways to go from local to cloud deployment in a "better" (more scalable, principled) way than what we show with Flask. A cool framework that can used across many different setups is [BentoML](https://www.bentoml.com/).
* [Chip's book](https://www.amazon.com/Designing-Machine-Learning-Systems-Production-Ready/dp/1098107969) contains chapters on monitoring and re-training, if you want to go deeper in what happens after deployment.