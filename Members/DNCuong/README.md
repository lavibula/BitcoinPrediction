# Bitcoin Price Prediction: Multiple Linear Regression and XGBoost Regression
We explore two methodologies for predicting Bitcoin prices: Multiple Linear Regression and XGBoost Regression.

## Data Processing

Both methods utilize TimeSeriesSplit for data preprocessing to ensure the training set contains past data while the test set consists of future data. 

## Multiple Linear Regression

Multiple Linear Regression involves using Gradient Descent, Stochastic Gradient Descent, or Normal Equation methods to determine optimal parameters. We use Lasso and Ridge Regression as regularization techniques to reduce overfitting, and Grid Search and Randomized Search for hyperparameter tuning.

Feature selection strategies are employed to improve model performance.

## XGBoost Regression

XGBoost is an ensemble learning method that combines multiple models to make more accurate predictions. 

We follow a similar approach to Multiple Linear Regression, utilizing hyperparameter tuning and feature selection techniques.

# Conclusion
By exploring different methodologies and fine-tuning our models, we aim to generate accurate predictions and insights into Bitcoin price movements.