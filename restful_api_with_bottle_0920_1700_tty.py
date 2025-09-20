# 代码生成时间: 2025-09-20 17:00:57
# restful_api_with_bottle.py
# This script creates a RESTful API using the Bottle framework.

from bottle import route, run, request, response, error

# Create a Bottle application instance
app = application = default_app = Bottle()

# Define the data store for simplicity
data_store = {
    "users": [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]
}

# Route for getting all users
@route('/users', method='GET')
def get_users():
    """
    GET request handler for retrieving all users.
    """
    return data_store["users"]

# Route for getting a single user by id
@route('/users/<id:int>', method='GET')
def get_user(id):
    """
    GET request handler for retrieving a single user by id.
    """
    user = next((user for user in data_store["users"] if user["id"] == id), None)
    if user is not None:
        return user
    else:
        response.status = 404
        return {"error": "User not found"}

# Route for creating a new user
@route('/users', method='POST')
def create_user():
    """
    POST request handler for creating a new user.
    """
    try:
        new_user = request.json
        if not new_user or 'name' not in new_user:
            response.status = 400
            return {"error": "Missing name in request data"}
        # Assign a new id to the user
        new_user["id"] = max(user["id"] for user in data_store["users"]) + 1
        data_store["users"].append(new_user)
        response.status = 201
        return new_user
    except:
        response.status = 500
        return {"error": "Internal server error"}

# Route for updating a user by id
@route('/users/<id:int>', method='PUT')
def update_user(id):
    """
    PUT request handler for updating a user by id.
    """
    user = next((user for user in data_store["users"] if user["id"] == id), None)
    if user:
        user.update(request.json)
        return user
    else:
        response.status = 404
        return {"error": "User not found"}

# Route for deleting a user by id
@route('/users/<id:int>', method='DELETE')
def delete_user(id):
    """
    DELETE request handler for deleting a user by id.
    """
    user = next((user for user in data_store["users"] if user["id"] == id), None)
    if user:
        data_store["users"].remove(user)
        response.status = 204
        return ""  # No content for DELETE
    else:
        response.status = 404
        return {"error": "User not found"}

# Error handler for 404 errors
@error(404)
def error_404(error):
    """
    Error handler for 404 not found errors.
    """
    return {"error": "Resource not found"}, 404

# Run the application
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)