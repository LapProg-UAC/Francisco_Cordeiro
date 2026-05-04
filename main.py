from encrypt import encrypt_json, decrypt_json
from create_client import create_one_client, create_several_clients

invalid = '\nPlease enter a valid number'

def menu():
    """
    Prints a menu for user interface and asks the user to input an option
    :return: option chosen by user
    :rtype: str
    """
    print('\nWelcome')
    print('\n[1] Create one client')
    print('[2] Create several clients')
    print('[0] Exit')
    num = input('\nWhat would you like to do? ')
    return num

def process_one_client():
    """
    Creates one client, encrypts, decrypts and processes that data into json files.
    :return: None
    """
    create_one_client()
    encrypt_json()
    decrypt_json()

def process_multiple_clients():
    """
    Asks the user for the total number of clients (>1).
    If the input is invalid, it creates their data. Otherwise, it displays and invalid input message
    :return: None
    """
    try:
        number_clients = int(input('\nHow many clients would you like to create? (>1) '))
        if number_clients > 1:
            create_several_clients(number_clients)
        else:
            print(invalid)
    except ValueError:
        print(invalid)

def main():
    """
    Main function of the program.
    Displays the menu in a continuous loop and, based on user input, it executes the following actions:
    Option 1: Processes one client
    Option 2: Processes multiple clients
    Option 0: Exit
    If the user input is invalid, it displays invalid input message
    :return: None
    """
    while True:
        num = menu()
        if num == '1':
            process_one_client()
        elif num == '2':
            process_multiple_clients()
        elif num == '0':
            print('\nThank you for using this program')
            break
        else:
            print(invalid)

main()
