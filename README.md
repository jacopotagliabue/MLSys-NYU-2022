# MLSys-NYU-2022
Slides, scripts and materials for the Machine Learning in Finance Course at NYU Tandon, 2022.

## Overview

DISCLAIMER: A significant part of our course is class participation (this is why, in the end, we have universities and not *just* books and repos!), and no amount of scripts can provide the same level of educational content, or a comparable experience. Please note that this course changes substantially every year, so the best way to keep up to date with us is... by enrolling in the [Master](https://engineering.nyu.edu/academics/programs/financial-engineering-ms)!

This repository contains some of the teaching materials by Prof. [Ethan Rosenthal](https://www.ethanrosenthal.com/) and [myself](https://jacopotagliabue.it/) for the 2022 course in ML at the NYU Tandon School of Engineering.

We open source slides, code snippets and assignments after the class is completed, hoping to benefit the broader community of Machine Learning students and practitioners; I had a calculus book that said, "What one fool can do, another can.", and I wish more and more fools could become proficient at building reliable, trust-worthy, well-crafted ML systems.

We feel there are now enough books and YouTube videos for people interested purely in the theory of ML; moreover, practitioners produce a much bigger marginal value when bringing into the class their day-to-day experience, which, for the time being, cannot be as easily found on YouTube.

Therefore, the course we run is very practical and focuses on the intuitive understanding of ML problems and their solutions _through real-world tools_: we emphasize the importance of good coding habits, and the use of industry standard methodology, over complex modelling and formulas (alas, we do indeed sometimes need to talk about math).

The whole course runs in 14 weeks, but we cover arguments that would keep you busy for a lifetime: every lecture, every slide, every code snippet are the result of many explicit and implicit trade-offs - what should we cover, what should we not? While no material can substitute for real-world interactions and our great sense of humour, we leave for the open source community to judge how useful the trade-offs we picked actually are.

## At a glance

### Repo structure

This year's repository is structured by week: each week has its folder, with a self-contained `README`, scripts / notebooks and slides. The choice results in some redundancy (especially in the second part, where the same training loop is used several times), but provides more clarity for students pacing themselves through the course, and highlights the highly modular nature of the syllabus. 

As part of the course, we emphasize the importance of virtual environments and submitting properly structured projects (notebooks are great, but we leave them for experimentation!). Each week contains a devoted `requirements.txt` file to make sure the scripts are reproducible.

### Changelog

Compared to [2021 edition](https://github.com/jacopotagliabue/FREE_7773), most material is indeed new and re-vamped. As a non-exhaustive list:

* new intro to Python / coding good practices;
* fraud detection as a finance-specific ML use case;
* NLP section has been replaced by a RecSys deep dive;
* new section on the importance of metrics, and expanded discussion on evaluating models;
* new tools: Metaflow sandbox and Streamlit apps.

## Tooling overview

### Intro to Python and Git

Python is the main language for Machine Learning, but it is surprisingly hard to set up a [working environment](https://calmcode.io/virtualenv/intro.html). We introduce virtualenv and basics of git to get you started.

#### Metaflow

[Metaflow](https://metaflow.org/) is an open-source tool designed to simplify building, maintaining and deploying ML pipelines (e.g. [here](https://github.com/jacopotagliabue/you-dont-need-a-bigger-boat)). Starting this year, Outerbounds provided us with free [sandbox accounts](https://outerbounds.com/docs/sandbox/) (thank you!).

#### Streamlit

[Streamlit](https://streamlit.io/) turns Python scripts into web apps in minutes, helping with prototyping and sharing the results of our pipelines. Streamlit apps can be used to display artifacts from Metaflow, and [make the model interactive for non-technical stakeholders](https://github.com/jacopotagliabue/MLSys-NYU-2022/blob/main/weeks/10/app/app.py).

#### Comet

[Comet](https://www.comet.com/site/) is a machine learning platform that can help you manage, visualize, and optimize training runs. We use Comet to keep track of our experiments, and document our progress with the rest of our team and technical stakeholders (thank you for the free account!).

#### Flask

[Flask](https://flask.palletsprojects.com/en/2.2.x/) is a micro web framework written in Python. It allows us to build (in Python) APIs that serve predictions made by our trained model *in real-time*, and display the results in the browser.

## Acknowledgments

Thanks to all outstanding people quoted and linked in the slides: this course is possible only because we truly stand on the shoulders of giants. Special thanks also to:

* [Hugo](https://www.linkedin.com/in/hugo-bowne-anderson-045939a5/) for being our fantastic guest speaker on Metaflow;
* [Chip](https://www.linkedin.com/in/chiphuyen/) for being our fantastic guest speaker on MLOps;
* [Ciro](https://www.linkedin.com/in/cirogreco/) for being our fantastic guest speaker on industry applications of ML and ML careers;
* [Gideon](https://www.linkedin.com/in/gideon-mendels/) for fantastic support and free Comet accounts for all the students.

## Suggested complementary / additional readings

The main topics - Regression, Classification, Time Series, Fraud Detection, MLOps, RecSys etc. - are all huge, and we could obviously just scratch the surface. Aside from all the references to be found in the slides and READMEs, these are few good places to further explore this world.

### Machine Learning
* [Deep Learning with Python](https://www.amazon.com/Learning-Python-Second-Fran%C3%A7ois-Chollet/dp/1617296864): great practical intro to ML concepts and the basics of DL using Keras.

* [Machine Learning with PyTorch and Scikit-Learn](https://www.amazon.com/Machine-Learning-PyTorch-Scikit-Learn-learning-ebook/dp/B09NW48MR1): another great practical intro to ML / DL, focused on PyTorch.

* [RecList](https://github.com/jacopotagliabue/reclist): our own open source project (library, paper, tutorials) for better testing of recommender systems.

### MLOps
* [Designing Machine Learning Systems: An Iterative Process for Production-Ready Applications](https://www.amazon.com/Designing-Machine-Learning-Systems-Production-Ready/dp/1098107969): a book by Chip Huyen on how machine learning systems are designed, end to end - excellent introduction to basic MLOps concepts.

* [Effective Data Science Infrastructure](https://www.manning.com/books/effective-data-science-infrastructure): a book by Ville Tuulos - Metaflow creator - on how to make data scientist productive.

* [You Don't Need a Bigger Boat](https://github.com/jacopotagliabue/you-dont-need-a-bigger-boat): our own fully open source repository showing how state-of-the-art ML systems can be built at scale, component after component.

* [Comet for Data Science](https://www.packtpub.com/product/comet-for-data-science/9781801814430): on how to take advantage of existing platform for experiment tracking, collaboration and managing the life-cycle of ML artifacts.

## Contacts

For questions, feedback, comments, please drop me a message at: `jacopo dot tagliabue at nyu.edu`.
