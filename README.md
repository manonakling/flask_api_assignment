#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:51:48 2026

@author: manonkling
"""

# Flask API Assignment

## Project Overview

This project demonstrates the development of a basic REST API
using Python and the Flask framework.

The application includes two endpoints that demonstrate
HTTP requests, JSON data handling, Python functions,
control flow, and error handling.

## Technologies Used

- Python 3
- Flask
- pytest
- REST API
- JSON

## Project Structure

flask_api_assignment/
    app.py
    test_app.py
    README.md

## API Endpoints

### GET /hello

Returns a greeting in JSON format.

Example request:

GET http://127.0.0.1:5000/hello?name=Manon

Expected response:

{
    "message": "Hello, Manon!"
}

If no name is provided, the API returns:

{
    "message": "Hello, World!"
}

### POST /sum

Accepts a JSON list of numbers and returns their sum.

Example request:

POST http://127.0.0.1:5000/sum

Example JSON payload:

{
    "numbers": [1, 2, 3]
}

Expected response:

{
    "sum": 6
}

## Error Handling

The application validates incoming requests and returns
HTTP status code 400 when invalid data is submitted.

Examples of invalid requests include:

- Missing numbers field
- Invalid data types
- Malformed JSON
- Non-numeric values

## Installation Instructions

### 1. Clone the Repository

git clone <repository-url>

cd flask_api_assignment

### 2. Create a Virtual Environment

python -m venv venv

### 3. Activate the Virtual Environment

Mac/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

### 4. Install Dependencies

python -m pip install Flask pytest

## Running the Application

Start the Flask server:

python app.py

The application runs locally at:

http://127.0.0.1:5000

## Testing the Application

Run automated tests using:

pytest test_app.py

The application includes six automated tests that
verify successful requests and error handling.

Expected test outcome:

6 passed

## Learning Outcomes

This project demonstrates:

- Building REST API endpoints with Flask
- Handling HTTP GET and POST requests
- Processing JSON data
- Using Python functions and conditional statements
- Manipulating lists and dictionaries
- Implementing HTTP error responses
- Writing automated tests with pytest
- Running a local development server

## Conclusion

This assignment provides practical experience
developing and testing a basic Flask REST API.

The application demonstrates fundamental Python
programming concepts and introductory API development
skills relevant to interoperability between systems.