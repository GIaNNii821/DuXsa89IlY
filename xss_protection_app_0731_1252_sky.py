# 代码生成时间: 2025-07-31 12:52:42
#!/usr/bin/env python

"""
XSS Protection Application using Bottle framework.

This application demonstrates how to protect against XSS (Cross-Site Scripting) attacks
by sanitizing user input.
"""

from bottle import route, run, request, template, response
import html

# XSS protection function
def xss_protect(data):
    """Sanitize input to prevent XSS attacks."""
    return html.escape(data)

# Home route
@route('/')
def home():
    """
    This route handles the home page request.
    It provides an input form for the user to submit data.
    The submitted data is then sanitized and displayed back.
    """
    return template("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>XSS Protection Demo</title>
    </head>
    <body>
        <h1>XSS Protection Demo</h1>
        <form action="/submit" method="post">
            <input type="text" name="user_input" placeholder="Enter your input here..." required>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    """)

# Submit route
@route('/submit', method='POST')
def submit():
    """
    This route handles the form submission.
    It retrieves the user input, sanitizes it to prevent XSS,
    and then returns the sanitized input.
    """
    try:
        # Get user input from the form
        user_input = request.forms.get('user_input')
        # Sanitize the input to prevent XSS
        sanitized_input = xss_protect(user_input)
        # Return the sanitized input
        return template("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>XSS Protection Result</title>
        </head>
        <body>
            <h1>XSS Protection Result</h1>
            <p>Your sanitized input: {{ sanitized_input }}</p>
        </body>
        </html>
        """, sanitized_input=sanitized_input)
    except Exception as e:
        # Handle any exceptions that may occur
        return f"An error occurred: {e}", 500

# Run the application
if __name__ == '__main__':
    run(host='localhost', port=8080)
