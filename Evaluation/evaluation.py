from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
import numpy as np

true_train = 0
prediction_train = 0
prediction_test = 1
true_test = 1

def calculate_acc(true_values, predicted_values):
    count = 0
    for i in range(1, len(true_values)):
        if (true_values[i] - true_values[i-1]) * (predicted_values[i] - predicted_values[i-1]) > 0:
            count += 1
    return count / (len(true_values) - 1)

def print_evaluation_results(true_values, predicted_values, dataset_name):
    print("Test ACCuracy for", dataset_name)
    print("------------------------------------------------------")
    # RMSE
    rmse = np.sqrt(mean_squared_error(true_values, predicted_values))
    print("Root Mean Square Error (RMSE): {:.4f}".format(rmse))
    
    # MAPE
    mape = mean_absolute_percentage_error(true_values, predicted_values)
    print("Mean Absolute Percentage Error (MAPE): {:.4f}".format(mape))
    
    # ACC
    acc = calculate_acc(true_values, predicted_values)
    print("ACC test: {:.4f}".format(acc))
    print()

# Print evaluation results for the train set
print_evaluation_results(true_train, prediction_train, "train set")

# Print evaluation results for the test set
print_evaluation_results(true_test, prediction_test, "test set")
