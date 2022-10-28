## End-to-End Machine Learning Project- Mechanical Properties Prediction for Low Alloy Steels using Machine Learning

<img target="_blank" src="https://github.com/dipakml/Mechanical-Properties-Prediction-for-Low-Alloy-Steels/blob/master/images/mech_img.png" width=1000>

### Table of Content
  * [Overview](#overview)
  * [Dataset Information](#dataset)
  * [Motivation](#motivation)
  * [Demo](#demo)
  * [Steps in the project execution](#Learning-Objective)
  * [Technical Aspect](#technical-aspect)
  * [Technologies Used](#technologies-used)
  * [Installation](#installation)
  * [Note](#note)



### Overview 

To finalize the material for an engineering product or application, it is important to understand the mechanical properties of the material. The mechanical properties of a material affect the mechanical strength and ability of a material to be molded in suitable shape. 
To obtain the mechanical properties of metals, designers, manufacturers and researchers have to rely on results obtained from the experiments that are conducted in testing laboratory. 
So, to obtain the desired properties for a material they need to customize composition of material and process parameters of the material prior of conducting the experiment. 
But these procedures demand massive expenditure and time to obtain the properties of materials. 
In case of Steels, Universal Tensile Testing Machine (UTM) is used for testing the steels and determining mechanical properties of steel like tensile strength, yield strength, etc. But when the material has to be tested at elevated temperatures it consumes more time to figure out the properties of material. 
In this project, we shall use available dataset which has chemical composition, temperature & various mechanical properties of low carbon steel. 
We shall prepare & train the machine learning model using different algorithms & develop a method to predict the various mechanical properties like 0.2% offset proof stress, tensile strength, %Elongation & % reduction in area. 
We will develop a web based application in which we shall input the chemical composition of steel and working temperature & it will predict the four properties as mentioned earlier.



### Dataset Information

The dataset describes chemical composition of low carbon steel which mentions the content of C, Si, P, Mn, S etc and various operating temperatures & corresponding mechanical properties. 
We have 15 independent variables & one target variable i.e. the mechanical property to predict.
Dataset used in this project is taken from here : [Dataset] (https://mits.nims.go.jp/en/)


### Motivation

Obtaining mechanical proerties is a tedious task which requires lots of manual efforts & has huge cost associated with it.
The motivation for working on this project was to use machine learning experiments to adress this challenge.

Idea is to implement the end to end machine learning project while using free deployment platform like Heroku.



### Demo
[Visit this link for live demo]( https://mechpropspred7.herokuapp.com/)

Web application Snapshot:

<img target="_blank" src="https://github.com/dipakml/Mechanical-Properties-Prediction-for-Low-Alloy-Steels/blob/master/images/webapp_snapshot.png" width=700>



### Steps in the project execution

<img target="_blank" src="https://github.com/dipakml/Mechanical-Properties-Prediction-for-Low-Alloy-Steels/blob/master/images/0_V0GyOt3LoDVfY7y5.png" width=700>

- Data Collection 
- Descriptive Analysis 
- Data Visualizations 
- Data Preprocessing 
- Data Modelling 
- Model Evaluation 
- Model Deployment 

### Technical Aspect 

- Training a machine learning model using scikit-learn. 
- Building and hosting a streamlit web app on Heroku. 
- A user has to input key features(Chemicalcomposition of steel).
- Once it gets all the fields information , the prediction is displayed. 


### Technologies Used  
![](https://forthebadge.com/images/badges/made-with-python.svg) 

<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/streamlit.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/heroku.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/numpy.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/pandas.jpeg" width=160>

### Installation 
- Clone this repository and unzip it.
- After downloading, cd into the working directory.
- Begin a new virtual environment with Python 3 and activate it.
- Install the required packages using pip install -r requirements.txt
- Execute the command: streamlit run app.py


### Note:
- Webapp can handle concurrency upto some extent but can be scaled.

