import json, sys
from file_manager import read_json, write_json


def encryption(phrase) -> str:
    """
    Encrypts the given phrase
    :param phrase: phrase to encrypt
    :type phrase: str
    :return: encrypted phrase
    :rtype: str
    """
    sentence = ''
    for i in phrase:
        if i.isupper():
            sentence += chr((ord(i) - ord('A') + 3) % 26 + ord('A'))
        elif i.islower():
            sentence += chr((ord(i) - ord('a') + 3) % 26 + ord('a'))
        elif i.isdigit():
            sentence += chr((ord(i) - ord('0') + 3) % 10 + ord('0'))
        else:
            sentence += i

    return sentence

def decryption(phrase:str) -> str:
    """
    Decrypts the given phrase
    :param phrase: Encrypted phrase
    :type phrase: str
    :return: Decrypted phrase
    :rtype: str
    """
    sentence = ''
    for i in phrase:
        if i.isupper():
            sentence += chr((ord(i) - ord('A') - 3) % 26 + ord('A'))
        elif i.islower():
            sentence += chr((ord(i) - ord('a') - 3) % 26 + ord('a'))
        elif i.isdigit():
            sentence += chr((ord(i) - ord('0') - 3) % 10 + ord('0'))
        else:
            sentence += i

    return sentence

def open_txt(filename: str) -> str:
    """
    Opens a txt file with the given filename
    :param filename: txt filename
    :type filename: str
    :return: the opened txt file as a string
    :rtype: str
    """
    with open(filename, 'r') as f:
        return f.read()

def write_txt_encrypted(filename: str) -> None:
    """
    Writes a txt file of an encrypted text from the given filename
    :param filename: txt filename to encrypt
    :type filename: str
    :return: None
    """
    with open('texto_encriptado.txt', 'w') as f:
        f.write(encryption(open_txt(filename)))

def write_txt_unencrypted(filename: str) -> None:
    """
    Writes a txt file of a decrypted text from the given filename
    :param filename: txt filename to decrypt
    :type filename: str
    :return: None
    """
    with open('texto_desencriptado.txt', 'w') as f:
        f.write(decryption(open_txt(filename)))


"""------------------------------------------------------------------------------------------------------"""

def encryption_number(ssn_number:str) -> str:
    """
    Encrypt a numeric SSN string using a Caesar-style digit shift.
    Each digit is shifted forward by 3. Values exceeding '9' wrap
    around to the beginning of the digit range.

    :param ssn_number: The SSN string to encrypt.
    :type ssn_number: str
    :return: The encrypted SSN string.
    :rtype: str
    """
    encrypted_ssn_number = ''
    for i in ssn_number:
        new = ord(i) + 3
        if new > 57:
            new = new - 10
        encrypted_ssn_number += chr(new)
    return encrypted_ssn_number

def decryption_number(ssn_number:str) -> str:
    """
    Decrypt a numeric SSN string encrypted with a Caesar-style digit shift.
    Each digit is shifted backward by 3. Values below '0' wrap
    around to the end of the digit range.

    :param ssn_number: The encrypted SSN string.
    :type ssn_number: str
    :return: The decrypted SSN string.
    :rtype: str
    """
    decrypted_ssn_number = ''
    for i in ssn_number:
        new = ord(i) - 3
        if new < 48:
            new = new + 10
        decrypted_ssn_number += chr(new)
    return decrypted_ssn_number

def encrypt_json(filename_input:str, filename_output:str, encode:str, indent:int) -> None:
    """
    Encrypt the SSN field in a JSON file and save the result.

    :param filename_input: Path to the input JSON file.
    :type filename_input: str
    :param filename_output: Path to the output JSON file.
    :type filename_output: str
    :param encode: File encoding used for reading and writing.
    :type encode: str
    :param indent: Indentation level for JSON formatting.
    :type indent: int
    :return: None
    :raises SystemExit: If the input file cannot be found.
    """
    try:
        data = read_json(filename_input, encode)
        ssn = str(data.get('SSN'))
        data['SSN'] = encryption_number(ssn)
        write_json(filename_output, data, encode, indent)
        return None
    except FileNotFoundError:
        sys.exit(f'Fatal Error: File "{filename_input}" not found.')

def decrypt_json(filename_input:str, filename_output:str, encode:str, indent:int) -> None:
    """
    Decrypt the SSN field in a JSON file and save the result.

    :param filename_input: Path to the encrypted input JSON file.
    :type filename_input: str
    :param filename_output: Path to the decrypted output JSON file.
    :type filename_output: str
    :param encode: File encoding used for reading and writing.
    :type encode: str
    :param indent: Indentation level for JSON formatting.
    :type indent: int
    :return: None
    :raises SystemExit: If the input file cannot be found.
    """
    try:
        client_data = read_json(filename_input, encode)
        ssn = str(client_data.get('SSN'))
        client_data['SSN'] = decryption_number(ssn)
        write_json(filename_output, client_data, encode, indent)
        return None
    except FileNotFoundError:
        sys.exit(f'Fatal Error: File "{filename_input}" not found.')

