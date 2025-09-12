import os
import yaml
from src.mlopsproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path) -> ConfigBox:
    """
    read yaml file and returns

    Args: path: path of yaml file
    Returns: ConfigBox: ConfigBox type
    Raises: ValueError: if yaml path is empty

    """
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {yaml_file} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e 
    
@ensure_annotations
def create_directories(path_to_directory:list, verbose=True):
    """
    create list of directories

    Args: path_to_directory(list) : take paths of directory
          ignore_log(bool, optional):  ignore if multiple dirs to be created. Defaults to False
    """
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save_json data

    Args: path(Path): path to save the file
          data(dict): data needs to be saved

    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load_json file

    Args: path(Path): path where file is located
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save binary file
    Args: data(Any): data to be saved as binary file
          path(Path) : path to binary file
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load the binary file
    Args: path(Path) : path to binary file
    Returns: Any: object stored in the file

    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data
