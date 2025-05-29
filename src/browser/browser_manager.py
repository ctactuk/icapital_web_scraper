from abc import ABC, abstractmethod
from playwright.sync_api import sync_playwright, Page
import logging

logger = logging.getLogger(__name__)

class BrowserManager(ABC):
    """Abstract base class for browser management"""
    @abstractmethod
    def initialize(self) -> None:
        """Initialize the browser"""
        pass

    @abstractmethod
    def cleanup(self) -> None:
        """Clean up browser resources"""
        pass

    @abstractmethod
    def get_page(self) -> Page:
        """Get the current page"""
        pass

class PlaywrightBrowserManager(BrowserManager):
    """Playwright implementation of browser management"""
    def __init__(self, headless: bool = True, timeout: int = 50000):
        self.headless = headless
        self.timeout = timeout
        self.playwright = None
        self.browser = None
        self.page = None

    def initialize(self) -> None:
        """Initialize Playwright browser"""
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(
                headless=self.headless,
                timeout=self.timeout
            )
            self.page = self.browser.new_page()
        except Exception as e:
            logger.error(f"Failed to initialize browser: {e}")
            raise

    def cleanup(self) -> None:
        """Clean up browser resources"""
        try:
            if self.browser:
                self.browser.close()
            if self.playwright:
                self.playwright.stop()
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")

    def get_page(self) -> Page:
        """Get the current page"""
        if not self.page:
            raise RuntimeError("Browser not initialized")
        return self.page 