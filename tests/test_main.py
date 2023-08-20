from fastapi.testclient import TestClient
from app.main import app
from .test_requests import *
import pytest

test_app = TestClient(app)

def test_api_root():
    """Method to test the root API path is successful with status code 200."""
    root_response = {"API Message": "Successful response from the backend root path."}
    server_response = test_app.get('/')
    assert server_response.status_code == 200
    assert server_response.json() == root_response

def test_invalid_endpoint():
    """Method to test when an invalid endpoint is requested from the server."""
    server_response = test_app.get('/invalid-endpoint')
    assert server_response.status_code == 404

def test_valid_request():
    pass

def test_invalid_request_not_feature():
    pass

def test_invalid_request_not_poly_mpoly():
    pass