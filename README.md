<div style="display: flex;">
    <a href="https://playwright.dev/">
        <img alt="Playwright" src="https://www.lambdatest.com/resources/images/header/Playwright_logo.svg" width="250" style="margin-right: 100px;"/>
    </a>
    <a href="https://www.python.org/">
        <img alt="Python" src="https://www.python.org/static/img/python-logo.png" width="200"/>
    </a>
     <a href="https://www.python.org/">
        <img alt="Python" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1657098680857/FoZEEuklb.png?auto=compress,format&format=webp" width="200" />
    </a>
</div>


# Playwright API & UI Python Framework
This repository contains a comprehensive API testing framework built using Python and Playwright. The framework is designed to streamline your API testing process and provide detailed reports with Allure.

### Initial Setup:
- Install and configure [Python3](https://www.python.org/downloads/)
- Setup your IDE (Preferably [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/#section=windows))
- Import cloned repository as project
- **Creating a virtual environment**.
   Open a terminal, move to the directory where you wish to create the virtual environment, and run the following command to create the virtual environment:

   Use `venv` (for Python 3.3+):

   ```bash
   python -m venv myenv
   ```
-  **Activate virtual environment**.
   To start using the virtual environment, you need to activate it. The activation command is slightly different for different operating systems:

   - On Windows (using Command Prompt):

    ```bash
     myenv\Scripts\activate
    ```

   - On Windows (using PowerShell):

    ```bash
     .\myenv\Scripts\Activate.ps1
    ```
 
   Once the virtual environment is activated, you will see the name of the virtual environment in front of the terminal prompt, indicating that you are in the virtual environment.

  - Install all required packages using this command
    ```sh
    pip install -r requirements.txt
    ``` 

## Key Functionalities

### Utils

#### api_actions.py
- `get_request`: Performs HTTP GET requests.
- `post_request`: Handles HTTP POST requests.
- `put_request`: Executes HTTP PUT requests.
- `patch_request`: Performs HTTP PATCH requests.
- `delete_request`: Handles HTTP DELETE requests.

#### api_utilities.py
- `get_response_code`: Retrieves the HTTP status code from the API response.
- `get_response_data`: Extracts the data from the API response.
- `get_value_from_response`: Fetches a specific value from the JSON response using a JSONPath expression.

#### api_validations.py
- `validate_response_code`: Validates the API response code.
- `validate_entire_response_body_data`: Compares the entire response body with expected data.
- `validate_in_response_body`: Validates specific data in the response body using JSONPath.
- `validate_schema`: Validates the JSON response against a provided schema.

#### utils.py
- `read_file`: Reads and returns data from a JSON file.
- `get_file_with_json_extension`: Constructs and returns the full path to a JSON file.

#### logger.py
- `customLogger`: Creates and configures a custom logger for logging messages.

## Running tests

This project uses `pytest` with `pytest-playwright` as a test runner.

### Defining test choice

#### Running all

To run all the scripts with default setting simply type:

    pytest

#### Running specific test

    pytest Tests/UI/login.py::TestLogin::test_login_with_valid_credentials

#### Running tests matching given expression

    pytest -m <market-name>

For more fancy ways of defining your suite check the official
markers [documentation](https://docs.pytest.org/en/latest/example/markers.html)

### Developer friendly run commands

This will run tests in a headed browser with a delay of 500 milliseconds between actions. It will make observing browser
behaviour easier.

    pytest --headed --slowmo 500

You can insert a breakpoint in your test. It will open interactive pdb session in your console which allows you to use
commands like: [continue, return, quit](https://docs.python.org/3/library/pdb.html#debugger-commands)

```python
def test_something(pytestconfig) -> None:
    base_url = pytestconfig.getini("base_url")
    breakpoint()
```

### Running Tests on Specific Browsers

To run tests on specific browsers, use the Pytest command with the --browser option:

    pytest --browser firefox

This will run tests on Firefox. You can also specify multiple browsers:

    pytest --browser firefox --browser chromium

### Other running options

#### Parallel execution

This repo uses `pytest-xdist` package to allow multiple test being performed in parallel.
Here is an example of running 5 parallel sessions on 3 browsers:

    pytest --base-url https://www.saucedemo.com/ -n 5 --browser chromium --browser firefox --browser webkit

#### Artifacts

Playwright comes with video recording and screen capturing out of the box. The results are saved in test-results
directory by default.

    pytest --screenshot={on,off,only-on-failure}

    pytest --video={on,off,retain-on-failure}

## REPL

Sometimes it's convenient to control the browser in interactive session in your python console. To run Playwright
without Pytest, try this snippet

```python
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
# Use playwright.chromium, playwright.firefox or playwright.webkit
# Pass headless=False to launch() to see the browser UI
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.saucedemo.com/")
page.screenshot(path="example.png")
browser.close()
playwright.stop()
```

## GitHub Actions

The purpose of Continuous integration in this repo is to:

1. Validate created Pull Requests - confirm the pre-commit and test are passing
2. Create a template for regularly launched tasks that will Test the targeted environment
