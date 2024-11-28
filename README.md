# 🩺 Early Stage Diabetes Prediction

> Powered by Machine Learning algorithms, simple web-app to help find early stage diabetes prediction.\
> Check out the app @ https://diabetes-classifier-qech.onrender.com

Using the power of three different machine learning classifiers, this website can help predict early stage diabetes.\
This project was designed and built during Software Engineering Semiar course, and was my first project in the realm of Machine Learning.

You can find the full seminar report (in Hebrew) at this  [`link`](https://drive.google.com/file/d/1WowPZkZfueunARCpy79JBXzuzU8cpo8v/view).

The models used in this projects are: [`Perceptron`](https://en.wikipedia.org/wiki/Perceptron), [`Multilayer Perceptron`](https://en.wikipedia.org/wiki/Multilayer_perceptron) and [`Decision Tree`](https://en.wikipedia.org/wiki/Decision_tree).\
The database used to train the models was taken from [`Kaggle`](https://www.kaggle.com/) and can be found [here](https://www.kaggle.com/ishandutta/early-stage-diabetes-risk-prediction-dataset).

The project is written in [`Python`](https://www.python.org/) with the website powered by [`Flask`](https://flask.palletsprojects.com/).\
The models object is taken from the [`scikit-learn`](https://scikit-learn.org/) library.

The web app is hosted on [`heruko`](https://www.heroku.com/).\
**Please note that when first loading the website it may take up to 30 seconds to load due to heruko free-tier hosting service.*

# How to run locally
To run the web app on your machine, clone this repo `https://github.com/birkagal/diabetes-classifier.git`

Open terminal window at the project directory an run 

    python app.py

The website would be available at [`https://localhost:5000`](https://localhost:5000/)

![enter image description here](https://i.ibb.co/WffSRvV/1.png)

# TODO

 - [ ] Fix decision tree problem caused on heruko. (Currently decision tree is disabled.)


# Project Background

There are more than 450,000 diabetics living in Israel who are treated with medication.  
according to estimates by the National Diabetes Council there are another 200,000 people with undiagnosed and untreated diabetes.  
Diagnosis of diabetes is important to treat the disease and prevent the complications associated with diabetes.

##	How To Use

To use the website, answer **ALL** of the following questions. The answers will be used in a Machine Learning model I created  
and the result would appear on screen.

# ‼️ IMPORTANT ‼️

PLEASE NOTE!:  This site is used for learning porpusus only  
and if you think you have diabetes,  
PLEASE SEEK PROFFESIONAL DOCTOR.

## Meta
Gal Birka - birkagal@gmail.com\
Distributed under MIT License. See LICENSE for more information.
