from fastapi.testclient import TestClient 
from datetime import datetime
from functools import wraps
from http import HTTPStatus
from typing import Dict, Optional 
from fastapi import FastAPI, Request

# Define application
app = FastAPI(
    title="TagIfAI - Made With ML",
    description="Predict relevant tags given a text input.",
    version="0.1",
)

def construct_response(f):
    @wraps(f)
    def wrap(request: Request, *args, **kwargs):
        results = f(request, *args, **kwargs)

        # Construct response
        response = {
            "message": results["message"],
            "method": request.method,
            "status-code": results["status-code"],
            "timestamp": datetime.now().isoformat(),
            "url": request.url._url,
        }

        # Add data
        if "data" in results:
            response["data"] = results["data"]

        return response
    return wrap


@app.get("/", tags=["General"])
@construct_response
def _index(request: Request):
    """Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response

# Interface
from fastapi.testclient import TestClient
client = TestClient(app)

def test_api_command():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK

test_api_command()
