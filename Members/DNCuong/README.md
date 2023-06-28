# Bitcoin Price Prediction: Multiple Linear Regression and XGBoost Regression
We explore two methodologies for predicting Bitcoin prices: Multiple Linear Regression and XGBoost Regression.

## Data Processing
Use BTC_close_tomorrow -> y (Target col) of X_today, BTC_close_today -> 1 feature in X_today.

Both methods utilize TimeSeriesSplit for data preprocessing to ensure the training set contains past data while the test set consists of future data. 

## Data Split
* 2 sets: Train set and Test set. (Last 250 days or 20% for Test). 
    - Train set: TimeSeriesSplit with GirdSearch and RandomizedSearch to find best parameters,
    - and Test set for Test. 

* 3 sets: Train, Val, Test set. 
    - Train set: TimeSeriesSplit with GirdSearch and RandomizedSearch to find best parameters
    - Train-Valid: Use default_param, grid_param, random_param với (train, test) = (Train set, Test set)
    - Test set: (train, test) = (Train&Val set, Test set) with best_param from (default_param, grid_param, random_param)

## Multiple Linear Regression

Multiple Linear Regression involves using Gradient Descent, Stochastic Gradient Descent, or Normal Equation methods to determine optimal parameters. We use Lasso and Ridge Regression as regularization techniques to reduce overfitting, and Grid Search and Randomized Search for hyperparameter tuning.

Feature selection strategies are employed to improve model performance.

## XGBoost Regression

XGBoost is an ensemble learning method that combines multiple models to make more accurate predictions. 

We follow a similar approach to Multiple Linear Regression, utilizing hyperparameter tuning and feature selection techniques.

# Conclusion
By exploring different methodologies and fine-tuning our models, we aim to generate accurate predictions and insights into Bitcoin price movements.

# Other folders: 
Data Collection Reference, Model Reference, Model Selection Reference

1. Docs chung nhóm: https://docs.google.com/document/d/182xPZ3Ul8HCVh77qIRNY-pT9e0FyJfjZ3q-vUvjqqmw/edit

https://docs.google.com/spreadsheets/d/13-slQv1toeaVKcFM22S9Gb3xPj_X6Apepwmo5fB2m3g/edit?fbclid=IwAR2CFOG6um7NPJV-XwjZdTG1Euw4O7ffYsLY3caSI13j9AE-I4fW0SUfYoA#gid=0

2. Slide presentation: https://husteduvn-my.sharepoint.com/:p:/g/personal/long_nt214912_sis_hust_edu_vn/EXSW7cVBIq5Ehq2eFumxmZcBCyFzr-r2po3W3sX6H4lHCg?e=LXxbMS&nav=eyJzSWQiOjI1Nn0&fbclid=IwAR1zg4_utqa4-VloCUNVgUXiNNpcQhC_PzqUi0Fh4XbqPxtzX_-zxO8qomM

3. Report: https://www.overleaf.com/project/64929d030e8fe2041fb823c9

4. Slide môn học thầy Khoát: https://husteduvn-my.sharepoint.com/:f:/g/personal/cuong_dn210141_sis_hust_edu_vn/EjyViQMj-IhMnYp7spERuqsBS3kXXLunTQVHyOITwkJMpQ?e=I1o2MI

