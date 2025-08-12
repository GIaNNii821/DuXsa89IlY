# 代码生成时间: 2025-08-13 07:42:44
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple math calculator tool using Bottle framework.
"""

from bottle import route, run, request, response
import math


# Define a route for the math calculator API
@route('/math/<operation>/<number1:float>/<number2:float>')
def calculate(operation, number1, number2):
    """
    Perform mathematical operations based on the operation parameter.
    Supported operations are: add, subtract, multiply, divide, power, root.
    """
    # Set the response content type to JSON
    response.content_type = 'application/json'
    
    # Initialize the result variable
    result = None
    
    # Perform the requested operation
    if operation == 'add':
        result = number1 + number2
    elif operation == 'subtract':
        result = number1 - number2
    elif operation == 'multiply':
        result = number1 * number2
    elif operation == 'divide':
        # Check for division by zero
        if number2 == 0:
            return {"error": "Cannot divide by zero."}
        result = number1 / number2
    elif operation == 'power':
        result = math.pow(number1, number2)
    elif operation == 'root':
        # Check for negative numbers under even roots
        if number1 < 0 and math.isclose(math.fmod(number2, 2), 0):
            return {"error": "Cannot calculate the root of a negative number."}
        result = math.pow(number1, 1.0 / number2)
    else:
        return {"error": "Unsupported operation."}
    
    # Return the result in JSON format
    return {"result": result}


# Run the Bottle server on port 8080
run(host='localhost', port=8080)