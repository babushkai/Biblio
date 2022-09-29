ML Flow

```python
import numpy as np
import pandas as pd
import random
from labelEncoder import LabelEncoder
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
def preprocess(df, :
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
    get_data_splits(X=df.text.to_numpy(), y=label_encoder.encode(df.tag))
```

6. Evaluaton
```python
from sklearn.metrics import precision_recall_fscore_support

# Evaluate
metrics = precision_recall_fscore_support(y_test, y_pred, average="weighted")
performance = {"precision": metrics[0], "recall": metrics[1], "f1": metrics[2]}
print (json.dumps(performance, indent=2))

```

