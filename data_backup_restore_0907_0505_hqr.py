# 代码生成时间: 2025-09-07 05:05:25
# -*- coding: utf-8 -*-

"""
Data Backup and Restore Service using Python and Bottle framework.
"""

import os
import shutil
import bottle
from datetime import datetime

# Configuration for backup directory and file name
BACKUP_DIR = 'data_backup'
FILE_EXTENSION = '.sql'

# Initialize Bottle application
app = bottle.Bottle()

# Route for backup data
@app.route('/backup', method='GET')
def backup_data():
    """
    Backup data by creating a copy of the database file.
    Returns a JSON response indicating success or failure.
    """
    try:
        # Generate file name with timestamp
        file_name = 'backup_' + datetime.now().strftime('%Y%m%d%H%M%S') + FILE_EXTENSION
        src_file = 'database.db'  # Replace with your actual database file
        dst_file = os.path.join(BACKUP_DIR, file_name)

        # Create backup directory if it does not exist
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)

        # Copy the database file to the backup directory
        shutil.copy(src_file, dst_file)
        return {"status": "success", "message": "Data backup successful"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Route for restore data
@app.route('/restore/<filename>', method='GET')
def restore_data(filename):
    """
    Restore data from a backup file.
    Returns a JSON response indicating success or failure.
    """
    try:
        # Validate file extension
        if not filename.endswith(FILE_EXTENSION):
            return {"status": "error", "message": "Invalid file extension"}

        src_file = os.path.join(BACKUP_DIR, filename)
        dst_file = 'database.db'  # Replace with your actual database file

        # Check if the backup file exists
        if not os.path.exists(src_file):
            return {"status": "error", "message": "Backup file not found"}

        # Copy the backup file to the database file
        shutil.copy(src_file, dst_file)
        return {"status": "success", "message": "Data restore successful"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Run the Bottle application
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)