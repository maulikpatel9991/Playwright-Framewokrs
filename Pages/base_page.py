from playwright.sync_api import Page, Locator

class BasePage:
    """
    Base class for page objects in the application.

    This class provides common functionality for interacting with a page. It can be extended by other
    page-specific classes to add page-specific methods and interactions.

    Attributes:
        current_page (Page): The Playwright Page object representing the current page.
    """
    def __init__(self,page: Page) -> None:
        """
        Initializes the BasePage object.

        Args:
            page (Page): The Playwright Page object representing the current page.
        """
        self.current_page = page

    def screen_title(self) -> Locator:
        """
        Retrieves the locator for the screen title element.

        This method provides a way to get the element representing the screen title on the page.

        Returns:
            Locator: The Playwright Locator object for the screen title element.
        """
        title_selector = self.current_page.locator(Selectors.ScreenTitle)
        return title_selector


class Selectors:
    """
    Class containing CSS selectors used for locating elements on pages.

    This class defines the selectors used by page objects to interact with different elements on
    the pages. It helps in managing and updating selectors in a centralized way.

    Attributes:
        ScreenTitle (str): CSS selector for the screen title element.
    """
    ScreenTitle = ".title"