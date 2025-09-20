# 代码生成时间: 2025-09-21 05:59:22
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
System Performance Monitor using Python and Bottle framework.
"""

from bottle import route, run, template, request
import psutil
import json


# Define the port and host for running the Bottle application
PORT = 8080
HOST = 'localhost'

"""
Error handling for invalid requests.
"""
@route('/error')
def error_handler():
    return template('<h1>Error</h1><p>Error processing the request.</p>')

"""
Route to get system information.
"""
@route('/info')
def get_system_info():
    """
    Returns a JSON object containing system information.
    """
    try:
        # Collect system information using psutil
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        system_info = {
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage,
            'disk_usage': disk_usage
        }
        return json.dumps(system_info)
    except Exception as e:
        # Handle any exceptions and return an error message
        return json.dumps({'error': str(e)})

"""
Main function to run the Bottle application.
"""
def main():
    """
    Runs the Bottle application with the specified port and host.
    """
    run(host=HOST, port=PORT, reloader=True)

if __name__ == '__main__':
    main()
