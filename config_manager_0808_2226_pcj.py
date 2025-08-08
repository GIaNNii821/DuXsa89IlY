# 代码生成时间: 2025-08-08 22:26:17
from bottle import route, run, request, response, template
import json
import os

# Define the root directory for the configuration files
CONFIG_DIR = 'configs'

# Check if the config directory exists, if not create it
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

# Load a configuration file
def load_config(file_name):
    config_file_path = os.path.join(CONFIG_DIR, file_name)
    try:
        with open(config_file_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

# Save a configuration file
def save_config(file_name, config_data):
    config_file_path = os.path.join(CONFIG_DIR, file_name)
    try:
        with open(config_file_path, 'w') as config_file:
            json.dump(config_data, config_file, indent=4)
    except Exception as e:
        raise Exception(f"Failed to save configuration: {e}")

# Bottle route to get configuration
@route('/get/<file_name>', method='GET')
def get_config(file_name):
    try:
        config_data = load_config(file_name)
        response.content_type = 'application/json'
        return json.dumps(config_data)
    except Exception as e:
        return f"Error getting configuration: {e}", 500

# Bottle route to set configuration
@route('/set/<file_name>', method='POST')
def set_config(file_name):
    try:
        config_data = request.json
        save_config(file_name, config_data)
        return f"Configuration for {file_name} updated successfully."
    except Exception as e:
        return f"Error setting configuration: {e}", 500

# Run the Bottle server
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)