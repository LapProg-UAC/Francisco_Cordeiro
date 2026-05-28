import json, sys


def read_json(filename:str, encode:str) -> dict:
    """
    Read and load data from a JSON file.

    :param filename: Path to the JSON file.
    :type filename: str
    :param encode: File encoding used to read the file.
    :type encode: str
    :return: Parsed JSON data as a dictionary.
    :rtype: dict
    """
    with open(filename, 'r', encoding=encode) as json_file:
        return json.load(json_file)

def write_json(filename_output:str, client_data:dict, encode:str, indent:int) -> None:
    """
    Write dictionary data to a JSON file.

    :param filename_output: Path to the output JSON file.
    :type filename_output: str
    :param client_data: Dictionary containing client data.
    :type client_data: dict
    :param encode: File encoding used to write the file.
    :type encode: str
    :param indent: Indentation level for JSON formatting.
    :type indent: int
    :return: None
    """
    with open(filename_output, 'w', encoding=encode) as json_file:
        json.dump(client_data, json_file, ensure_ascii=False, indent=indent)
        return None
    
def read_txt(filename:str, encode:str) -> list:
    """
    Create a list from the contents of a text file.
    Each line in the file is stored as an element in the returned list.

    :param filename: Path to the input file.
    :type filename: str
    :param encode: File encoding to use when reading the file.
    :type encode: str
    :return: A list containing the lines of the file.
    :rtype: list
    :raises SystemExit: If the file does not exist.
    """
    try:
        with open(filename, "r", encoding=encode) as file:
            return file.read().splitlines()
    except FileNotFoundError:
        sys.exit(f'Fatal Error: File "{filename}" not found.')