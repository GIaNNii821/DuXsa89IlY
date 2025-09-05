# 代码生成时间: 2025-09-06 00:59:56
from bottle import route, run, response, request
from urllib.parse import urlparse
import requests

"""
URL Validator Application

This Bottle application is a simple web server that validates the
effectiveness of a given URL. It checks if the URL exists and is reachable.
"""

# Function to validate URL
def is_valid_url(url):
    """
    Check if a URL is valid by attempting to make an HTTP request.
    :param url: The URL to be validated.
    :return: True if the URL is valid, False otherwise.
    """
    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc]):
            response = requests.head(url, allow_redirects=True, timeout=5)
            return response.status_code == 200
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Route for URL validation
@route('/validate', method='POST')
def validate_url():
    """
    Endpoint to validate a URL. Expects a JSON payload with a single key 'url'.
    :return: A JSON response indicating the validity of the URL.
    """
    # Parse JSON data from the request
    try:
        data = request.json
        url = data.get('url')
        if not url:
            response.status = 400
            return {"error": "No URL provided."}

        # Validate the URL
        if is_valid_url(url):
            return {"message": "URL is valid."}
        else:
            return {"error": "URL is invalid or unreachable."}
    except Exception as e:
        response.status = 500
        return {"error": str(e)}

# Run the Bottle application
if __name__ == '__main__':
    run(host='localhost', port=8080)