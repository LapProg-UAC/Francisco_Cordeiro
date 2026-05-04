import random
from itertools import combinations
from generate_matrix import create_list, generate_matrix, create_excel_file

med_list = create_list("data/medicamentos.txt")
matrix = generate_matrix(med_list)
create_excel_file(matrix, 'data/matrix.xlsx')

def generate_prescription() -> list:
    """
    Generates a prescription (list) of 3-5 unique medicine from the medicine list
    and sums up the values of each combination of the medicines as a danger value.
    :return: prescription and danger value
    :rtype: list
    """

    num_medicine = random.randint(3, 5)
    medicine = []
    while len(medicine) < num_medicine:
        drug = random.choice(med_list)
        if drug not in medicine:
            medicine.append(drug)

    pairs = list(combinations(medicine, 2))

    danger_value = 0
    for a in pairs:
        for b in matrix:
            if a[0] == b[0] and a[1] == b[1]:
                danger_value += b[2]

    return [medicine, danger_value]