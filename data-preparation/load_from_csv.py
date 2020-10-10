"""
examples for loading and pre-processing csv files
"""

from csv import reader
from typing import List, Dict


def load_csv(filename: str) -> List[List]:
    """
    loads the csv file returns it as a list of lists
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


# functions for pre-processing data
def get_column_encodings(dataset: List[List], column_index: int) -> Dict[str, int]:
    """
    returns a lookup table for with numbers corresponding to categories in a given column
    """
    categories = set()
    for row in dataset:
        categories.add(row[column_index])
    lookup_table: Dict[str, int] = dict(zip(categories, range(len(categories))))
    return lookup_table


def str_column_to_float(dataset: List[List], column_index: int) -> None:
    """
    Convert the entire column inplace in the dataset from string to float
    """
    for row in dataset:
        row[column_index]: float = float(row[column_index].strip())


def encode_column_to_int(dataset: List[List], column_index: int) -> None:
    """
    Convert the entire column inplace in the dataset from string to int
    """
    encoder: Dict[str, int] = get_column_encodings(dataset, column_index)
    for row in dataset:
        row[column_index] = encoder[row[column_index]]


# ---- Example 1: pima-indians-diabetes.csv ----

# load the data and check if it is in the acceptable format
filepath: str = "../datasets/pima-indians-diabetes.csv"
data: List = load_csv(filepath)
print("\n[INFO] Loaded data file '{}' with {} rows and {} columns\n"
      .format(filepath.split("/")[-1], len(data), len(data[0])))
print("Sample row from dataset:\n{}\n".format(data[0]))


# pre-process the loaded data to the required format
# we see that all columns are strings, but we need them as floats
# iterate over each column index and pass it through str_column_to_float
for col_index in range(len(data[0])):
    str_column_to_float(data, col_index)


# verify if the pre-processing is satisfactory
print("Sample row after pre-processing:\n{}\n".format(data[0]))


# ---- Example 2: iris.csv ----

# load the data and check if it is in the acceptable format
filepath: str = "../datasets/iris.csv"
data: List = load_csv(filepath)
print("\n[INFO] Loaded data file '{}' with {} rows and {} columns\n"
      .format(filepath.split("/")[-1], len(data), len(data[0])))
print("Sample row from dataset:\n{}\n".format(data[0]))


# pre-process the loaded data to the required format
# we need to convert the first 4 columns to float
# the last column has to be encoded
for col_index in range(4):
    str_column_to_float(data, col_index)
encode_column_to_int(data, -1)


# verify if the pre-processing is satisfactory
print("Sample row after pre-processing:\n{}\n".format(data[0]))
