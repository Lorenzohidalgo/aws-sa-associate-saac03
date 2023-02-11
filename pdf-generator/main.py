"""
    Test
"""

from helpers.repository_structure import get_folder_structure
from helpers.create_pdf import create_pdf

if __name__ == '__main__':
    repo_struct = get_folder_structure()
    print(repo_struct)
    create_pdf(repo_struct, 'TestFile.pdf')
