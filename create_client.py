import random
import json
from perscription import generate_prescription


def create_name_list(first_name_list:str) -> list:
    """
    Creates a list of first names from the list given
    :param first_name_list: file name of the list of first names
    :type first_name_list: list
    :return: list of first names
    :rtype: list
    """
    with open(first_name_list, "r") as file:
        return file.read().splitlines()

def create_surname_list(surname_list:str) -> list:
    """
    Creates a list of surnames from the list given
    :param surname_list: file name of the list of surnames
    :type surname_list: list
    :return: list of surnames
    :rtype: list
    """
    with open(surname_list, "r") as file:
        return file.read().splitlines()

def create_full_name(fn:list, sn:list) -> str:
    """
    Creates a full name from the list given
    :param fn: first name list
    :type fn: list
    :param sn: surname list
    :type sn: list
    :return: full name
    :rtype: str
    """
    name_random = random.randint(0, len(fn) - 1)
    surname_random = random.randint(0, len(sn) - 1)
    full_name = fn[name_random] + ' ' + sn[surname_random]
    return full_name

def user_number() -> int:
    """
    Creates a Social Security Number (SSN) at random
    :return: random SSN
    :rtype: int
    """
    return random.randint(1000, 1000000)

def client_info():
    """
    Creates client info (first name list, surname list, SSN)
    :return: full name, SSN
    :rtype: str, int
    """
    first_name = create_name_list("data/first_name.txt")
    surname = create_surname_list("data/surname.txt")
    number = user_number()
    return create_full_name(first_name, surname), number

def create_one_client():
    """
    Creates a json file with the information of one client, with perscription info
    :return: None
    """
    name, ssn = client_info()
    medicine, danger = generate_prescription()

    client = {
        "Name": name,
        "SSN": ssn,
        "Perscription": medicine,
        "Danger": danger
    }

    print(json.dumps(client, ensure_ascii=False, indent=2))

    with open("data/data_client.json", "w") as file:
        json.dump(client, file, ensure_ascii=False, indent=2)

def create_several_clients(amount: int):
    """
    Creates a json file with the information of several clients
    :param amount: number of clients
    :type amount: int
    :return: None
    """
    clients = []

    for _ in range(amount):
        name, ssn = client_info()
        medicine, danger = generate_prescription()

        client = {
            "Name": name,
            "SSN": ssn,
            "Perscription": medicine,
            "Danger": danger
        }

        clients.append(client)

    print(json.dumps(clients, ensure_ascii=False, indent=2))

    with open("data/data_more_clients.json", "w") as file:
        json.dump(clients, file, ensure_ascii=False, indent=2)

