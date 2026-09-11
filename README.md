#  Car Price Prediction System

## Project Overview

Buying or selling a car can be difficult because the price depends on many factors, such as the manufacturer, model, year, engine power, fuel type, transmission, vehicle size, mileage, and other specifications.

In this project, I built a machine learning regression system that predicts the estimated Manufacturer's Suggested Retail Price (MSRP) of a car based on its specifications.

The project includes a complete machine learning workflow, starting from data cleaning and analysis, followed by model training, evaluation, and deployment through a Streamlit web application.

The main purpose of this project is to understand how machine learning can be used to solve a real-world price prediction problem.

---

##  Project Objective

The objective of this project is to develop a machine learning model that can estimate a car's MSRP using information such as:

- Car manufacturer
- Car model
- Manufacturing year
- Engine fuel type
- Engine horsepower
- Number of engine cylinders
- Transmission type
- Driven wheels
- Number of doors
- Market category
- Vehicle size
- Vehicle style
- Highway MPG
- City MPG
- Popularity

The target variable is:

```text
MSRP (Manufacturer's suggested retail Price)



Dataset

The dataset contains information about different cars and their specifications.

Dataset details

Number of original records: 11,914

Number of columns: 16

Target column: MSRP

Problem type: Supervised Machine Learning - Regression

The dataset contains both:

Numerical features

Categorical features

Numerical features

Year

Engine HP

Engine Cylinders

Number of Doors

Highway MPG

City MPG

Popularity

Categorical features

Make

Model

Engine Fuel Type

Transmission Type

Driven Wheels

Market Category

Vehicle Size

Vehicle Style

 Project Workflow

The project follows these major steps:

Dataset
   ↓
Data Understanding
   ↓
Exploratory Data Analysis
   ↓
Data Cleaning
   ↓
Duplicate Removal
   ↓
Missing Value Handling
   ↓
Feature and Target Separation
   ↓
Train-Test Split
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Model Training
   ↓
Hyperparameter Tuning
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Deployment

 Data Cleaning and Preprocessing

The dataset was checked for:

Missing values

Duplicate records

Numerical and categorical columns

Unusual values

Distribution of the target variable

High-priced vehicles

Duplicate records were removed to avoid using repeated observations during model training.

Missing numerical values were handled using the median value of the respective column.

For example:

Missing Engine HP values were filled using the median Engine HP.

Missing Engine Cylinders values were filled using the median Engine Cylinders.

Missing Number of Doors values were filled using the median Number of Doors.

Missing values in categorical columns were handled using suitable replacements. For the Market Category column, missing values were replaced with:

Unknown

High-priced cars were inspected carefully. Some cars had very high MSRP values, but they represented genuine luxury or high-performance vehicles. Therefore, they were not removed simply because they appeared as statistical outliers.

 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the dataset and identify important patterns.

The analysis included:

Checking the structure of the dataset

Studying numerical statistics

Checking missing values

Finding duplicate records

Understanding the distribution of MSRP

Inspecting high-priced vehicles

Analyzing popular car manufacturers

Analyzing frequently occurring car models

The MSRP distribution was found to be right-skewed because most cars had moderate prices, while a smaller number of luxury and high-performance cars had very high prices.

 Machine Learning Approach

The dataset contains both numerical and categorical features. Therefore, preprocessing was required before training the models.

Numerical feature preprocessing

Numerical features were scaled so that features with larger numerical values would not dominate the model.

Categorical feature preprocessing

Categorical features were converted into numerical form using one-hot encoding.

Feature selection

Feature selection was applied after preprocessing to retain useful features and reduce unnecessary information before model training.

The preprocessing and feature selection objects were saved separately so that the same transformations could be applied when making predictions through the Streamlit application.

 Model Training

Different regression approaches were considered for predicting car prices.

The project includes a trained regression model that takes the car specifications as input and predicts the estimated MSRP.

The final saved model is:

car_price_model.pkl

The model is used together with the saved preprocessing and feature selection files.

📁 Project Files
car-price-prediction-system/
│
├── app.py
├── car_MSRP.csv
├── car_price_model.pkl
├── car_price_preprocessor.pkl
├── car_price_selector.pkl
├── Car Price Prediction System — MSRP Estimation.ipynb
└── README.md
File descriptions

File

	

Description




app.py

	

Streamlit application used to interact with the trained model




car_MSRP.csv

	

Dataset used for the project




car_price_model.pkl

	

Saved trained machine learning model




car_price_preprocessor.pkl

	

Saved preprocessing object for transforming input data




car_price_selector.pkl

	

Saved feature selection object




.ipynb

	

Complete notebook containing data analysis, preprocessing, training, and evaluation




README.md

	

Project documentation

 Streamlit Application

A Streamlit web application was created to make the prediction system easy to use.

The user can enter or select car specifications such as:

Make

Model

Year

Engine Fuel Type

Engine HP

Engine Cylinders

Transmission Type

Driven Wheels

Number of Doors

Market Category

Vehicle Size

Vehicle Style

Highway MPG

City MPG

Popularity

After clicking the Predict MSRP button, the application sends the entered information through the saved preprocessing and feature selection objects.

The trained model then predicts the estimated car price.

The result is displayed as:

Estimated MSRP: $XX,XXX.XX
 Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Streamlit

Joblib

Google Colab

GitHub

 How to Run the Project
1. Clone the repository
git clone https://github.com/HruthwikThota/car-price-prediction-system.git
2. Open the project folder
cd car-price-prediction-system
3. Install the required libraries
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
4. Run the Streamlit application
streamlit run app.py
5. Open the application

After running the command, Streamlit will provide a local URL similar to:

http://localhost:8501

Open this URL in a browser to use the application.

 What I Learned from This Project

Through this project, I learned how to:

Understand a real-world dataset

Identify numerical and categorical features

Handle missing values

Remove duplicate records

Perform exploratory data analysis

Prepare data for machine learning

Apply preprocessing using ColumnTransformer

Perform feature selection

Train a regression model

Evaluate a regression model

Save and reuse trained machine learning objects

Build a user interface using Streamlit

Upload and organize a project on GitHub

 Future Improvements

This project can be improved further by:

Comparing more regression algorithms

Improving model accuracy

Adding more detailed evaluation visualizations

Using additional vehicle-related features

Adding prediction confidence or an estimated price range

Deploying the Streamlit application online

Improving the user interface

Adding charts to explain the predicted price

 Author

Hruthwik Thota

This project was created as part of my machine learning learning journey to understand the complete process of building and deploying a regression-based application.


## How to edit it on GitHub

1. Open your repository.
2. Click **README.md**.
3. Click the **pencil/edit icon** near the top-right of the README.
4. Select all existing text and delete it.
5. Paste the complete README above.
6. Scroll down to **Commit changes**.
7. Use this commit message:

```text
Improve project README documentation

Select Commit directly to the main branch.

Click Commit changes.
