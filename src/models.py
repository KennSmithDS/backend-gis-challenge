from pydantic import BaseModel
from geojson_pydantic import Polygon, MultiPolygon
from typing import Dict, Any, List, Tuple, Union

class RequestBody(BaseModel):
    type: str
    geometry: Dict[str, Any]
    properties: Dict[str, Any] | None = None

class ResponseBody(BaseModel):
    type: str
    geometry: Dict[str, Any]
    properties: Dict[str, Any] | None = None
    bbox: List[float]