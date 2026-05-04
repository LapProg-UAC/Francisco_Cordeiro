import random
import pandas as pd

def create_list(filename:str) -> list:
    """
    Reads a txt file and creates a list where each element is a line of the file
    :param filename: name of the file
    :type filename: str
    :return: list of lines of original file
    :rtype: list
    """
    with open(filename, "r") as file:
        return file.read().splitlines()

def generate_matrix(med_list:list) -> list:
    """
    Generates a matrix, in the form of a list, where each row and column is an element of the given list
    and gives each combination a random number from 1-6 (or 0 if the row and column are equal).
    :param med_list: list of elements to create matrix
    :type med_list: list
    :return: matrix
    :rtype: list
    """
    matrix = []
    for row in med_list:
        for column in med_list:
            if row == column:
                value = 0
            else:
                value = random.randint(1,6)
            matrix.append([row, column, value])
    return matrix

def create_excel_file(matrix:list, filename:str) -> None:
    """
    Creates an Excel file, with the given filename, of a given matrix
    :param matrix: matrix
    :type matrix: list
    :param filename: name of the file
    :type filename: str
    :return: None
    """
    df = pd.DataFrame(matrix, columns=['Row', 'Column', 'Value'])
    matrix_df = df.pivot(index='Row', columns='Column', values='Value')
    matrix_df.to_excel(filename, engine='openpyxl')
