"""
Rescaling data - normalization and standardization
"""

from typing import List, Tuple, Dict
from csv import reader
from math import sqrt


# functions for rescaling features
def get_dataset_minmax(dataset: List[List], columns_list=True) -> Dict[int, Tuple[float, float]]:
    """
    get the minimum and maximum values of the specified columns in the dataset
    if columns_list is not specified, get minimum and maximum for all columns
    """
    minmax = dict()
    if columns_list:
        # choose all columns
        column_indices = range(len(dataset[0]))
    else:
        # choose only the specified columns
        column_indices = columns_list
    for col_index in column_indices:
        col_values = [row[col_index] for row in dataset]
        col_min = min(col_values)
        col_max = max(col_values)
        minmax[col_index] = (col_min, col_max)
    return minmax


def norm(value: float, minimum: int, maximum: int) -> float:
    """
    return the norm of the value
    """
    return (value-minimum) / (maximum-minimum)


def normalize_dataset(dataset: List[List], columns_list=True) -> None:
    """
    normalize the columns in the dataset
    """
    minmax_lookup: Dict[int, Tuple[float, float]] = get_dataset_minmax(dataset, columns_list)
    if columns_list:
        # choose all columns
        column_indices = range(len(dataset[0]))
    else:
        # choose only the specified columns
        column_indices = columns_list
    for row in dataset:
        for col_index in column_indices:
            col_value: int = row[col_index]
            col_min: float = minmax_lookup[col_index][0]
            col_max: float = minmax_lookup[col_index][1]

            row[col_index]: float = norm(col_value, col_min, col_max)


def get_mean_std_dataset(dataset: List[List], columns_list=True) -> Dict[int, Tuple[float, float]]:
    """
    get the mean and standard deviation of the specified columns in the dataset
    if columns_list is not specified, get for all columns
    """
    mean_std = dict()
    if columns_list:
        # choose all columns
        column_indices = range(len(dataset[0]))
    else:
        column_indices = columns_list
    for col_index in column_indices:
        col_values: List = [row[col_index] for row in dataset]
        num_values: float = float(len(col_values))
        col_mean: float = sum(col_values) / num_values
        col_std: float = sqrt(sum((x-col_mean)**2 for x in col_values) / num_values)
        mean_std[col_index]: Tuple[float, float] = (col_mean, col_std)
    return mean_std


def standardize_value(value: float, mean: float, std_deviation: float) -> float:
    """
    Standardize the value with respect to it's column and return it
    """
    return (value - mean) / (std_deviation)


def standardize_dataset(dataset: List[List], columns_list=True) -> None:
    """
    standardize the columns in the dataset
    """
    mean_std_lookup: Dict[int, Tuple[float, float]] = get_mean_std_dataset(dataset, columns_list)
    if columns_list:
        # choose all columns
        column_indices = range(len(dataset[0]))
    else:
        # choose only the specified columns
        column_indices = columns_list
    for row in dataset:
        for col_index in column_indices:
            col_value: float = row[col_index]
            col_mean: float = mean_std_lookup[col_index][0]
            col_std: float = mean_std_lookup[col_index][1]

            row[col_index]: float = standardize_value(col_value, col_mean, col_std)


# Define functions for loading data
def load_csv(filename: str) -> List[List]:
    """
    Loads the csv file and returns a list of lists
    """
    dataset: List = list()
    with open(filename, "r") as file:
        csv_reader: reader = reader(file)
        for row in csv_reader:
            # skip empty rows
            if not row:
                continue
            dataset.append(row)
    return dataset


# Define functions for pre-processing data
def str_column_to_float(dataset: List[List], column_index: int) -> None:
    """
    Convert the entire column inplace in the dataset from string to float
    """
    for row in dataset:
        row[column_index] = float(row[column_index].strip())


# ---- load the dataset and explore a sample ----
filepath: str = "../datasets/pima-indians-diabetes.csv"
data: List[List] = load_csv(filepath)
print("\n[INFO] Loaded dataset '{}' with {} rows and {} columns\n"
      .format(filepath.split("/")[-1], len(data), len(data[0])))
print("Sample row from dataset:\n{}\n".format(data[0]))


# ---- pre-process the dataset ----
# convert all columns from string to float
for index in range(len(data[0])):
    str_column_to_float(data, index)
print("Sample row from dataset after datatype conversion:\n{}\n".format(data[0]))


# ---- normalize all columns in the dataset ----
normalize_dataset(data)
print("Sample row from dataset after normalization:\n{}\n".format(data[0]))


# load dataset again, preprocess and standardize columns
data: List[List] = load_csv(filepath)
for index in range(len(data[0])):
    str_column_to_float(data, index)
standardize_dataset(data)
print("Sample row from dataset after standardization:\n{}\n".format(data[0]))
