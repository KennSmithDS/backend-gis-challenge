from fastapi import FastAPI, HTTPException
from typing import Dict
from copy import deepcopy
from src.models import RequestBody, ResponseBody
from src.geo_utils import *
from src.exceptions import InvalidGeoJSON, UnsupportedGeometryType

app = FastAPI()

@app.get("/")
def api_root() -> Dict[str, str]:
    """Helper method to test the status of the root API path.
    
    Args:
        None.
    
    Returns:
        Dict[str, str]: A dictionary response that indicates the root path is available.
    """
    return {"API Message": "Successful response from the backend root path."}

@app.post("/calculate_properties")
def calculate_properties(request_body: Dict[str, Any]):
    """

    Parameters:
        request_body Dict[str, Any]: A dictionary request body from the client.
    Returns:
        ResponseBody: A pydantic model type with expected new properties for response body.
    """
    # Validate the request body as GeoJSON Feature
    if validate_feature(request_body):
        # Make a copy of request body for response body
        response_body = deepcopy(request_body)
        
        # Convert the GeoJSON geometry into shapely geometry object
        shapely_geometry = get_shapely_geometry(request_body['geometry'])

        # Transform the CRS projection of the shapely object from 4326 to 3857
        transformed_geometry = transform_projection(shapely_geometry)
        # Calculate and add the area property to response body
        response_body['properties']['area'] = {
            "value": get_area(transformed_geometry),
            "unit": "sq meters"
        }

        # Calculate and add the centroid property to response body
        response_body['properties']['centroid'] = get_geojson_geometry(
            get_centroid(shapely_geometry)
        )

        # Calculate and add the bbox property to response body
        response_body['bbox'] = get_bbox(shapely_geometry)

        # Validate response body has required properties
        try:
            valid_response_body = ResponseBody(**response_body)
        except ValidationError as ve:
            print(ve)

        # return the response body
        return valid_response_body
    else:
        raise InvalidGeoJSON(
            status_code=400,
            detail='Request body is not a valid GeoJSON Feature.'
            )
        
