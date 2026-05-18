import random, sys
from encrypt import write_json
from prescription import generate_prescription
from generate_matrix import create_list


def load_name_list(first_name_filename:str, encode:str) -> list:
    """
    Load a list of first names from a file.

    :param first_name_filename: Path to the file containing first names.
    :type first_name_filename: str
    :param encode: File encoding to use when reading the file.
    :type encode: str
    :return: A list of first names.
    :rtype: list
    """
    return create_list(first_name_filename, encode)

def load_surname_list(surname_filename:str,encode:str) -> list:
    """
    Load a list of surnames from a file.

    :param surname_filename: Path to the file containing surnames.
    :type surname_filename: str
    :param encode: File encoding to use when reading the file.
    :type encode: str
    :return: A list of surnames.
    :rtype: list
    """
    return create_list(surname_filename, encode)

def create_full_name(first_name_list:list, surname_list:list) -> str:
    """
    Create a random full name using a first name and surname.

    :param first_name_list: List of available first names.
    :type first_name_list: list
    :param surname_list: List of available surnames.
    :type surname_list: list
    :returns: A randomly generated full name.
    :rtype: str
    """
    return (random.choice(first_name_list) + ' ' + random.choice(surname_list))

def generate_ssn(min_ssn_value:int, max_ssn_value:int) -> str:
    """
    Generate a random Social Security Number within a range.

    :param min_ssn_value: Minimum allowed SSN value.
    :type min_ssn_value: int
    :param max_ssn_value: Maximum allowed SSN value.
    :type max_ssn_value: int
    :return: A randomly generated SSN.
    :rtype: str
    :raises SystemExit: If 'min_ssn_value' is greater than 'max_ssn_value'.
    """
    if min_ssn_value > max_ssn_value:
        sys.exit('"min_ssn_value" must be smaller than "max_ssn_value"')
    return str(random.randint(min_ssn_value, max_ssn_value))

def generate_client_info(data:list) -> tuple:
    """
    Generate client information including full name and SSN.

    :param data: Configuration and data source list used for generation.
    :type data: list
    :returns: A tuple containing the client's full name and SSN.
    :rtype: tuple
    """
    return (create_full_name(load_name_list(data[0], data[13]), load_surname_list(data[1], data[13])),
            generate_ssn(data[8], data[9]))

def create_one_client(data:list) -> dict:
    """
    Create a single client record and write it to a JSON file.

    :param data: Configuration and data source list used for generation.
    :type data: list
    :returns: A dictionary containing the generated client information.
    :rtype: dict
    """
    name, ssn = generate_client_info(data)
    medicine, danger = generate_prescription(data)

    client = {"Name": name,
              "SSN": ssn,
              "Prescription": medicine,
              "Danger": danger}

    write_json(data[2], client, data[13], data[14])
    return client

def create_several_clients(number_of_clients:int, data:list) -> dict:
    """
    Create multiple client records and write them to a JSON file.

    :param number_of_clients: Number of clients to generate.
    :type number_of_clients: int
    :param data: Configuration and data source list used for generation.
    :type data: list
    :returns: A dictionary containing all generated clients.
    :rtype: dict
    """
    clients = {}

    for i in range(number_of_clients):
        name, ssn = generate_client_info(data)
        medicine, danger = generate_prescription(data)

        client = {"Name": name,
                  "SSN": ssn,
                  "Prescription": medicine,
                  "Danger": danger}

        clients[f'Client #{i + 1}'] = client

    write_json(data[3], clients, data[13], data[14])
    return clients

