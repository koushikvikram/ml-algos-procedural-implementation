"""
Algorithm Evaluation Methods
- train-test split
- k-fold cross validation split
"""

from math import floor
from random import shuffle, seed
from typing import List, Tuple


# define methods for validation
def train_test_split(dataset: List[List], split: float = 0.7) -> Tuple[List, List]:
    """
    shuffles dataset, splits into training and test set
    training set is split% of entire dataset
    """
    row_indices = list(range(len(dataset)))
    shuffle(row_indices)
    train_final_index = int(floor(split*len(dataset)))
    train_indices, test_indices = row_indices[:train_final_index], row_indices[train_final_index:]
    train_set = [value for index, value in enumerate(dataset) if index in train_indices]
    test_set = [value for index, value in enumerate(dataset) if index in test_indices]
    return train_set, test_set


def cross_validation_split(dataset: List[List], k: int = 3) -> List[List[List]]:
    """
    shuffles dataset, splits into 'k' eaual parts
    """
    shuffle(dataset)
    split_dataset = list()
    multiplication_factor: int = len(dataset)//k
    split_points: range = [multiplication_factor*m for m in range(k)]
    for index in split_points:
        start: int = index
        end: int = index + multiplication_factor
        split_dataset.append(dataset[start:end])
    return split_dataset


seed(1)
sample_ds = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10],
             [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]
train, test = train_test_split(sample_ds)
print("Training set: {}".format(train))
print("Test set: {}".format(test))

print("\nCross validation split with k=3:\n{}\n".format(cross_validation_split(sample_ds)))
