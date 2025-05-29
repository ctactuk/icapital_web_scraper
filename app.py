import logging
from datetime import datetime
from src.scrapers.icapital_scraper import ICapitalJobScraper

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'job_scraper.log'),
        logging.StreamHandler()
    ],
)
logger = logging.getLogger(__name__)

def main():
    """Main entry point"""
    config = {
        'page_url': 'https://icapital.com/careers',
        'department_filter': "All Departments",
        'office_filter': "CA ON - Toronto",
        'employment_type_filter': "Full-time",
        'headless': True,
        'timeout': 50000
    }

    try:
        scraper = ICapitalJobScraper(config)
        results = scraper.scrape()
        with open('output/results.json', 'w') as f:
            f.write(results)
        print(results)
    except Exception as e:
        logger.error(f"Application error: {e}")
        raise

if __name__ == "__main__":
    main() 