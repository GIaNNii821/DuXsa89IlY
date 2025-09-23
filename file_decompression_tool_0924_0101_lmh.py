# 代码生成时间: 2025-09-24 01:01:27
from bottle import route, run, request, response
import zipfile
import os
import shutil
# 改进用户体验

"""
A simple Bottle web application that serves as a file decompression tool.
This application allows users to upload a zip file and decompresses it to a specified directory.
"""

# The directory where the files will be extracted
DECOMPRESSION_DIR = "decompressed_files"

@route('/decompress', method='POST')
def decompress_file():
    # Check if the request contains a file
    if 'file' not in request.files:
        return {"error": "No file part"}
# TODO: 优化性能
    file = request.files['file']
    
    # Check if the uploaded file is actually a zip file
    if file.filename.split('.')[-1].lower() != 'zip':
# 扩展功能模块
        return {"error": "Invalid file type. Only .zip files are allowed."}
    
    # Create the decompression directory if it doesn't exist
    if not os.path.exists(DECOMPRESSION_DIR):
        os.makedirs(DECOMPRESSION_DIR)
    
    # Prepare the path to save the zip file
    temp_zip_path = os.path.join(DECOMPRESSION_DIR, file.filename)
    
    # Save the file to the server
    with open(temp_zip_path, 'wb') as fp:
        fp.write(file.file.read())
    
    try:
        # Extract the zip file
        with zipfile.ZipFile(temp_zip_path, 'r') as zip_ref:
            zip_ref.extractall(DECOMPRESSION_DIR)
# FIXME: 处理边界情况
        return {"message": "File successfully decompressed."}
    except zipfile.BadZipFile:
        return {"error": "Invalid zip file."}
    finally:
        # Clean up the temporary zip file
        os.remove(temp_zip_path)

# Set the Bottle application to run on port 8080
# TODO: 优化性能
run(host='localhost', port=8080, debug=True)