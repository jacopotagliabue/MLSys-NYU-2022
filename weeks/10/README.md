# Week 10

## Error analysis, testing etc.

The `notebooks` folder contain some sample code we will be using to investigate failure mode of different models, and appreciate how hard testing and evaluation actually is in practice.

The modelling aspect per se is not that important, as we are focusing here on evaluating performances _given a trained model_ (sometime, we may be asked to help evaluate a model we did _not_ train!). 

For brevity, please note that some required, non-standard packages can be found inside the cells with the special syntax `!pip install XXX`.

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

* [Streamlit](https://docs.streamlit.io/library/get-started) tutorial is a fantastic way to understand its main concepts
* The original [Model Cards](https://arxiv.org/pdf/1810.03993.pdf) paper from Google
* Behavioral testing in NL: [Checklist](https://www.microsoft.com/en-us/research/publication/beyond-accuracy-behavioral-testing-of-nlp-models-with-checklist/)
* From your professor + Metaflow creators, [DAG Cards](https://arxiv.org/abs/2110.13601)
* On the importance of a rounded evaluation, see also the [CIKM 2022 Data Challenge](https://github.com/RecList/evalRS-CIKM-2022) (all open source) in the RecSys domain