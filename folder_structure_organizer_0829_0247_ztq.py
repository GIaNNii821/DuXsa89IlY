# 代码生成时间: 2025-08-29 02:47:44
# folder_structure_organizer.py

# Imports
from bottle import route, run, request, response
import os
import shutil
from typing import Dict, List

# Global variables
ORGANISER = 'Organizer'

# Function to check if a path is a directory
def is_directory(path: str) -> bool:
    """Check if the given path is a directory."""
    return os.path.isdir(path)

# Function to create a directory
def create_directory(path: str) -> None:
    """Create a directory if it does not exist."""
    if not is_directory(path):
        os.makedirs(path)

# Function to move files to a directory
def move_files_to_directory(files: List[str], directory: str) -> None:
    """Move a list of files to a directory."""
    for file in files:
        try:
            shutil.move(file, directory)
        except Exception as e:
            print(f"Error moving file {file}: {e}")

# Function to organize files in a directory
def organize_files_in_directory(directory: str) -> None:
    """Organize files in a given directory into subdirectories."""
    create_directory(directory)
    file_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    move_files_to_directory(file_list, directory)

# Bottle route to handle the folder structure organizing
@route('/organize', method='POST')
def organize_folder_structure():
    "