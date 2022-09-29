ML Baseline


```python
%%writefile label.py
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
```

```python
import random
import json
import warnings 
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import seaborn as sns

from label import LabelEncoder
from sklearn import metrics
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import precision_recall_fscore_support, log_loss
from sklearn.model_selection import train_test_split
```

2. Set random seeds
```python
def set_seeds(seed=42):
    """Set seeds for reproducibility."""
    np.random.seed(seed)
    random.seed(seed)
```

3. Preprocess

```python
def preprocess(df,) :
    """Preprocess the data."""
    return df
```

4. Split data
```python
def get_data_splits(X, y, train_size=0.7):
    """Generate balanced data splits."""
    X_train, X_, y_train, y_ = train_test_split(
        X, y, train_size=train_size, stratify=y)
    X_val, X_test, y_val, y_test = train_test_split(
        X_, y_, train_size=0.5, stratify=y_)
    return X_train, X_val, X_test, y_train, y_val, y_test
```

5. Setup
```python
set_seeds()
df = pd.read_csv("sample.csv")
df = df.sample(frac=1).reset_index(drop=True) # shuffle
df = preprocess(df, lower=True, stem=False, min_freq=min_freq)
label_encoder = LabelEncoder().fit(df.tag)
X_train, X_val, X_test, y_train, y_val, y_test = \
    get_data_splits(X=df.drop(df.tag, axis=1), y=label_encoder.encode(df.tag))
```

6. Check Class weight
```python
# Class weights
counts = np.bincount(y_train)
class_weights = {i: 1.0/count for i, count in enumerate(counts)}
print (f"class counts: {counts},\nclass weights: {class_weights}")
```

7. Model Training
```python
# Example: Stochastic Gradient Descent
model = SGDClassifier(
    loss="log", penalty="l2", alpha=1e-4, max_iter=1,
    learning_rate="constant", eta0=1e-1, power_t=0.1,
    warm_start=True)

# Train model
num_epochs = 100
for epoch in range(num_epochs):
    # Training
    model.fit(X_train, y_train)

    # Evaluation
    train_loss = log_loss(y_train, model.predict_proba(X_train))
    val_loss = log_loss(y_val, model.predict_proba(X_val))

    if not epoch%10:
        print(
            f"Epoch: {epoch:02d} | "
            f"train_loss: {train_loss:.5f}, "
            f"val_loss: {val_loss:.5f}"
        )
```

8. Evaluaton
```python
# Evaluate
y_pred = model.predict(X_test)
metrics = precision_recall_fscore_support(y_test, y_pred, average="weighted")
performance = {"precision": metrics[0], "recall": metrics[1], "f1": metrics[2]}
print (json.dumps(performance, indent=2))

```

