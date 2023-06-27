# Model Selection: 

General performance summary table of models: 

|           |Train Set| Train Set|Train Set|Test Set|Test Set|Test Set|
|-----------|-------|----------|---------|-------|----------|---------|
| **Model**| **R2** | **RMSE** | **MAPE%**   | **R2**    | **RMSE**    | **MAPE%**  |
| Linear Regression | 0.9965 | 799.3932 | 4.3926  | 0.9898 | 1339.5982 | 2.9076 |
| SVM          | 0.9968 | 985.0937 | 3.3692% | 0.9611 | 831.7924 | 2.6539% |
| KNN   | --- | --- | --- | 0.9113 | 1256.7745 | 4.0181% |
| Random Forest    | --- | 33.5004 | 0.0802% | 0.9897 | 430.0638| 1.3385% |
| Adaboost          | 0.9924 | 1508.1469 | 77.2415% | 0.7346 | 2173.5470| 75.3318% | 
| XGBoost           | 0.9970 | 925.0439 | 2.9174% | 0.9501 | 1015.8001| 3.5157% |
| LightGBM           | --- | 549.2033 | 1.2529% | 0.9640 |805.4951| 2.4725% |
| ARIMA         | 0.9970 | 733.2738 | 2.8100% | -1.5391 | 21103.8951 | 79.7169% |
| GAN           | 0.9955 | 706.8428 | 3.29% | 0.9651 | 731.9221| 2.30% |
| GRU           | 0.9971 | 666.0494 | 2.98% | 0.9738 | 651.7368| 2.04% |
| LSTM          | 0.9969 | 666.1824 | 3.00% | 0.9736 | 669.6527| 2.07% |


SORT ACCORDING **R2_TEST**: 

|           |Train Set| Train Set|Train Set|Test Set|Test Set|Test Set|
|-----------|-------|----------|---------|-------|----------|---------|
| **Model**| **R2** | **RMSE** | **MAPE%**   | **R2**    | **RMSE**    | **MAPE%**  |
| Linear Regression | 0.9965 | 799.3932 | 4.3926  | 0.9898 | 1339.5982 | 2.9076 |
| Random Forest    | --- | 33.5004 | 0.0802% | 0.9897 | 430.0638| 1.3385% |
| GRU           | 0.9971 | 666.0494 | 2.98% | 0.9738 | 651.7368| 2.04% |
| LSTM          | 0.9969 | 666.1824 | 3.00% | 0.9736 | 669.6527| 2.07% |
| GAN           | 0.9955 | 706.8428 | 3.29% | 0.9651 | 731.9221| 2.30% |
| LightGBM           | --- | 549.2033 | 1.2529% | 0.9640 |805.4951| 2.4725% |
| SVM          | 0.9968 | 985.0937 | 3.3692% | 0.9611 | 831.7924 | 2.6539% |
| XGBoost           | 0.9970 | 925.0439 | 2.9174% | 0.9501 | 1015.8001| 3.5157% |
| KNN   | --- | --- | --- | 0.9113 | 1256.7745 | 4.0181% |
| Adaboost          | 0.9924 | 1508.1469 | 77.2415% | 0.7346 | 2173.5470| 75.3318% | 
| ARIMA         | 0.9970 | 733.2738 | 2.8100% | -1.5391 | 21103.8951 | 79.7169% |


Analyze the performance results of the models *BITCOIN PRICE PREDICTION*

**Overall**

From the analysis, it can be observed that several models exhibit good performance in predicting Bitcoin prices. The top-performing models include Linear Regression, Random Forest, GRU, LSTM, GAN, and LightGBM, which demonstrate high R2 values on both the training and test sets. Additionally, these models exhibit low RMSE values and MAPE% on the test set, indicating accurate predictions with minimal error.

On the other hand, KNN, Adaboost, and ARIMA models display lower effectiveness compared to other models. These models exhibit lower R2 values on the test set and higher error metrics, particularly Adaboost and ARIMA, which demonstrate significantly higher MAPE% values on the test set.

**Analyzing the different types of models used**

1. The statistical model ARIMA shows the lowest performance. This can be attributed to the fact that this method utilizes less information compared to other approaches, leading to lower performance.

2. Machine learning models, such as Linear Regression, demonstrate good performance. It can be hypothesized that this is due to good data normalization and the presence of linear relationships between various economic and market factors. On the other hand, KNN and SVM do not perform as well.

3. Ensemble Learning models including Bagging methods like Random Forest and Boosting methods like AdaBoost, CatBoost, XGBoost and LightGBM did not show significantly high performance except for the Random Forest method.

4. The Deep Learning model demonstrates good performance at a high level, and there is still room for improvement. However, due to time and resource limitations, we were unable to adjust the parameters or create more complex neural networks to maximize the model's performance. 

**In summary**

In summary, the analysis reveals the superiority of linear methods, such as Linear Regression and Random Forest, compared to other models in terms of training time and overall performance. Deep learning models exhibit good performance and have the potential for further improvement, but they require longer training times and resource-intensive parameter tuning.