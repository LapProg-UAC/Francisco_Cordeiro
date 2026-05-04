import json

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

def encryption_number(num:str) -> str:
    """
    Encrypts the given number
    :param num: number to encrypt
    :type num: str
    :return: encrypted number
    :rtype: str
    """
    number = ''
    for i in num:
        new = ord(i) + 3
        if new > 57:
            new = new - 10
        number += chr(new)
    return number

def encrypt_json():
    """
    Opens a json file with the information a client, and creates a new json file with
    the SSN of the client encrypted
    :return: None
    """
    with open('data/data_client.json', 'r') as json_file:
        data = json.load(json_file)
        a = data.get('SSN')
        data['SSN'] = a

    with open('data/data_client_encrypted.json', 'w') as json_file:
        data['SSN'] = int(encryption_number(str(a)))
        json.dump(data, json_file, ensure_ascii=False, indent=2)

def decryption_number(num:str) -> str:
    """
    Decrypts the given number
    :param num: Number to decrypt
    :type num: str
    :return: Decrypted number
    :rtype: str
    """
    number = ''
    for i in num:
        new = ord(i) - 3
        if new < 48:
            new = new + 10
        number += chr(new)
    return number

def decrypt_json():
    """
    Opens a json file with the information a client, and creates a new json file with
    the SSN of the client decrypted
    :return: None
    """
    with open('data/data_client_encrypted.json', 'r') as json_file:
        data = json.load(json_file)
        a = data.get('SSN')
        data['SSN'] = a


    with open('data/data_client_decrypted.json', 'w') as json_file:
        data['SSN'] = int(decryption_number(str(a)))
        json.dump(data, json_file, ensure_ascii=False, indent=2)