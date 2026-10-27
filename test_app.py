#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:47:50 2026

@author: manonkling
"""

# Import the Flask application
from app import app

# Create a test client to simulate HTTP requests
import pytest


@pytest.fixture
def client():
    # Configure Flask for testing
    app.config["TESTING"] = True

    # Create and return a test client
    with app.test_client() as client:
        yield client


# Test 1: Check the default greeting
def test_hello_default(client):
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


# Test 2: Check a personalized greeting
def test_hello_name(client):
    response = client.get("/hello?name=Manon")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Manon!"}


# Test 3: Check that numbers are added correctly
def test_sum_valid(client):
    response = client.post(
        "/sum",
        json={"numbers": [1, 2, 3]}
    )

    assert response.status_code == 200
    assert response.get_json() == {"sum": 6}


# Test 4: Check for missing numbers
def test_sum_missing(client):
    response = client.post(
        "/sum",
        json={}
    )

    assert response.status_code == 400
    assert "error" in response.get_json()


# Test 5: Check for invalid numbers
def test_sum_invalid(client):
    response = client.post(
        "/sum",
        json={"numbers": ["apple", "banana"]}
    )

    assert response.status_code == 400
    assert "error" in response.get_json()


# Test 6: Check for malformed JSON
def test_sum_malformed(client):
    response = client.post(
        "/sum",
        data='{"numbers": [1, 2,}',
        content_type="application/json"
    )

    assert response.status_code == 400
    assert "error" in response.get_json()