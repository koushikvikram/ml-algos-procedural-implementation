"""
Models used to establish baseline performance on a predictive algorithm.
Provides a point of comparison for evaluating more advanced algorithms.
- Random Prediction Algorithm
- Zero Rule Algorithm
For both these models, it doesn't matter what the test data is.
"""

from typing import List
from random import choice, seed


def random_algorithm(train: List, test: List) -> List:
    """
    - returns a list of random predictions for the test set
    - works for both regression and classification
    """
    possible_predictions: List = list(set(row[-1] for row in train))
    predicted_values: List = [choice(possible_predictions) for i in range(len(test))]
    return predicted_values


def zero_rule_algorithm_classification(train: List, test: List) -> List:
    """
    - calculates the most frequently occurring class in the train set
    - predicts this value for all observations in the test set
    """
    train_outputs: List = [row[-1] for row in train]
    prediction: int = max(train_outputs, key=train_outputs.count)
    predicted_values: List = [prediction for i in range(len(test))]
    return predicted_values


def zero_rule_algorithm_regression(train: List, test: List) -> List:
    """
    - a good default prediction for real values is the central tendency (mean)
    - calculates the mean of output values in the training data
    - predicts this value for all observations in the test set
    """
    train_outputs: List = [row[-1] for row in train]
    # calculate the mean of train_outputs and assign to prediction
    prediction: float = sum(train_outputs)/float(len(train_outputs))
    predicted_values: List = [prediction for i in range(len(test))]
    return predicted_values


seed(1)
train_set: List = [[0], [1], [1], [1], [0], [1]]
test_set: List = [[None], [None], [None], [None], [None], [None]]

train_reg: List = [[10], [15], [12], [15], [18], [20]]
test_reg: List = [[None], [None], [None], [None], [None], [None]]

random_predictions: List = random_algorithm(train_set, test_set)
zero_rule_classification_predictions: List = zero_rule_algorithm_classification(train_set, test_set)
zero_rule_regression_predictions: List = zero_rule_algorithm_regression(train_reg, test_reg)

print("Predictions from random algorithm: {}".format(random_predictions))
print("Predictions from zero rule classification algorithm: {}"
      .format(zero_rule_classification_predictions))
print("Predictions from zero rule regression algorithm: {}"
      .format(zero_rule_regression_predictions))
