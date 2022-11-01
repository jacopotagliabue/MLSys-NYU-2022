# Week 10

## Error analysis, testing etc.

The `notebooks` folder contain some sample code we will be using to investigate failure mode of different models, and appreciate how hard testing and evaluation actually is in practice.

Requirements needed for the notebooks are in the same folder.

## Documenting your flow

We will be using the built-in Metaflow `@card` [decorator](https://docs.metaflow.org/metaflow/visualizing-results/effortless-task-inspection-with-default-cards) to automatically produce documentation about what `training_flow.py` (which is the same linear regression flow from week 8) is doing.

When running the code, add the proper flag to the end: `python training_flow.py run --with card`. Once the flow completes, you can use `python training_flow.py card view start` to visualize the card!

## Sharing model and data with a UI prototype

The `app` folder contains a Streamlit app that uses Metaflow Client API to retrieve the artifacts from the latest run from `training_flow.py`.

Make sure all dependecies are installed and that you run the flow in `training_flow.py` at least once successfully. Then:

* cd into `app`
* run `streamlit run app.py`

A browser window will open with the app!

## Misc. Links

TBC