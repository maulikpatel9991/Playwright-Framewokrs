from playwright.sync_api import APIRequestContext, Playwright
import logging
import base64
import pytest
# from Pages.Login.login_page import LoginPage
# from Utilities.read_config import AppConfiguration
from playwright.sync_api import sync_playwright
from Utils import configutils
from pytest_html_reporter import attach
# from Pages.Products.products_list_page import ProductsListPage
from typing import Generator
from Utils.logger import logger1

def pytest_html_report_title(report):
   report.title = 'Test-Demo'

def get_browser(browser_name, playwright, launch_options):
    """
    Returns a Playwright browser instance based on the specified browser name and launch options.

    Args:
        browser_name (str): The name of the browser to launch. Supported values are 'chromium', 'firefox', 
                            'msedge', and 'webkit'.
        playwright: The Playwright instance used to launch the browser.
        launch_options (dict): A dictionary of options to configure the browser launch, such as headless mode 
                               and slow motion.

    Returns:
        Browser: The Playwright browser instance.

    Raises:
        ValueError: If the provided `browser_name` is not supported.
    """

    if browser_name == "chromium":
        return playwright.chromium.launch(**launch_options)
    elif browser_name == "firefox":
        return playwright.firefox.launch(**launch_options)
    elif browser_name == "webkit":
        return playwright.webkit.launch(**launch_options)
    elif browser_name == "msedge":
        return playwright.chromium.launch(**launch_options)  # Edge is based on Chromium
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")



@pytest.fixture()
def setup(request, setup_browser):
    """
    A pytest fixture for setting up a browser instance for tests.

    This fixture initializes Playwright, configures browser options, creates a browser context, 
    and provides a page object for tests to interact with. It also ensures proper cleanup 
    of resources after the tests have finished.

    Args:
        request: The pytest request object, used to access the test class and share data.
        setup_browser: The name of the browser to be used, passed as a parameter to the fixture.
    """
    base_url = configutils.get_url()
    

    # Browser options
    headless = (configutils.get_headless())  # convert to bool

    slow_mo = (configutils.get_slowmo())
    launch_options = {"headless": bool(headless), "slow_mo": slow_mo}

    # Start Playwright
    playwright = sync_playwright().start()
    browser = get_browser(setup_browser, playwright, launch_options)
    # browser = playwright.chromium.launch(**launch_options, args=['--start-maximized'])

    context_options = {'base_url': base_url}

    # Browser context settings
    if setup_browser == "firefox" or setup_browser == "webkit":
        browser_context = browser.new_context(**context_options, viewport={"width": 1920, "height": 1080})
    else:
        browser_context = browser.new_context(**context_options, no_viewport=True)

    browser_context.set_default_navigation_timeout(configutils.get_defaultnavigationtimeout())
    browser_context.set_default_timeout(configutils.get_defaultimeout())

    # Create Page
    page = browser_context.new_page()

    request.cls.page = page
    page.goto(base_url)
    

    yield page

    # Clean up: close the page, browser, and stop Playwright after the test completes
    page.close()
    browser.close()
    playwright.stop()




@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright, ) -> Generator[APIRequestContext, None, None]:
    """
    Fixture to create and manage an API request context for the entire test session.
    Args:
        playwright (Playwright): The Playwright instance used to create the API request context.
    Yields:
        APIRequestContext: The API request context object that can be used for making HTTP requests.
    Logs:
        - "testcase start now ....." at the beginning of the fixture setup.
        - "testcase End now ....." at the end of the fixture teardown.
    """
    request_context = playwright.request.new_context()
    logger1.info("testcase start now .....")

    yield request_context
    request_context.dispose()
    logger1.info("testcase End now .....")



def pytest_addoption(parser):
    """
    Adds a custom command-line option to pytest for specifying the browser to use.

    Args:
        parser (argparse.Parser): The pytest parser object used to add new command-line options.

    Example:
        pytest --browser-name firefox
    """
    # Add a custom command-line option to specify the browser name
    parser.addoption(
        "--browser-name",  # The name of the command-line option to be added
        action="store",    # The action to be taken is to store the value provided by the user
        default="chromium",  # The default value to use if the option is not specified by the user
        help="Browser to run tests with (chromium, firefox, webkit, edge)"  # Help text describing the option
    )

@pytest.fixture()
def setup_browser(request):
    """
    :return: This will return the browser name to setup method
    """
    return request.config.getoption("--browser-name")

@pytest.fixture(scope='module', autouse=True)
def setup_logging():
    """
    A pytest fixture for setting up logging.

    This fixture configures the logging system to output logs to both the console and a log file.
    It is automatically used for all tests in the module due to `autouse=True` and applies to the entire module scope.

    Logs will be captured with DEBUG level and above, and are formatted with timestamp, logger name, log level, and message.
    """
    # Configure the logging system
    logging.basicConfig(
        level=logging.DEBUG,  # Set the logging level to DEBUG to capture all levels of log messages
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log message format
        handlers=[
            logging.StreamHandler(),  # Output logs to the console
            logging.FileHandler('test_log.log')  # Output logs to a file named 'test_log.log'
        ]
    )
    
    # Yield to allow test execution
    yield
    # Optionally, teardown or additional cleanup can be done here (not implemented in this example)