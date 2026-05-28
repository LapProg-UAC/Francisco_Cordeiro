from encrypt import encrypt_json, decrypt_json
from create_client import (create_one_client, create_several_clients, get_client_by_ssn,
                           get_clients_by_ssn_range, get_prescriptions_by_ssn, get_prescriptions_by_ssn_range)


def menu() -> str:
    """
    Display the main menu and get the user's option.

    :return: The selected menu option.
    :rtype: str
    """
    print('\nWelcome')
    print('\n[1] Create one client')
    print('[2] Create several clients')
    print('[3] Get client by SSN')
    print('[4] Get clients by SSN range')
    print('[5] Get prescriptions by SSN')
    print('[6] Get prescriptions by SSN range')
    print('[0] Exit')

    return input('\nWhat would you like to do? ')

def data() -> list:
    """
    Create and return the program configuration data.
    The returned list contains file paths, limits, encoding settings,
    and formatting options used throughout the application.

    :return: A list containing application configuration values.
    :rtype: list
    """
    #0
    first_name_list = 'data/first_name.txt'
    #1
    surname_list = 'data/surname.txt'
    #2
    one_client_output = 'data/data_one_client.json'
    #3
    several_clients_output = 'data/data_several_clients.json'
    #4
    encrypt_output = 'data/data_client_encrypted.json'
    #5
    decrypt_output = 'data/data_client_decrypted.json'
    #6
    medicine_list = 'data/medicamentos.txt'
    #7
    excel = 'data/matrix.xlsx'
    #8
    ssn_min_value = 1000
    #9
    ssn_max_value = 1000000
    #10
    min_medicine_num = 3
    #11
    max_medicine_num = 5
    #12
    max_danger_value = 6
    #13
    encode = 'utf-8'
    #14
    indent = 2

    return [first_name_list, surname_list, one_client_output, several_clients_output, encrypt_output,
            decrypt_output, medicine_list, excel, ssn_min_value, ssn_max_value,min_medicine_num, max_medicine_num,
            max_danger_value, encode, indent]

def ask_ssn() -> str:
    return input("Enter SSN: ")

def ask_range() -> tuple:
    x = int(input("Enter minimum SSN: "))
    y = int(input("Enter maximum SSN: "))
    return x, y

def ask_number_of_clients() -> int:
    """
    Prompt the user for the number of clients to create.
    The function keeps requesting input until the user enters
    a valid integer greater than 1.

    :return: Number of clients to generate.
    :rtype: int
    """
    while True:
        try:
            number = int(input('\nHow many clients would you like to create? (>1) '))
            if number > 1:
                return number
            else:
                print('\nPlease enter a valid number')
        except ValueError:
            print('\nPlease enter a valid number')

def process_one_client(data:list) -> dict:
    """
    Generate, encrypt, and decrypt data for a single client.

    :param data: Configuration and data source list used for generation.
    :type data: list
    :return: None
    :rtype: None
    """
    client = create_one_client(data)
    encrypt_json(data[2], data[4], data[13], data[14])
    decrypt_json(data[4], data[5], data[13], data[14])
    return client

def process_multiple_clients(number_of_clients:int, data:list) -> dict:
    """
    Generate data for multiple clients.

    :param number_of_clients: Number of clients to generate.
    :type number_of_clients: int
    :param data: Configuration and data source list used for generation.
    :type data: list
    :return: Dictionary containing the generated client data.
    :rtype: dict
    """
    return create_several_clients(number_of_clients, data)

def main():
    clients = {}

    while True:
        option = menu()

        if option == '1':
            process_one_client(data())

        elif option == '2':
            number_of_clients = ask_number_of_clients()
            clients = process_multiple_clients(number_of_clients, data())

        elif option == '3':
            ssn = ask_ssn()
            print(get_client_by_ssn(clients, ssn))

        elif option == '4':
            x, y = ask_range()
            print(get_clients_by_ssn_range(clients, x, y))

        elif option == '5':
            ssn = ask_ssn()
            print(get_prescriptions_by_ssn(clients, ssn))

        elif option == '6':
            x, y = ask_range()
            print(get_prescriptions_by_ssn_range(clients, x, y))

        elif option == '0':
            print('\nThank you for using this program')
            break

        else:
            print('\nPlease enter a valid number')

if __name__ == '__main__':
    main()
