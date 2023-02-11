"""
    Provides Helpfull funtions to crawl the repository folders
"""


import os


def get_all_main_folders() -> list:
    """Fetches all the current folders

    Returns:
        list: available folders names
    """
    return os.listdir()


def get_folder_with_content(folder: str, subfolder='00_LEARNINGAIDS') -> str|None:
    """Checks folders for available images

    Args:
        folder (str): folders
        subfolder (str, optional): name of subfolder. Defaults to '00_LEARNINGAIDS'.

    Returns:
        str: path to images
    """
    valid_folder = False
    try:
        path = folder
        if subfolder is not None:
            path += '/' + subfolder
        files = os.listdir(path)
        for file in files:
            if file.rsplit('.', maxsplit=1)[1] == 'png':
                valid_folder = True
                break
    except NotADirectoryError:
        pass
    if valid_folder:
        return path
    return None


def get_all_images_from_folder(folder_path: str) -> list:
    """Retrieves all paths for images inside folder path

    Args:
        folder_path (str): path for the desired folder

    Returns:
        list: all available images paths
    """
    images = []
    try:
        files = os.listdir(folder_path)
        for file in files:
            if file.rsplit('.', maxsplit=1)[1] == 'png':
                images.append(folder_path + '/' + file)
    except NotADirectoryError:
        pass
    return images
