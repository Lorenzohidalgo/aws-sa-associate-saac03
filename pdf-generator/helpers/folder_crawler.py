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


def get_folders_with_content(folders: list, subfolder='00_LEARNINGAIDS') -> list:
    """Checks folders for available images

    Args:
        folders (list): available folders
        subfolder (str, optional): name of subfolder. Defaults to '00_LEARNINGAIDS'.

    Returns:
        list: full paths to folders with images
    """
    valid_folders = []
    for folder in folders:
        try:
            path = folder
            if subfolder is not None:
                path += '/' + subfolder
            files = os.listdir(path)
            has_images = False
            for file in files:
                if file.rsplit('.', maxsplit=1)[1] == 'png':
                    has_images = True
                    break
            if has_images:
                valid_folders.append(path)
        except NotADirectoryError:
            pass
    return valid_folders


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
