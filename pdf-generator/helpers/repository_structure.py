"""
    Module to ease the task of crawling and preparing the necessaty objects.
"""
from . import folder_crawler as fc
from . import names_parsers as np


def get_folder_structure() -> list:
    """Crawles and returns the parsed folderstructure

    Returns:
        list: sorted with folder_objects containing its sorted images list
    """
    folder_structure = []
    available_folders = fc.get_all_main_folders()
    for folder in available_folders:
        folder_object = np.folder_object_from_name(folder)
        folder_object["content_path"] = fc.get_folder_with_content(folder)
        folder_object["has_files"] = folder_object["content_path"] is not None
        images = []
        if folder_object["has_files"]:
            available_content = fc.get_all_images_from_folder(folder_object["content_path"])
            for image_path in available_content:
                image_name = np.get_name_from_path(image_path)
                image_object = np.file_object_from_name(image_name)
                image_object["full_path"] = image_path
                images.append(image_object)
        folder_object["images"] = sorted(images, key=lambda e: (e["file_name"], e["file_order"]))
        folder_structure.append(folder_object)
    folder_structure = sorted(folder_structure, key=lambda e: (e["folder_order"], e["folder_sub_order"]))
    return folder_structure
