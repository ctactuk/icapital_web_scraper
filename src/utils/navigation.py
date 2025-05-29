from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class PageNavigator:
    """Handles page navigation and loading"""
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str) -> None:
        """Navigate to specified URL"""
        try:
            logger.info(f"Navigating to {url}")
            self.page.goto(url)
            self.page.wait_for_load_state('networkidle')
        except PlaywrightTimeoutError:
            logger.error("Page load timeout")
            raise
        except Exception as e:
            logger.error(f"Navigation failed: {e}")
            raise

class FilterManager:
    """Manages job search filters"""
    def __init__(self, page: Page):
        self.page = page

    def apply_filter(self, selector: str, label: str, wait_time: int = 3000) -> None:
        """Apply a single filter"""
        try:
            self.page.select_option(selector, label=label)
            self.page.wait_for_timeout(wait_time)
        except Exception as e:
            logger.error(f"Failed to apply filter {selector}: {e}")
            raise

    def apply_filters(self, filters: Dict[str, str]) -> None:
        """Apply multiple filters"""
        for selector, label in filters.items():
            self.apply_filter(selector, label) 