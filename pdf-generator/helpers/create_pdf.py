"""
    Module to create a PDF from the received repository structure
"""


import img2pdf


def create_pdf(repo_structure: list, file_name: str) -> None:
    """Creates a PDF from the received repository structure

    Args:
        repo_structure (list): 
        file_name (str): 
    """
    with open(file_name, "wb") as file:
        for folder_object in repo_structure:
            if not folder_object["has_files"]:
                continue
            for image_object in folder_object["images"]:
                print("Writing image " + image_object["parsed_name"] + " to pdf")
                file.write(img2pdf.convert(image_object["full_path"]))