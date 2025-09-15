# 代码生成时间: 2025-09-15 21:30:04
from bottle import route, run, request, HTTPError
import json

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Bottle route to handle GET requests
@route('/sort', method='GET')
def sort_numbers():
    """Sorts a list of numbers using Bubble Sort algorithm.
       Returns the sorted list in JSON format."""
    try:
        # Get the query parameters
        arr = request.query.get('numbers')
        if not arr:
            raise HTTPError(400, 'No numbers provided for sorting.')
        
        # Convert the query parameter to a list of integers
        numbers = [int(x) for x in arr.split(',')]
        
        # Sort the list using Bubble Sort
        sorted_numbers = bubble_sort(numbers)
        
        # Return the sorted list as JSON
        return json.dumps({'sorted_numbers': sorted_numbers})
    except ValueError:
        raise HTTPError(400, 'Invalid numbers provided. Please provide a comma-separated list of integers.')
    except Exception as e:
        raise HTTPError(500, 'An unexpected error occurred: ' + str(e))

# Start the Bottle server
if __name__ == '__main__':
    run(host='localhost', port=8080)