import FastAPI, Request
from typing import Union, Dict, List, Type

JSON = Union[Dict[str, 'JSON'], List['JSON'], int, str, float, bool, Type[None]]

# Define application
app = FastAPI(
    title="Babushka",
    description="Testing",
    version="0.1",
)

def wrapper():
    pass

@app.get("/")
def _index(request: Request) -> JSON:
    response={}

    return response