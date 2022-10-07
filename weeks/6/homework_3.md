# Homework 3 (Due 10/14/22)

For each problem, you should submit a python file (a "script") with the question name, like `question_1.py`, `question_2.py`, etc... These files should only use standard python or the libraries that are included in `requirements.txt`. Your grader should be able to install the libraries from `requirements.txt` into a virtual environment and then run your script from the command line like:

```commandline
python question_1.py
```

You can assume that your grader is running the script from the same folder that this document is in.

## Dataset

I have constructed a fake Fraud dataset for this homework assignment. There are 3 CSVs in `data/`:

### payments.csv
Each row of this CSV corresponds to an individual payment. The columns are:

- `id`: A unique ID for the payment.
- `merchant_id`: The unique ID of the merchant who took the payment.
- `buyer_id`: The unique ID of the buyer who made the payment.
- `transaction_timestamp`: The time at which the payment occurred. 
- `payment_amount`: The number of US Cents associated with the payment.
- `chargeback_timestamp`: The timestamp that a chargeback was issued against the payment, if there was one. If there is a chargeback timestamp, then we assume the payment was fraudulent. If there is no chargeback timestamp, then we assume this was a non-fraudulent payment.

### merchants.csv
Each row corresponds to a Merchant that processes payments. The columns are:
- `id`: The unique ID of the merchant.
- `country`: The country in which the merchant is located.
- `category`: The category of business that the mechant is in.

### buyers.csv
Each row corresponds to a buyer who makes a payment. The columns are:
- `id`: The unique ID of the buyer.
- `country`: The country in which the buyer is located.


## 1. Waiting For Chargebacks (25%)
In order to properly train and test a model, you must ensure that you're only using information to train the model that you would have at the time that you are predicting with the model. 

For the Fraud dataset, we assume that if there is no chargeback then the payment was not fraudulent. However, a payment for yesterday may have a chargeback tomorrow. This means that today I will think it's good, whereas tomorrow I'll know it's fraudulent. Using the dataset, determine how many days you must wait after a payment is processed in order to be sure that at least 95% of payments which _would have_ received a chargeback will have received a chargeback. 

Your script should read in the appropriate dataset(s) and print out the number of days.

## 2. Train / Test Split (25%)

This question involves thinking through how to construct a training and test set if you want to build an ML model to predict fraud. Remember, training and test sets should approximate real world scenarios as much as possible.

Imagine you train and deploy a model on the same day. You plan to collect a month's worth of _ground truth_ data in order to analyze the model's performance. Construct a training and test dataset based on this scenario. 

Using the payments data, construct a test set containing a month's worth of data and a training dataset containing as much data as possible. You should only use data in the training dataset that you would know the ground truth for at the time of the start of the test data. You can use your answer from part 1 help you determine which payments you would have solid ground truth for.

In your script, divide the payments up into training and test data and print out the start and end timestamp of each dataset.

## 3. Historical Features (25%)

For each payment, calculate the average fraud rate for the merchant and the buyer. If there are no prior transactions, then assume that the rate is zero. Note: your features should be calculated using only information that is known at the time of the transaction. 

In order to verify your answer, your script should print out the sum of average merchant fraud rates for all payments plus the sum of average buyer fraud rates for all payments.


## 4. Make a Model (25%)

For the final question, you should build an ML model to predict fraud. Your model should join together the payments, merchant, and buyer data and use the following features:

- payment_amount
- merchant category
- merchant country
- buyer country
- merchant fraud rate (from question 3)
- buyer fraud rate (from question 3)

Split your data up into training and test data using your answers from question 2, train a model on the training data, and evaluate the model's area under the ROC curve (AUC) on the test data. Print out the AUC at the end. You model will likely perform poorly, and that's ok! Fraud is hard.

