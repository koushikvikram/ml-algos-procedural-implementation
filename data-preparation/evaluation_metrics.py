"""
Evaluation metrics for machine learning algorithms.
- Accuracy = (correct predictions / total predictions) * 100
- Confusion Matrix
- Mean Absolute Error = i=1 to n, summation(abs(predicted_i - actual_i))
                        / total predictions
- Root Mean Squared Error = sqrt(i=1 to n, summation(abs(predicted_i - actual_i)**2)
                            / total predictions)
"""

from typing import List, Tuple
from math import sqrt


def accuracy(actual: List, predicted: List) -> float:
    """
    accuracy = % of correct predictions
    """
    num_correct: int = 0
    num_predictions: int = len(actual)
    for i in range(num_predictions):
        if predicted[i] == actual[i]:
            num_correct += 1
    return num_correct/float(num_predictions) * 100


def num_pair_occurrence(pair: Tuple[int, int], actual: List, predicted: List) -> int:
    """
    number of times pair[0], pair[1] occur in actual and predicted respectively
    """
    count: int = 0
    for i, expected in enumerate(actual):
        if expected == pair[0] and predicted[i] == pair[1]:
            count += 1
    return count


def confusion_matrix(actual: List, predicted: List) -> Tuple[set, List[List]]:
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
    error = predicted value - actual value
    absolute error = absolute(error)
    total absolute error = sum(absolute error) for all predictions
    mean absolute error = total absolute error / number of predictions
    """
    num_predictions: int = len(predicted)
    total_abs_error: float = sum(abs(predicted[i]-actual[i]) for i in range(num_predictions))
    return total_abs_error/float(num_predictions)


def rmse_metric(actual: List, predicted: List) -> float:
    """
    error = predicted - actual
    squared error = error^2
    total squared error = sum(squared error) for all predictions
    mean squared error = total squared error / number of predictions
    root mean squared error = sqrt(mean squared error)
    """
    num_predictions: int = len(predicted)
    total_squared_error: float = sum((predicted[i]-actual[i])**2 for i in range(num_predictions))
    return sqrt(total_squared_error/float(num_predictions))


y: List = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_hat: List = [0, 1, 0, 0, 0, 1, 0, 1, 1, 1]

y_reg: List = [0.1, 0.2, 0.3, 0.4, 0.5]
y_reg_hat: List = [0.11, 0.19, 0.29, 0.41, 0.5]

unique_values, conf_matrix = confusion_matrix(y, y_hat)

print("Accuracy: {}".format(accuracy(y, y_hat)))
print_confusion_matrix(unique_values, conf_matrix)
print("MAE: {}".format(mae_metric(y_reg, y_reg_hat)))
print("RMSE: {}".format(rmse_metric(y_reg, y_reg_hat)))
