import itertools
import json
import re
from argparse import Namespace
from collections import Counter
from pathlib import Path
from typing import List, Sequence, Tuple

import numpy as np
import pandas as pd
import torch
from nltk.stem import PorterStemmer
from skmultilearn.model_selection import IterativeStratification

from config import config
from tagifai import utils


def filter_name():
    pass

def compute_features():
    """Compute features to use for training.
    Args:
        params (Namespace): Input parameters for operations.
    """
    utils.set_seed(seed=params.seed)

    # Load data
    projects = utils.load_dict(filepath=Path(config.DATA_DIR, "projects.json"))
    df = pd.DataFrame(projects)

    # Compute features
    df["text"] = df.title + " " + df.description
    df.drop(columns=["title", "description"], inplace=True)
    df = df[["id", "created_on", "text", "tags"]]

    # Save
    features = df.to_dict(orient="records")
    df_dict_fp = Path(config.DATA_DIR, "features.json")
    utils.save_dict(d=features, filepath=df_dict_fp)

    return df, features

def prepare():
    pass

def preprocess():
    pass

class Sample:
    pass

class Sample2:
    pass