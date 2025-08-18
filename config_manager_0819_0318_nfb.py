# 代码生成时间: 2025-08-19 03:18:02
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Config Manager - A simple configuration file manager using Bottle framework.

This script allows users to load, save, and reload configuration files.
It demonstrates a simple implementation of a RESTful service using Bottle.
"""

from bottle import route, run, request, response, template
import json
import os

# Define the path where configuration files will be stored.
CONFIG_DIR = './configs'

# Ensure the configuration directory exists.
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

# Helper function to load configuration from a file.
def load_config(file_name):
    try:
        with open(os.path.join(CONFIG_DIR, file_name), 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

# Helper function to save configuration to a file.
def save_config(file_name, config):
    try:
        with open(os.path.join(CONFIG_DIR, file_name), 'w') as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        raise Exception('Failed to save configuration: {}'.format(e))

# Route to load configuration.
@route('/config/<file_name>', method='GET')
def load(file_name):
    """
    Load a configuration file and return its content.
    :param file_name: The name of the configuration file.
    """
    config = load_config(file_name)
    if config is None:
        response.status = 404
        return {'error': 'Configuration file not found.'}
    return config

# Route to save configuration.
@route('/config/<file_name>', method='PUT')
def save(file_name):
    """
    Save a new configuration or update an existing one.
    :param file_name: The name of the configuration file.
    """
    try:
        config = request.json
        save_config(file_name, config)
        return {'message': 'Configuration saved successfully.'}
    except Exception as e:
        response.status = 400
        return {'error': str(e)}

# Route to reload configuration.
@route('/config/<file_name>/reload', method='POST')
def reload(file_name):
    """
    Reload a configuration file.
    :param file_name: The name of the configuration file.
    """
    try:
        config = load_config(file_name)
        if config is None:
            response.status = 404
            return {'error': 'Configuration file not found.'}
        # Reload logic can be added here, e.g., update global variables or restart services.
        return {'message': 'Configuration reloaded successfully.'}
    except Exception as e:
        response.status = 400
        return {'error': str(e)}

# Start the Bottle server.
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)