# Bitcoin Price Prediction: Multiple Linear Regression and XGBoost Regression
We explore two methodologies for predicting Bitcoin prices: Multiple Linear Regression and XGBoost Regression.

## Data Processing
Use BTC_tomorrow làm target cho X_today

Both methods utilize TimeSeriesSplit for data preprocessing to ensure the training set contains past data while the test set consists of future data. 

## Data Split
* NCuong: 2 phần train, test. Tập Train: TimeSeriesSplit để tìm parameters. Tìm xong cho gán vào test.

Split Data: Last 250 days for Test. 
Train set with GirdSearch and RandomizedSearch to find best parameters, and Test set for Test. (I don't split: Train, Valid, Test)

* Mỹ Linh chia 3 phần: train, val, test. 
- Tập Train: dùng TimeSeriesSplit để tìm parameters = Grid Search và Randomized Search. 
- Tập Train-Valid:  Tthử 3 bộ param: default_param, grid_param, random_param với test=VALID xem cái nào tốt nhất trong 3 cái. 
- Chọn cái tốt nhất để train lại với Train-Valid và Test.

## Multiple Linear Regression

Multiple Linear Regression involves using Gradient Descent, Stochastic Gradient Descent, or Normal Equation methods to determine optimal parameters. We use Lasso and Ridge Regression as regularization techniques to reduce overfitting, and Grid Search and Randomized Search for hyperparameter tuning.

Feature selection strategies are employed to improve model performance.

## XGBoost Regression

XGBoost is an ensemble learning method that combines multiple models to make more accurate predictions. 

We follow a similar approach to Multiple Linear Regression, utilizing hyperparameter tuning and feature selection techniques.

# Conclusion
By exploring different methodologies and fine-tuning our models, we aim to generate accurate predictions and insights into Bitcoin price movements.


1. Docs chung nhóm: https://docs.google.com/document/d/182xPZ3Ul8HCVh77qIRNY-pT9e0FyJfjZ3q-vUvjqqmw/edit

2. Report: https://www.overleaf.com/project/64929d030e8fe2041fb823c9

3. Slide môn: https://husteduvn-my.sharepoint.com/:f:/g/personal/cuong_dn210141_sis_hust_edu_vn/EjyViQMj-IhMnYp7spERuqsBS3kXXLunTQVHyOITwkJMpQ?e=I1o2MI