import json
from pathlib import Path
from Utils.logger import logger1
from Utils import configutils
from dataclasses import dataclass, field
from typing import Any, Dict
import yaml

"""CSV/JSON Folder Path"""
json_file_path = 'testData/' + configutils.get_testdata_folder() + '/'

def read_file(file_name):
    """
    Reads the content of a JSON file.

    Args:
        file_name (str): The name of the JSON file to be read.

    Returns:
        dict: The JSON data loaded from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
        Exception: For any other unexpected errors.
    """
    # Determine the full path of the file, including the '.json' extension
    path = get_file_with_json_extension(json_file_path + file_name)
    logger1.info(f"Reading file from path: {path}")
    
    try:
        # Open the file and load its JSON content
        with open(path, 'r') as f:
            data = json.load(f)
            logger1.info(f"Successfully read data from file: {file_name}")
            return data
    except FileNotFoundError:
        # Log error if file is not found and re-raise the exception
        logger1.error(f"File not found: {path}")
        raise
    except json.JSONDecodeError as e:
        # Log error if there is an issue decoding the JSON content
        logger1.error(f"Error decoding JSON from file: {path}. Error: {e}")
        raise
    except Exception as e:
        # Log any other unexpected errors
        logger1.error(f"An unexpected error occurred while reading file: {path}. Error: {e}")
        raise

def get_file_with_json_extension(file_name):
    """
    Ensures that the file name has a '.json' extension.

    Args:
        file_name (str): The file name to be checked/modified.

    Returns:
        str: The file name with '.json' extension if it was not already present.
    """
    # Check if the file name already contains a '.json' extension
    if '.json' in file_name:
        path = file_name
    else:
        # Append '.json' extension if not present
        path = json_file_path.joinpath(f'{file_name}.json')
    
    logger1.info(f"Resolved file path: {json_file_path}")
    return path

@dataclass
class SharedData:
    """
    A class to manage shared data in a dictionary format.

    Attributes:
        data (Dict[str, Any]): A dictionary to store key-value pairs of shared data.
    """
    data: Dict[str, Any] = field(default_factory=dict)

    def set_data(self, key: str, value: Any):
        """
        Sets a key-value pair in the shared data dictionary.

        Args:
            key (str): The key under which the value is to be stored.
            value (Any): The value to be stored.
        """
        logger1.info(f"Setting data for key: {key} with value: {value}")
        self.data[key] = value
        logger1.info(f"Current data state: {self.data}")

    def get_data(self, key: str) -> Any:
        """
        Retrieves the value associated with a key from the shared data dictionary.

        Args:
            key (str): The key whose value is to be retrieved.

        Returns:
            Any: The value associated with the key, or None if the key does not exist.
        """
        value = self.data.get(key)
        if value is not None:
            logger1.info(f"Retrieved data for key: {key} with value: {value}")
        else:
            logger1.info(f"No data found for key: {key}")
        return value

# Create an instance of SharedData to manage shared data
shared_data = SharedData()
