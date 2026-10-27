#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:42:11 2026

@author: manonkling
"""

# Import Flask tools
from flask import Flask, request, jsonify

# Create the Flask application
app = Flask(__name__)


# GET endpoint: Returns a personalized greeting
@app.route('/hello', methods=['GET'])
def hello():
    # Get the name from the URL, or use "World" as the default
    name = request.args.get('name', 'World')

    # Return the greeting as JSON
    return jsonify({"message": f"Hello, {name}!"}), 200


# POST endpoint: Adds numbers from a JSON list
@app.route('/sum', methods=['POST'])
def calculate_sum():
    # Check that the request contains JSON
    if not request.is_json:
        return jsonify({"error": "Request must contain JSON"}), 400

    # Read the JSON data
    data = request.get_json(silent=True)

    # Check that the JSON contains a list of numbers
    if not isinstance(data, dict) or "numbers" not in data:
        return jsonify({"error": "Missing 'numbers' field"}), 400

    numbers = data["numbers"]

    # Validate the numbers
    if not isinstance(numbers, list):
        return jsonify({"error": "'numbers' must be a list"}), 400

    if not all(type(num) in (int, float) for num in numbers):
        return jsonify({"error": "All items must be numbers"}), 400

    # Calculate and return the sum
    total = sum(numbers)

    return jsonify({"sum": total}), 200


# Start the Flask server on port 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    