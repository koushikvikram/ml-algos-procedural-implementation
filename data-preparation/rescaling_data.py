"""
Rescaling data - normalization and standardization
"""

from typing import List
from csv import reader


# functions for rescaling features
def get_dataset_minmax(dataset: List[List], columns_list=True) -> dict:
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


def norm(value: float, min: int, max: int) -> float:
    """
    return the norm of the value
    """
    return (value-min) / (max-min)


def normalize_dataset(dataset: List[List], minmax_lookup: dict) -> None:
    """
    normalize the columns in the dataset that are part of minmax_lookup
    """
    column_indices = minmax_lookup.keys()
    for row in dataset:
        for col_index in column_indices:
            col_value: int = row[col_index]
            col_min: float = minmax_lookup[col_index][0]
            col_max: float = minmax_lookup[col_index][1]

            row[col_index]: float = norm(col_value, col_min, col_max)


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
print("\n[INFO] Loaded dataset '{}' with {} rows and {} columns\n".format(filepath.split("/")[-1], len(data), len(data[0])))
print("Sample row from dataset:\n{}\n".format(data[0]))


# ---- pre-process the dataset ----
# convert all columns from string to float
for col_index in range(len(data[0])):
    str_column_to_float(data, col_index)
print("Sample row from dataset after datatype conversion:\n{}\n".format(data[0]))


# ---- normalize all columns in the dataset ----
minmax_lookup: dict = get_dataset_minmax(data)
normalize_dataset(data, minmax_lookup)
print("Sample row from dataset after normalization:\n{}\n".format(data[0]))