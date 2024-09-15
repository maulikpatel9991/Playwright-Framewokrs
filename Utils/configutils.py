import os

import yaml


def load_config(env: str) -> dict:
    f"""
    Function to load configuration settings based on the specified environment.
    Parameters:
    - env (str): The environment for which configuration settings are to be loaded.
    Returns:
    - dict: A dictionary containing configuration settings for the specified environment.
    """
    # Open the 'config.yml' file in read mode
    # script_dir = os.path.dirname(os.path.realpath(__file__))
    # config_path = os.path.join(script_dir, 'config.yml')
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
        return config.get(env, {})

def get_username():
    """
    Retrieves the username from the configuration based on the current environment.

    This function fetches the username from the configuration settings, which are loaded based on
    the current environment specified in the 'ENV' environment variable. If the environment variable
    is not set, it defaults to 'qa'. The function then extracts and returns the username from the
    configuration.

    Returns:
        str: The username retrieved from the configuration settings.
    """
    # Get the current environment from the 'ENV' environment variable, defaulting to 'qa'
    current_env = os.environ.get('ENV', 'qa')
    config = load_config(current_env)       # Load configuration settings for the current environment
    url = config.get('UserName', '')
    return url

def get_password():
    # Get the current environment from the 'ENV' environment variable, defaulting to 'qa'
    current_env = os.environ.get('ENV', 'qa')
    config = load_config(current_env)       # Load configuration settings for the current environment
    url = config.get('Password', '')
    return url

def get_url() -> str:
    # Get the current environment from the 'ENV' environment variable, defaulting to 'qa'
    current_env = os.environ.get('ENV', 'qa')
    config = load_config(current_env)       # Load configuration settings for the current environment
    url = config.get('url', '')
    return url

def get_api_url() -> str:
    # Get the current environment from the 'ENV' environment variable, defaulting to 'qa'
    current_env = os.environ.get('ENV', 'qa')
    config = load_config(current_env)       # Load configuration settings for the current environment
    url = config.get('api_url', '')
    return url

def get_testdata_folder() -> str:
    # Get the current environment from the 'ENV' environment variable, defaulting to 'qa'
    current_env = os.environ.get('ENV', 'qa')
    config = load_config(current_env)       # Load configuration settings for the current environment
    url = config.get('DatFolder', '')
    return url

def get_headless() -> str:
    # Get the current environment from the 'ENV' environment variable, defaulting to 'qa'
    current_env = os.environ.get('ENV', 'qa')
    config = load_config(current_env)       # Load configuration settings for the current environment
    Headless = (config.get('Headless', ''))
    return (Headless)

def get_slowmo() -> str:
    # Get the current environment from the 'ENV' environment variable, defaulting to 'qa'
    current_env = os.environ.get('ENV', 'qa')
    config = load_config(current_env)       # Load configuration settings for the current environment
    slowmo = (config.get('SlowMo', ''))
    return float(slowmo)

def get_defaultnavigationtimeout() -> str:
    # Get the current environment from the 'ENV' environment variable, defaulting to 'qa'
    current_env = os.environ.get('ENV', 'qa')
    config = load_config(current_env)       # Load configuration settings for the current environment
    timeout = (config.get('DefaultNavigationTimeout', ''))
    return float(timeout)

def get_defaultimeout() -> str:
    # Get the current environment from the 'ENV' environment variable, defaulting to 'qa'
    current_env = os.environ.get('ENV', 'qa')
    config = load_config(current_env)       # Load configuration settings for the current environment
    defaultimeout = float(config.get('DefaultTimeout', ''))
    return float(defaultimeout)

