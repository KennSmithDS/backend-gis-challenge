from src.geo_utils import *
from .test_requests import request_body_200
from shapely.geometry import Polygon, mapping
import json

def test_get_shapely_geometry():
    """Method to test conversion from GeoJSON geometry to shapely shape object."""
    shapely_geometry = get_shapely_geometry(request_body_200['geometry'])
    assert isinstance(shapely_geometry, Polygon)

def test_get_geojson_geometry():
    """Method to test conversion from shapely shape object to GeoJSON geometry."""
    shapely_geometry = get_shapely_geometry(request_body_200['geometry'])
    geojson_geometry = get_geojson_geometry(shapely_geometry)
    assert isinstance(geojson_geometry, dict)

    # Unable to assert that the input GeoJSON equaled the output GeoJSON
    # Sorted_input = dict(sorted(request_body_200['geometry'].items()))
    # Sorted_output = dict(sorted(geojson_geometry.items()))
    # Assert json.dumps(sorted_input) == json.dumps(sorted_output)

def test_transform_projection():
    """Method to test reprojection from EPSG:4326 to EPSG:3857."""
    web_mercator_object = '{"type": "Polygon", "coordinates": [[[0.0, 0.0], [0.0, 111325.1428663851], [111319.49079327357, 111325.1428663851], [111319.49079327357, 0.0], [0.0, 0.0]]]}'
    shapely_geometry = get_shapely_geometry(request_body_200['geometry'])
    transformed_geometry = transform_projection(shapely_geometry)
    assert isinstance(transformed_geometry, Polygon)
    assert json.dumps(mapping(transformed_geometry)) == web_mercator_object

def test_get_area():
    """Method to test area calculation in squared meters."""
    shapely_geometry = get_shapely_geometry(request_body_200['geometry'])
    transformed_geometry = transform_projection(shapely_geometry)
    transformed_area = get_area(transformed_geometry)
    assert isinstance(transformed_area, float)
    assert transformed_area == 12392658216.37442

def test_get_centroid():
    """Method to test centroid calculation."""
    shapely_geometry = get_shapely_geometry(request_body_200['geometry'])
    input_centroid = get_centroid(shapely_geometry)
    output_centroid = '{"type": "Point", "coordinates": [0.5, 0.5]}'
    assert json.dumps(mapping(input_centroid)) == output_centroid

def test_get_bbox():
    """Method to test bounding box conversion."""
    shapely_geometry = get_shapely_geometry(request_body_200['geometry'])
    input_bbox = get_bbox(shapely_geometry)
    output_bbox = [0, 0, 1, 1]
    assert isinstance(input_bbox, list)
    assert input_bbox == output_bbox