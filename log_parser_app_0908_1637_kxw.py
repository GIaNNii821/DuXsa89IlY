# 代码生成时间: 2025-09-08 16:37:21
#!/usr/bin/env python

"""
Log Parser Application using Bottle framework

This application provides a simple web interface to parse log files and display the results.
"""

from bottle import route, run, template, request, response
import re
import os

# Define the path to the log files
LOG_FILES_PATH = 'log_files/'

# Check if the log files directory exists
if not os.path.exists(LOG_FILES_PATH):
    os.makedirs(LOG_FILES_PATH)

# Define a regex pattern to match log file lines
LOG_LINE_PATTERN = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),(\S+),(\S+),(\S+)')

# Function to parse a single log file
def parse_log_file(file_path):
    """Parses a log file and returns a list of dictionaries with the log entries."""
    parsed_logs = []
    with open(file_path, 'r') as file:
        for line in file:
            match = LOG_LINE_PATTERN.match(line)
            if match:
                parsed_logs.append({
                    'timestamp': match.group(1),
                    'level': match.group(2),
                    'message': match.group(3),
                    'source': match.group(4)
                })
            else:
                # Handle lines that do not match the pattern
                parsed_logs.append({'error': 'Invalid log format'})
    return parsed_logs

# Define a route to serve the index page
@route('/')
def index():
    """Serves the index page for the log parser application."""
    return template('index')

# Define a route to handle the log file upload and parsing
@route('/parse', method='POST')
def parse_log():
    """Handles the log file upload and parses the file."""
    # Check if a file was uploaded
    if 'file' not in request.files:
        return template('index', error='No file uploaded.')
        
    # Get the uploaded file
    uploaded_file = request.files['file']
    
    # Save the uploaded file to the log files directory
    file_name = uploaded_file.filename
    file_path = os.path.join(LOG_FILES_PATH, file_name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.file.read())
    
    try:
        # Parse the uploaded log file
        logs = parse_log_file(file_path)
        return template('results', logs=logs)
    except Exception as e:
        # Handle any exceptions that occur during parsing
        return template('index', error=str(e))

# Start the Bottle server
run(host='localhost', port=8080, debug=True, reloader=True)