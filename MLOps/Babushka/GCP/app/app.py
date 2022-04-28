from fastapi import FastAPI, Request

from functools import wraps
from typing import Union, Dict, List, Type

from babushka import main

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


def load_artifacts():
    pass


def response():
    # https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
    @wraps(f) 
    def wrap():
        pass
    
    return wrap

@response
def predict():
    pass

@response
def _params():
    pass

@response
def peformance():
    pass