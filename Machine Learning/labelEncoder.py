import json
import re
from collections import Counter
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class LabelEncoder:
    """Encode labels into unique indices.
    ```python
    # Encode labels
    label_encoder = LabelEncoder()
    label_encoder.fit(labels)
    y = label_encoder.encode(labels)
    ```
    """

    def __init__(self, class_to_index: Dict = {}) -> None:
        """Initialize the label encoder.
        Args:
            class_to_index (Dict, optional): mapping between classes and unique indices. Defaults to {}.
        """
        self.class_to_index = class_to_index or {}  # mutable defaults ;)
        self.index_to_class = {v: k for k, v in self.class_to_index.items()}
        self.classes = list(self.class_to_index.keys())

    def __len__(self):
        return len(self.class_to_index)

    def __str__(self):
        return f"<LabelEncoder(num_classes={len(self)})>"

    def fit(self, y: List):
        """Fit a list of labels to the encoder.
        Args:
            y (List): raw labels.
        Returns:
            Fitted LabelEncoder instance.
        """
        classes = np.unique(y)
        for i, class_ in enumerate(classes):
            self.class_to_index[class_] = i
        self.index_to_class = {v: k for k, v in self.class_to_index.items()}
        self.classes = list(self.class_to_index.keys())
        return self

    def encode(self, y: List) -> np.ndarray:
        """Encode a list of raw labels.
        Args:
            y (List): raw labels.
        Returns:
            np.ndarray: encoded labels as indices.
        """
        encoded = np.zeros((len(y)), dtype=int)
        for i, item in enumerate(y):
            encoded[i] = self.class_to_index[item]
        return encoded

    def decode(self, y: List) -> List:
        """Decode a list of indices.
        Args:
            y (List): indices.
        Returns:
            List: labels.
        """
        classes = []
        for i, item in enumerate(y):
            classes.append(self.index_to_class[item])
        return classes

    def save(self, fp: str) -> None:
        """Save class instance to JSON file.
        Args:
            fp (str): filepath to save to.
        """
        with open(fp, "w") as fp:
            contents = {"class_to_index": self.class_to_index}
            json.dump(contents, fp, indent=4, sort_keys=False)

    @classmethod
    def load(cls, fp: str):
        """Load instance of LabelEncoder from file.
        Args:
            fp (str): JSON filepath to load from.
        Returns:
            LabelEncoder instance.
        """
        with open(fp) as fp:
            kwargs = json.load(fp=fp)
        return cls(**kwargs)