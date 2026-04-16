from task1 import *

def test_too_big_age():
    json_input = """{
            "name": "John Doe",
            "age": 200,
            "email": "john.doe@example.com",
            "is_employed": false,
            "address": {
                "city": "New York",
                "street": "5th Avenue",
                "house_number": 123
            }
        }"""
    try:
        validate_user(json_input)
        assert False
    except ValidationError as e:
        assert "Input should be less than or equal to 120" in str(e)

def test_too_small_age():
    json_input = """{
            "name": "John Doe",
            "age": -5,
            "email": "john.doe@example.com",
            "is_employed": true,
            "address": {
                "city": "New York",
                "street": "5th Avenue",
                "house_number": 123
            }
        }"""
    try:
        validate_user(json_input)
        assert False
    except ValidationError as e:
        assert "Input should be greater than or equal to 0" in str(e)

def test_wrong_age():
    json_input = """{
            "name": "John Doe",
            "age": 70,
            "email": "john.doe@example.com",
            "is_employed": true,
            "address": {
                "city": "New York",
                "street": "5th Avenue",
                "house_number": 123
            }
        }"""
    try:
        validate_user(json_input)
        assert False
    except ValidationError as e:
        assert "Age must be between 18 and 65" in str(e)