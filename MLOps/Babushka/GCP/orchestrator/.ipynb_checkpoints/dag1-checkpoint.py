from pathlib import Path

from great_expectations_provider.operators.great_expectations import (
    GreatExpectationsOperator,
)

from airflow.decorators import dag
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import BranchPythonOperator, PythonOperator
from airflow.utils.dates import days_ago
from app import cli, 