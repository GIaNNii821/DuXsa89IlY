# 代码生成时间: 2025-09-12 06:07:51
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
URL Validator Application using Bottle Framework

This application is used to validate the URL links. It checks whether the URL is valid or not.
"""

from bottle import route, run, request, HTTPError
import urllib.parse
from urllib.parse import urlparse, parse_qs
import requests

# Define the function to validate URL
def is_valid_url(url):
    """
    Checks if the URL is valid by parsing it and checking its scheme and netloc.
    
    Args:
        url (str): The URL to validate.
    
    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

# Define the API endpoint to validate URL
@route('/validate_url', method='POST')
def validate_url():
    """
    Validates the URL received in the POST request body.
    
    Returns:
        JSON response with URL validity status.
    """
    try:
        # Get the URL from the request body
        data = request.json
        url = data.get('url')
        
        # Check if URL is provided
        if not url:
            raise HTTPError(400, 'URL is required')
        
        # Validate the URL
        if is_valid_url(url):
            return {'status': 'success', 'message': 'URL is valid'}
        else:
            return {'status': 'error', 'message': 'URL is invalid'}
    except HTTPError as e:
        return {'status': 'error', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': 'An unexpected error occurred'}

# Run the Bottle application
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)