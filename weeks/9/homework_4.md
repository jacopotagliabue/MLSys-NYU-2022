# Homework #4 (due 11/04/2022)

## Task 1: Experiment tracking (with Comet) and hyperparameter tuning (75%)
Thanks to our partnership with Comet ML, we can use their experiment tracking tool for free! We discussed the importance of experiment tracking in the class, and in this assignment you will be asked to start doing it! Consider again [small_flow.py](https://github.com/jacopotagliabue/MLSys-NYU-2022/blob/main/weeks/8/src/small_flow.py)  (the simple DAG-based regression training).

 Duplicate the script, change the class name, and change the `train_model` step: instead of a linear regression, use any other scikit-available algorithm from the class, as long as the algorithm has one hyperparameter (make sure to use a dataset that makes sense with the algorithm you choose - if you choose a classification algorithm, you need to generate an appropriate synthetic dataset). 
 
 Instead of training one model, you will:

* Make sure to have a validation split, not just train and test split.
* Use metaflow parallelization capabilities (foreach or branch!) to train multiple models: pick 4 values for the hyperparameter and train the model 4 times, each time with a different value.
* Evaluate the models on the validation set and pick the best one.
* Make sure to log the experiments in Comet: does the dashboard clearly show what model is the best?

When you submit the code, submit both the new script and screenshot / prints from your Comet dashboard, clearly illustrating the tracking (you can also share the dashboard with your TA)

Useful links: [Comet scikit docs](https://www.comet.com/docs/v2/integrations/ml-frameworks/scikit-learn/)
, [Metaflow foreach docs](https://docs.metaflow.org/metaflow/basics).


## Task 2: generalizing the flow (25%)

After you complete the first task, you will make the flow more general, by adding a new Metaflow Parameter. 

A Parameter allows us to inject values for our flow when we invoke it, making it more flexible.

* Duplicate the flow you obtained in part I
* Instead of hard-coding 4 values for the hyperparameter selection, declare a Parameter
variable in the class and run again the flow by providing the Parameter at runtime. HINT: you can provide values as comma-separated numbers (and then split the string) or as min-max of a range (and then generate the 4 values).
* As before, submit the flow and the Comet dashboard (with comments if necessary) to show your work.
