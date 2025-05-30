from abc import ABC, abstractmethod

class IScraper(ABC):
    """Base scraper class"""
    @abstractmethod
    def scrape(self) -> str:
        """Main scraping method"""
        pass
