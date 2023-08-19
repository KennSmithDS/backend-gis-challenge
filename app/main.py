from fastapi import FastAPI
from typing import Dict

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
def calculate_properties():
    """
    """
    pass