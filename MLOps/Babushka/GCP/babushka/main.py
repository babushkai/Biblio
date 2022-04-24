# Main operations with Command line interface (CLI).
# CLI application

import json
import tempfile
import warnings
from argparse import Namespace
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

import mlflow
import optuna
import pandas as pd
import tensorflow 
import typer
from feast import FeatureStore
from numpyencoder import NumpyEncoder
from optuna.integration.mlflow import MLflowCallback

from config import config
from config.config import logger
from orchestrator import dag1
from babushka import data, models, predict, train, utils 

# Ignore warning
warnings.fiterwarnings("ignore")

# Typer CLI app
app = typer.Typer()

@app.command()
def download_auxiliary_data():
    print("test")

@app.command()
def trigger_orchestrator():
    

@app.command()
def compute_features(params_fp: Path = Path(config.CONFIG_DIR, "params.json"),) -> None:
    """Compute and save features for training.
    Args:
        params_fp (Path, optional): Location of parameters (just using num_samples,
                                    num_epochs, etc.) to use for training.
                                    Defaults to `config/params.json`.
    """
    # Parameters
    params = Namespace(**utils.load_dict(filepath=params_fp))

    # Compute features
    data.compute_features(params=params)
    logger.info("✅ Computed features!")

@app.command()
def trainer():
    pass

@app.command()
def load_artifacts():
    model = models.load_model()
    pass