from sklearn.metrics import mean_squared_error,mean_absolute_percentage_error
import numpy as np
true_train=0
prediction_train=0
prediction_test=0
true_test=1
def AUC(true_test,prediction_test):
    count = 0
    for i in range(1,len(true_test)):
        if (true_test[i] - true_test[i-1]) * (prediction_test[i] - prediction_test[i-1]) > 0:
            count += 1
    return count/(len(true_test)-1)
print("Test accuracy for train set")
#RMSE
print("Root Mean Square Error (RMSE):", np.sqrt(mean_squared_error(true_train, prediction_train)))

#MAPE
print(" Mean Absolute Percentage Error (MAPE):", mean_absolute_percentage_error(true_train,prediction_train))
print("Test accuracy for test set")
#RMSE
print("Root Mean Square Error (RMSE):", np.sqrt(mean_squared_error(true_test, prediction_test)))

#MAPE
print(" Mean Absolute Percentage Error (MAPE):", mean_absolute_percentage_error(true_test,prediction_test))
#AUC
print("AUC test:",AUC(true_test,prediction_test))