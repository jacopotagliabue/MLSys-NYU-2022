# MLSys-NYU-2022
Slides, scripts and materials for the Machine Learning in Finance Course at NYU Tandon, 2022.

## Overview

This repository contains the teaching materials by Prof. [Ethan Rosenthal](https://www.ethanrosenthal.com/) and [myself](https://jacopotagliabue.it/) for the 2022 course in ML at the NYU Tandon School of Engineering.

We open source slides, code snippets and even assignements after the class is completed, hoping to benefit the broader community of Machine Learning students and practitioners; I had a calculus book that said, "What one fool can do, another can.", and I wish more and more fools could become proficient at building reliable, trust-worthy, well-crafted ML systems.

We feel there are now enough books and YouTube videos for people interested purely in the theory of ML; moreover, practictioners produce a much bigger marginal value when bringing into the class their day-to-day experience, which, for the time being, cannot be as easily found on YouTube.

Therefore, the course we run is very practical and focuses on the intuitive understanding of ML problems and their solutions _through real-world tools_: we emphasize the importance of good coding habits, and the use of industry standard methodology, over complex modelling and formulas (alas, we do indeed sometime need to talk about math).

The whole course runs in 14 weeks, but we cover arguments that would keep you busy for a lifetime: every lecture, every slide, every code snippet are the result of many explicit and implicit trade-offs - what should we cover, what should we not? While this material cannot substitute for real-world interactions and our great sense of humour, we leave for the open source community to judge how useful the trade-offs we picked actually are.

### At a glance

### Repo structure

This year's repository is structured by week: each week has its folder, with a self-contained `README`, scripts / notebooks and slides. The choice results in some redundancy (especially in the second part, where the same training loop is used several times), but provides more clarity for students pacing themselves through the course, and highlight the highly modular nature of the syllabus. 

As part of the course, we emphasize the importance of virtual environments and submitting properly structured projects (notebooks are great, but we leave them for experimentation!). Each week contains a devoted `requirements.txt` file to make sure the scripts are reproducible.

### Changelog

Compared to [2021 edition](https://github.com/jacopotagliabue/FREE_7773), most material is indeed new and re-vamped. As a non-exhaustive list:

* new intro to Python / coding good practices;
* fraud detection as a finance-specific ML use case;
* NLP section has been replaced by a RecSys deep dive;
* new section on the importance of metrics, and expanded discussion on evaluating models;
* new tools: Metaflow sandbox and Streamlit apps.

## Tooling overview

### Intro to Python

TBC

### Metaflow

TBC

### Streamlit

TBC

### Comet

The file `comet_playground.py` is a simple adaptation of Comet onboarding script for sklearn: if run correctly, the Comet dashboard should start displaying experiments under the chosen project name.
 
Make sure to set `COMET_API_KEY` and `MY_PROJECT_NAME` as env variables before running the script.

### Flask

TBC

## Acknowledgments

Thanks to all outstanding people quoted and linked in the slides: this course is possible only because we truly stand on the shoulders of giants. Special thanks also to:

* Hugo;
* Chip;
* Gideon.

## Suggested complementary / additional readings

The main topics - Time Series, Fraud Detection, MLOps, RecSys etc. - are all huge, and we could obviously just scratch the surface. Aside from all the references to be found in the weeklys slides and READMEs, these are few good places to further explore this world.

### Modelling
* [Deep Learning with Python](https://www.amazon.com/Learning-Python-Second-Fran%C3%A7ois-Chollet/dp/1617296864): great practical intro to ML concepts and the basics of DL;

### MLOps
* [You Don't Need a Bigger Boat](https://github.com/jacopotagliabue/you-dont-need-a-bigger-boat): our own fully open source repository showing how state-of-the-art ML systems can be built at scale, component after component.

## Contacts

For questions, feedback, comments, please drop me a message at: `jacopo dot tagliabue at nyu.edu`.
