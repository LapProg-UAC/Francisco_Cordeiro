import random
import pandas as pd


def generate_matrix(medicine_list:list, max_danger_value) -> list:
    """
    Generate a matrix of medicine interaction danger values.
    Each medicine is paired with every other medicine. Identical pairs
    receive a value of 0, while different pairs receive a random value
    between 1 and 'max_danger_value'.

    :param medicine_list: List of medicine names.
    :type medicine_list: list
    :param max_danger_value: Maximum random danger value allowed.
    :type max_danger_value: int
    :return: A list of tuples containing row medicine, column medicine, and danger value.
    :rtype: list
    """
    matrix = []
    for row in medicine_list:
        for column in medicine_list:
            if row == column:
                value = 0
            else:
                value = random.randint(1,max_danger_value)
            matrix.append((row, column, value))
    return matrix

def create_excel_file(matrix:list, filename_output:str) -> None:
    """
    Create an Excel file from a medicine interaction matrix.
    The matrix is converted into a pandas DataFrame and exported
    as an Excel spreadsheet.

    :param matrix: List of tuples representing the interaction matrix.
    :type matrix: list
    :param filename_output: Path of the output Excel file.
    :type filename_output: str
    :return: None
    :rtype: None
    """
    df = pd.DataFrame(matrix, columns=['Row', 'Column', 'Value'])
    matrix_df = df.pivot(index='Row', columns='Column', values='Value')
    matrix_df.to_excel(filename_output, engine='openpyxl')
    return None
