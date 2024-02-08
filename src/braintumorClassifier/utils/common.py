import os
from box.exceptions import BoxValueError
import yaml
from braintumorClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return a ConfigBox object.
    :param path_to_yaml: Path to the YAML file.
    :return: ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories
    Args:
      path_to_directories (list): list of directories to create
      ignore_log (bool, optional): ignore if multiple directories is to be created. default to false.
      
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'created directory at: {path}')

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save a JSON file.
    Args:
      path (Path): Path to the JSON file.
      data (dict): Data to be saved.
    """
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    logger.info(f'json file: {path} saved successfully')


@ensure_annotations
def load_json(path: Path) -> ConfigBox:

    """ 
    Load a JSON file and return a ConfigBox object.
    Args:
      path (Path): Path to the JSON file.
    Returns:
      ConfigBox object.
    """
    try:
        with open(path, 'r') as json_file:
            content = json.load(json_file)
        logger.info(f'json file: {path} loaded successfully')
        return ConfigBox(content)
    except Exception as e:
        raise e

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save a binary file.
    Args:
      data (Any): Data to be saved.
      path (Path): Path to the binary file.
    """
    with open(path, 'wb') as outfile:
        outfile.write(data)
    logger.info(f'binary file: {path} saved successfully')

@ensure_annotations
def load_bin(path: Path) -> Any:
    """ 
    Load a binary file and return a ConfigBox object.
    Args:
      path (Path): Path to the binary file.
    Returns:
      ConfigBox object.
    """
    try:
        with open(path, 'rb') as json_file:
            content = json.load(json_file)
        logger.info(f'binary file: {path} loaded successfully')
        return content
    except Exception as e:
        raise e

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file.
    Args:
      path (Path): Path to the file.
    Returns:
      Size of the file.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~{size_in_kb} KB'


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string