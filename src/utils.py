# Libraries
import yaml
from pathlib import Path
from pprint import pprint
from typing import Optional, Union

project_path = Path("__file__").resolve().parents[1]

# Functions
def load_parameters(file_path: Union[Path, str] = project_path.joinpath("parameters.yaml")) -> dict:
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

import pandas as pd

def parse_date(date_str: str) -> pd.Timestamp:
    """
    Parses a string date in 'dd/mm/yyyy' or 'yyyy-mm-dd' format and returns a datetime object.

    Args:
        date_str: The date in string.

    Returns:
        A datetime object representing the date.
    """
    try:
        return pd.to_datetime(date_str, format='%d/%m/%Y').date()
    except ValueError:
        return pd.to_datetime(date_str, format='%Y-%m-%d').date()
