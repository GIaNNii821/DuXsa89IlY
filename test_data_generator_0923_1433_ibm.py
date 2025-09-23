# 代码生成时间: 2025-09-23 14:33:22
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test_data_generator.py
# A simple Bottle web application that serves as a test data generator.

from bottle import route, run, request, response
import json
import random
import string


# Configuration
PORT = 8080
HOST = 'localhost'

# Create a dictionary to store the data types and their corresponding generators
DATA_TYPES = {
    'string': lambda length: ''.join(random.choices(string.ascii_letters + string.digits, k=length)),
    'integer': lambda: random.randint(1, 100),  # Random integer between 1 and 100
    'float': lambda: round(random.uniform(1.0, 100.0), 2),  # Random float between 1.0 and 100.0 with 2 decimal places
}


# Route to generate a single test data item
@route('/generate/<type>')
def generate_test_data(type):
    # Check if the requested data type is supported
    if type not in DATA_TYPES:
        response.status = 404
        return {'error': 'Unsupported data type'}

    try:
        # Generate the test data
        data = DATA_TYPES[type]()
        return {'data': data}
    except Exception as e:
        # Handle any unexpected errors
        response.status = 500
        return {'error': str(e)}


# Route to generate a list of test data items
@route('/generate/<type>/<count>')
def generate_test_data_list(type, count):
    if type not in DATA_TYPES:
        response.status = 404
        return {'error': 'Unsupported data type'}

    try:
        # Convert count to an integer
        count = int(count)
        # Generate a list of test data
        data_list = [DATA_TYPES[type]() for _ in range(count)]
        return {'data': data_list}
    except ValueError:
        response.status = 400
        return {'error': 'Invalid count value'}
    except Exception as e:
        response.status = 500
        return {'error': str(e)}


# Start the Bottle server
if __name__ == '__main__':
    run(host=HOST, port=PORT, debug=True)