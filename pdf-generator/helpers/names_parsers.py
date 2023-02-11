"""
This module helps parse folder and file names into usefull objects.
"""

import re


def __get_folder_orders(order: str) -> tuple:
    if len(order) != 4:
        return 0, 0
    primary = 0
    try:
        primary = int(order[:2])
    except ValueError:
        pass
    secondary = 0
    try:
        secondary = int(order[2:2])
    except ValueError:
        pass
    return primary, secondary


def folder_object_from_name(name: str) -> object:
    """ Parses the folder name into the desired object

    Args:
        name (str): Folder Name

    Returns:
        object: contains the following keys + values
        ["folder_name", "folder_order", "folder_sub_order", "parsed_name"]
    """
    folder_object = {}
    folder_object["folder_name"] = name
    raw_order, raw_name = name.split('-')
    folder_object["folder_order"], folder_object["folder_sub_order"] = __get_folder_orders(
        raw_order)
    folder_object["parsed_name"] = " ".join(raw_name.split('_'))
    return folder_object


def __get_file_type(name: str) -> str:
    return name.rsplit('.', maxsplit=1)[1]


def __get_file_order(name: str) -> int:
    name_part = name.rsplit('.', maxsplit=1)[0]
    if '-' in name_part:
        order_part = name_part.rsplit('-', maxsplit=1)[-1]
        try:
            return int(order_part)
        except ValueError:
            return 0
    else:
        return 0


def __format_words(words: list) -> str:
    result = ''
    for word in words:
        if len(word) <= 2 or len(result) < 1:
            result += word
        else:
            result += ' ' + word
    return result


def __get_formatted_file_name(name: str) -> str:
    raw_name = name.rsplit('.', maxsplit=1)[0]
    if '-' in raw_name:
        check_last = raw_name.rsplit('-', maxsplit=1)[-1]
        try:
            int(check_last)
            raw_name = raw_name.rsplit('-', maxsplit=1)[0]
        except ValueError:
            pass
    name_parts = re.findall(r'[A-Z](?:[a-z\-\d]+|\d*(?=[A-Z]|$))', raw_name)
    if len(name_parts) == 0:
        return raw_name
    return __format_words(name_parts)


def file_object_from_name(name: str) -> object:
    """Parses the file name into the desired object

    Args:
        name (str): File name

    Returns:
        object: contains the following keys + values
        ["file_name", "file_type", "file_order", "parsed_name"]
    """
    file_object = {}
    file_object["file_name"] = name
    file_object["file_type"] = __get_file_type(name)
    file_object["file_order"] = __get_file_order(name)
    file_object["parsed_name"] = __get_formatted_file_name(name)
    return file_object
