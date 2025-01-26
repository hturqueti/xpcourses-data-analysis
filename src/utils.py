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
