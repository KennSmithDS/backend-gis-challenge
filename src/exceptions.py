from fastapi import HTTPException

class InvalidGeoJSON(HTTPException):
    """Raised when the request body is not a valid GeoJSON Feature"""
    pass

class UnsupportedGeometryType(HTTPException):
    """Raised when the request body is a valid GeoJSON Feature but not supported shape type, i.e. Polygon and Multipolygon."""

class InvalidGeometry(HTTPException):
    """Raised when the request body is a valid GeoJSON Feature but the geometry object is an invalid POlygon or MultiPolygon."""