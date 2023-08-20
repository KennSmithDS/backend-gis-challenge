from geojson_pydantic import Feature, Polygon, MultiPolygon
from shapely.geometry import shape, mapping, Point, polygon, multipolygon
from shapely.ops import transform
from pydantic import ValidationError
from pyproj.transformer import Transformer
from typing import Any, Dict, List, Optional, Union
from .exceptions import InvalidGeoJSON, UnsupportedGeometryType, InvalidGeometry

def validate_feature(request_payload: Dict[str, Any]) -> bool:
    """Helper method to validate if a request payload is a GeoJSON Feature, and if the geometry type is Polygon or MultiPolygon.
    
    Parameters:
        request_payload:
            Dict[str, Any]: A dictionary GeoJSON object to be validated.
    
    Returns:
        bool: True if the object is a valid GeoJSON Feature and is either Polygon or MultiPolygon type.
    
    Raises:
        InvalidGeoJSON: HTTPException error raised when request body is not a valid GeoJSON Feature.
        UnsupportedGeometryType: HTTPException error raised when the GeoJSON Feature is not a Polygon or MultiPolygon
        InvalidGeometry: HTTPException error raised when the GeoJSON Feature geometry is not a Polygon or MultiPolygon
    """
    
    try:
        # Check if object has properties property for Feature validation
        if 'properties' not in request_payload.keys():
            request_payload['properties'] = {}
        
        # Validate if JSON object is valid GeoJSON Feature
        feature = Feature(**request_payload)

        # Extract the geometry property from GeoJSON Feature
        if 'geometry' in request_payload.keys():
            geometry = request_payload['geometry']

            # Check if the geometry is either Polygon or MultiPolygon type
            assert geometry['type'] in ['Polygon','MultiPolygon']

            if geometry['type'] == 'Polygon':
                return is_polygon(geometry)
            elif geometry['type'] == 'MultiPolygon':
                return is_multipolygon(geometry)
    
    # If request payload is not a valid GeoJSON Feature
    except ValidationError as ve:
        raise InvalidGeoJSON(
            status_code=400,
            detail="Request payload is not a valid GeoJSON Feature."
        )
    
    # If not Feature is neither Polygon nor MultiPolygon type, return False
    except AssertionError as ae:
        raise UnsupportedGeometryType(
            status_code=400,
            detail="GeoJSON Feature type is not supported by the API, only Polygon and Multipolygon are accepted types."
        )

def is_polygon(geometry: Dict[str, Any]) -> bool:
    """Helper function to validate Feature is a Polygon.

    Parameters:
        geometry Dict[str, Any]: A dictionary object representing the `geometry` property of the GeoJSON Feature.
    Returns:
        bool: True if the geometry is a valid Polygon.
    Raises:
        ValidationError: if the geometry is not a valid Polygon.
    """
    try:
        return isinstance(Polygon(**geometry), Polygon)
    except ValidationError as ve:
        raise InvalidGeometry(
            status_code=400,
            detail="GeoJSON Feature geometry object is not a valid Polygon object."
        )

def is_multipolygon(geometry: Dict[str, Any]) -> bool:
    """Helper function to validate Feature is a MultiPolygon.

    Parameters:
        geometry Dict[str, Any]: A dictionary object representing the `geometry` property of the GeoJSON Feature.
    Returns:
        bool: True if the geometry is a valid MultiPolygon.
    Raises:
        ValidationError: if the geometry is not a valid MultiPolygon.
    """
    try:
        return isinstance(MultiPolygon(**geometry), MultiPolygon)
    except ValidationError as ve:
        raise InvalidGeometry(
            status_code=400,
            detail="GeoJSON Feature geometry object is not a valid MultiPolygon object."
        )

def get_shapely_geometry(feature_geometry: Dict[str, Any]) -> Union[polygon.Polygon, multipolygon.MultiPolygon]:
    """Helper function to convert the GeoJSON Feature geometry property to a shapely object.

    Parameters:
        feature_geometry Dict[str, Any]: A dictionary from a GeoJSON object's geometry property
    Returns:
        Union[polygon.Polygon, multipolygon.MultiPolygon]: shapely Polygon or MultiPolygon object
    """
    return shape(feature_geometry)

def get_geojson_geometry(shapely_geometry: Union[polygon.Polygon, multipolygon.MultiPolygon]) -> Dict[str, Any]:
    """Helper function to convert a shapely geometry object into GeoJSON Feature geometry.

    Parameters:
        shapely_geometry Union[polygon.Polygon, multipolygon.MultiPolygon]: shapely Polygon or MultiPolygon object
    Returns:
        Dict[str, Any]: A dictionary format of GeoJSON geometry object
    """
    return mapping(shapely_geometry)

def transform_projection(
    input_geometry: Union[polygon.Polygon, multipolygon.MultiPolygon],
    input_crs: Optional[str] = '4326', # WGS 84 lat/long
    output_crs: Optional[str] = '3857' # Web Mercator
) -> Union[polygon.Polygon, multipolygon.MultiPolygon]:
    """Method to transform the projection of the input geometry from request payload to another CRS. 
    Assumption is made that the input CRS is in latitude and longitude coordinates in EPSG 4326 by default, 
    and the output needs to be transformed to Web Mercator EPSG 3857 which is a meter based projection.

    Parameters:
        input_geometry Union[Polygon, MultiPolygon]: A shapely object to transform projection
        input_crs str: string value of the input CRS
        output_crs str: string value of the output CRS
    Returns:
        output_geometry Union[polygon.Polygon, multipolygon.MultiPolygon]
    """
    # Instantiate the pyproj transformer
    geometry_transformer = Transformer.from_crs(
        crs_from=input_crs, 
        crs_to=output_crs,
        always_xy=True
    ).transform

    # Transform the shapely geometry object from input to output CRS
    output_geometry = transform(geometry_transformer, input_geometry)
    return output_geometry

def get_area(geometry_shape: Union[polygon.Polygon, multipolygon.MultiPolygon]) -> float:
    """Method to calculate the area of a geometry from request body in square meters.

    Parameters:
        geometry_shape Union[polygon.Polygon, multipolygon.MultiPolygon]: shapely object
    Returns:
        float value for the area of the shapely object's geometry
    """
    return geometry_shape.area

def get_centroid(geometry_shape: Union[polygon.Polygon, multipolygon.MultiPolygon]) -> Point:
    """Method to find the centroid Point of a geometry from request body.

    Parameters:
        geometry_shape Union[polygon.Polygon, multipolygon.MultiPolygon]: shapely object
    Returns:
        Point object that contains the XY coordinates of the geometry's centroid
    """
    return geometry_shape.centroid

def get_bbox(geometry_shape: Union[polygon.Polygon, multipolygon.MultiPolygon]) -> List[float]:
    """Method to find the bounding box of a geometry from request body.

    Parameters:
        geometry_shape Union[polygon.Polygon, multipolygon.MultiPolygon]: shapely object
    Returns:
        List[float]: set of minX, minY, maxX, maxY coordinates for the bounding box
    """
    return list(geometry_shape.bounds)