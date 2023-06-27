# Model Selection: 

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
| GAN           | 0.9955 | 706.8428 | 3.29% | 0.9651 | 731.9221| 2.30% |
| GRU           | 0.9971 | 666.0494 | 2.98% | 0.9738 | 651.7368| 2.04% |
| LSTM          | 0.9969 | 666.1824 | 3.00% | 0.9736 | 669.6527| 2.07% |
| ARIMA         | 0.9970 | 733.2738 | 2.8100% | -1.5391 | 21103.8951 | 79.7169% |

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

Phân tích results mẫu: 
As we can see, the performance of the statistical
models is the lowest. This is relatively easy to
understand because in this method we only use
the close price for forecasting, the model uses
much less information than others, so low per-
formance is inevitable.

Next to the linear methods, the method that we
see the best performance is LDA. We don’t have
time to analyze specifically what the reason is
here, but we will make an assumption that be-
cause our window normalization causes the fea-
ture distributions to move towards normal dis-
tributions. Most of the dimensions do not carry
many classification capabilities, so they satisfy
more applicable conditions than Logistic Regres-
sion or Support Vector Machine.
Regarding ensemble learning methods, we can
see the superiority of boosting, performance on
this set of methods is stronger than other mod-
els.
As for Deep Learning models, the performance is
at a good threshold. We think the performance
can be even better on GAN and LSTM but we
don’t have resources to tune the parameters nor
make the neural network more complicated to
see if the performance can be higher than boosting. 

In summary, we can see the superiority of boost-
ing over linear models (with very fast train-
ing times and very good performance). Deep
Learning has a good performance but the train-
ing time is really long and the tuning of the
parameters is also extremely resource-intensive

and time-consuming. Therefore, we will choose
LightGBM as a representative model for analy-
sis in the following sections.


