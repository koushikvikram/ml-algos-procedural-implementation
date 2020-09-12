"""
evaluation metrics for machine learning algorithms
- accuracy = (correct predictions / total predictions) * 100
- confusion matrix
- mean absolute error = i=1 to n, summation(abs(predicted_i - actual_i))
                        / total predictions
- root mean squared error = sqrt(i=1 to n, summation(abs(predicted_i - actual_i)**2)
                            / total predictions)
"""

from typing import List
from math import sqrt


def accuracy(actual: List, predicted: List) -> float:
    """
    calculates the accuracy of predictions
    """
    num_correct: int = 0
    num_predictions: int = len(actual)
    for i in range(num_predictions):
        if predicted[i] == actual[i]:
            num_correct += 1
    return num_correct/float(num_predictions) * 100


def num_pair_occurrence(pair: tuple, actual: List, predicted: List) -> int:
    """
    get the count of first element in pair occurring in actual
    and second element of pair occurring in predicted
    """
    count: int = 0
    for i, expected in enumerate(actual):
        if expected == pair[0] and predicted[i] == pair[1]:
            count += 1
    return count


def confusion_matrix(actual: List, predicted: List) -> tuple:
    """
    returns the set of unique values as well as the confusion matrix
    """
    unique: set = set(actual)
    matrix: List = list()
    for i in unique:
        row: List = list()
        for j in unique:
            row.append(num_pair_occurrence((i, j), actual, predicted))
        matrix.append(row)
    return unique, matrix


def print_confusion_matrix(unique: set, matrix: List) -> None:
    """
    Pretty prints confusion matrix - works for binary classification
    """
    print("(P)" + " ".join(str(value) for value in unique))
    print("(A)---")
    for i, value in enumerate(unique):
        print("{}| {}".format(value, ' '.join(str(value) for value in matrix[i])))


def mae_metric(actual: List, predicted: List) -> float:
    """
    returns the mean absolute error
    """
    num_predictions: int = len(predicted)
    total_abs_error: float = sum(abs(predicted[i]-actual[i]) for i in range(num_predictions))
    return total_abs_error/float(num_predictions)


def rmse_metric(actual: List, predicted: List) -> float:
    """
    returns the root mean squared error
    """
    num_predictions: int = len(predicted)
    total_squared_error: float = sum((predicted[i]-actual[i])**2 for i in range(num_predictions))
    return sqrt(total_squared_error/float(num_predictions))


y: List = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_hat: List = [0, 1, 0, 0, 0, 1, 0, 1, 1, 1]

y_reg = [0.1, 0.2, 0.3, 0.4, 0.5]
y_reg_hat = [0.11, 0.19, 0.29, 0.41, 0.5]

unique_values, conf_matrix = confusion_matrix(y, y_hat)

print("Accuracy: {}".format(accuracy(y, y_hat)))
print_confusion_matrix(unique_values, conf_matrix)
print("MAE: {}".format(mae_metric(y_reg, y_reg_hat)))
print("RMSE: {}".format(rmse_metric(y_reg, y_reg_hat)))
