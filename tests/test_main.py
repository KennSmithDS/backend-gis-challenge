from fastapi.testclient import TestClient
from main import app
from .test_requests import *
import pytest
import json

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

def test_calculate_properties_valid_request():
    """Method to test /calculate_properties endpoint is successful with status code 200."""
    server_response = test_app.post('/calculate_properties', content=json.dumps(request_body_200))
    assert server_response.json() == response_body_200

def test_calculate_properties_invalid_request_not_feature():
    """Method to test /calculate_properties endpoint receive ValidationError when request body not valid GeoJSON Feature."""
    server_response = test_app.post('/calculate_properties', content=json.dumps(request_body_not_feature))
    assert server_response.status_code == 400

def test_calculate_properties_invalid_request_not_poly():
    """Method to test /calculate_properties endpoint receive ValidationError when GeoJSON Feature geometry is not Polygon type."""
    server_response = test_app.post('/calculate_properties', content=json.dumps(request_body_not_poly))
    assert server_response.status_code == 400

def test_calculate_properties_invalid_request_not_multipoly():
    """Method to test /calculate_properties endpoint receive ValidationError when GeoJSON Feature geometry is not MultiPolygon type."""
    server_response = test_app.post('/calculate_properties', content=json.dumps(request_body_not_multipoly))
    assert server_response.status_code == 400