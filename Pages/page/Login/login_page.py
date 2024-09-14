from playwright.sync_api import Page, Locator
from Pages.base_page import BasePage
from Pages.page.Products.products_list_page import ProductsListPage

class LoginPage(BasePage):
    """
    Page object model for the Login page of the application.

    This class encapsulates interactions with the Login page elements and provides methods
    for performing login actions and retrieving information from the page.

    Attributes:
        _selectors (LoginPage._Selectors): Contains CSS selectors for identifying elements on the page.
    """
    def __init__(self, page: Page):
        """
        Initializes the LoginPage object.

        Args:
            page (Page): The Playwright Page object representing the current page.
        """
        super().__init__(page)     # Initialize the base class with the page object
        self._selectors = self._Selectors()     # Initialize the selectors for this page


    def set_username(self, value: str):
        """
        Sets the username value in the username input field.

        Args:
            value (str): The username to be entered in the input field.
        """
        self.current_page.fill(self._selectors.USERNAME, value)

    def set_password(self, value: str):
        """
        Sets the password value in the password input field.

        Args:
            value (str): The password to be entered in the input field.
        """
        self.current_page.fill(self._selectors.PASSWORD, value)

    def click_login(self):
        """
        Clicks the login button to submit the login form.
        """
        self.current_page.click(self._selectors.LOGIN_BUTTON)

    def login_to_application(self, username: str, password: str) -> ProductsListPage:
        """
        Performs the login action using provided username and password.

        Args:
            username (str): The username to be used for login.
            password (str): The password to be used for login.

        Returns:
            ProductsListPage: An instance of the ProductsListPage class representing the page 
                               after a successful login.
        """
        self.set_username(username)
        self.set_password(password)
        self.click_login()
        

    def get_error_locator(self) -> Locator:
        """
        Retrieves the locator for the error message element.

        Returns:
            Locator: The Playwright Locator object for the error message.
        """
        return self.current_page.locator(self._selectors.ERROR_MSG)

    def get_login_button_locator(self) -> Locator:
        """
        Retrieves the locator for the login button.

        Returns:
            Locator: The Playwright Locator object for the login button.
        """
        return self.current_page.locator(self._selectors.LOGIN_BUTTON)

    class _Selectors:
        """
        Contains CSS selectors for identifying elements on the Login page.
        """
        USERNAME = "#user-name"
        PASSWORD = "#password"
        LOGIN_BUTTON = "#login-button"
        ERROR_MSG = "[data-test='error']"
    
