
from Pages.page.Login.login_page import LoginPage
from playwright.sync_api import expect
from Pages.base_page import BasePage
import pytest
from Utils import configutils
from Utils.logger import logger1


@pytest.mark.usefixtures("setup")
class TestLogin():
    """
    Test suite for login functionality.

    This class contains tests for verifying the login process with different sets of credentials.
    It uses the `setup` fixture to initialize the page object before each test method.

    Attributes:
        page (Page): The Playwright page object provided by the `setup` fixture.
    """
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_with_valid_credentials(self):
        """
        Test login with valid credentials.

        This test verifies that a user can log in successfully with valid credentials and is redirected
        to the correct page. It checks that the page title contains the expected text "Products".

        Steps:
            1. Initialize the LoginPage object with the Playwright page.
            2. Perform login using valid credentials.
            3. Log the attempt with the username used.
            4. Verify that the screen title is "Products".
        """
        self.login_page = LoginPage(self.page)
        self.login_page.login_to_application(configutils.get_username(), configutils.get_password())
        logger1.info(f'Attempting to login with username: {configutils.get_username()}')
        title = self.login_page.screen_title()
        expect(title).to_have_text("Products")
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_with_invalide_credentials(self):
        """
        Test login with invalid credentials.

        This test verifies that a user receives the appropriate error message when attempting to log in
        with invalid credentials. It checks that the error message matches the expected text.

        Steps:
            1. Initialize the LoginPage object with the Playwright page.
            2. Perform login using invalid credentials.
            3. Retrieve and verify the error message displayed on the page.
        """
        self.login_page = LoginPage(self.page)
        msg = "Epic sadface: Username and password do not match any user in this service"
        self.login_page.login_to_application(configutils.get_username(), configutils.get_password())
        message = self.login_page.get_error_locator()
        expect(message).to_have_text(msg)
    

        


