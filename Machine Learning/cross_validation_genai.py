from typing import List, Tuple

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Define default imputers outside the function scope for clarity and reusability
DEFAULT_NUMERICAL_IMPUTER = SimpleImputer(strategy='median')
DEFAULT_CATEGORICAL_IMPUTER = SimpleImputer(strategy='most_frequent')

def create_numerical_transformer(imputer=DEFAULT_NUMERICAL_IMPUTER) -> Pipeline:
    """Creates a pipeline for numerical feature transformations."""
    return Pipeline(steps=[
        ('imputer', imputer),
        ('scaler', StandardScaler())  
    ])

def create_categorical_transformer(imputer=DEFAULT_CATEGORICAL_IMPUTER) -> Pipeline:
    """Creates a pipeline for categorical feature transformations."""
    return Pipeline(steps=[
        ('imputer', imputer),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))  
    ])

def create_preprocessing_pipeline(
    numerical_features: List[str] = None, 
    categorical_features: List[str] = None,
    numerical_imputer=DEFAULT_NUMERICAL_IMPUTER, 
    categorical_imputer=DEFAULT_CATEGORICAL_IMPUTER
) -> ColumnTransformer:
    """Creates a preprocessing pipeline for numerical and categorical features.

    Args:
        numerical_features: List of numerical feature names. Defaults to None.
        categorical_features: List of categorical feature names. Defaults to None.
        numerical_imputer: Imputer for numerical features. 
                           Defaults to SimpleImputer(strategy='median').
        categorical_imputer: Imputer for categorical features. 
                             Defaults to SimpleImputer(strategy='most_frequent').

    Returns:
        Preprocessing pipeline as a ColumnTransformer object.

    Raises:
        ValueError: If both `numerical_features` and `categorical_features` are None 
                     or if any of the provided lists is empty.
    """

    if numerical_features is None and categorical_features is None:
        raise ValueError(
            "At least one of 'numerical_features' or 'categorical_features' must be provided."
        )

    if numerical_features is not None and not numerical_features:
        raise ValueError("`numerical_features` cannot be an empty list.")
    if categorical_features is not None and not categorical_features:
        raise ValueError("`categorical_features` cannot be an empty list.") 

    transformers: List[Tuple[str, Pipeline, List[str]]] = [] 
    if numerical_features:
        transformers.append(('num', create_numerical_transformer(numerical_imputer), numerical_features))
    if categorical_features:
        transformers.append(('cat', create_categorical_transformer(categorical_imputer), categorical_features))

    return ColumnTransformer(transformers=transformers)