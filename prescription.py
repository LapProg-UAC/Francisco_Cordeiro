import random, sys
from itertools import combinations
from file_manager import read_txt
from generate_matrix import generate_matrix, create_excel_file


def generate_prescription(data:list) -> tuple:
    """
    Generate a random prescription and calculate its danger value.
    The function loads a medicine list, generates a medicine interaction
    matrix, exports the matrix to an Excel file, randomly selects a set
    of medicines, and calculates the total danger value based on the
    interaction matrix.

    :param data: Configuration and data source list used for generation.
    :type data: list
    :return: A tuple containing the selected medicines and the total danger value.
    :rtype: tuple
    :raises SystemExit: If 'min_medicine_num' is greater than 'max_medicine_num'.
    """
    medicine_list = read_txt(data[6], data[13])
    matrix = generate_matrix(medicine_list, data[12])
    create_excel_file(matrix, data[7])

    if data[10] > data[11]:
        sys.exit('"min_medicine_num" must be smaller than "max_medicine_num"')

    number_of_medicine = random.randint(data[10], data[11])
    medicine = []
    while len(medicine) < number_of_medicine:
        drug = random.choice(medicine_list)
        if drug not in medicine:
            medicine.append(drug)

    danger_value = 0
    for i in tuple(combinations(medicine, 2)):
        for j in matrix:
            if i[0] == j[0] and i[1] == j[1]:
                danger_value += j[2]

    return (medicine, danger_value)
