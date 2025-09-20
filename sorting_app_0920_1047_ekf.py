# 代码生成时间: 2025-09-20 10:47:24
#!/usr/bin/env python

# This is a simple sorting application using the Bottle framework.
# It uses a simple sorting algorithm to sort a list of numbers.

from bottle import route, run, request
from typing import List

"""
    This function sorts a list of integers in ascending order.

    :param numbers: A list of integers to be sorted.
    :return: A sorted list of integers.
"""
def bubble_sort(numbers: List[int]) -> List[int]:
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap the elements
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

"""
    This function validates if the input is a list of integers.

    :param input_list: The input list to validate.
    :return: True if the input is a valid list of integers, False otherwise.
"""
def validate_input(input_list: List[int]) -> bool:
    return all(isinstance(item, int) for item in input_list)


@route('/sort', method='POST')
def sort_numbers():
    """
        This endpoint sorts a list of numbers provided through POST request.

        :return: A JSON response with the sorted list of numbers.
        :raises: HTTPError with a 400 status code if the input is invalid.
    """
    try:
        # Get the list of numbers from the request body
        numbers = request.json.get('numbers', [])
        # Validate the input
        if not validate_input(numbers):
            return {'error': 'Invalid input. Please provide a list of integers.'}
        # Sort the numbers
        sorted_numbers = bubble_sort(numbers)
        # Return the sorted list as a JSON response
        return {'sorted_numbers': sorted_numbers}
    except Exception as e:
        # Return a generic error message if any other exception occurs
        return {'error': 'An error occurred while sorting the numbers.'}

# Run the Bottle development server on localhost port 8080
run(host='localhost', port=8080)