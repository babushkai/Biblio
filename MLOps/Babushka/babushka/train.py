
import itertools
import json
from argparse import Namespace
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import optuna
import pandas as pd
import torch
import torch.nn as nn
from numpyencoder import NumpyEncoder
from sklearn.metrics import precision_recall_curve

from config import config
from config.config import logger
from babushka import data, models, utils


class Trainer:
    pass

    def train(self):
        pass

    def objective():
        pass