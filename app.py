import logging
import os
from datetime import datetime
from src.scrapers.icapital_scraper import ICapitalJobScraper

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/job_scraper.log'),
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
        logger.info("Starting job scraper")
        scraper = ICapitalJobScraper(config)
        results = scraper.scrape()
        
        # Ensure output directory exists
        os.makedirs('output', exist_ok=True)
        
        with open(f'output/results_icapital_jobs_{datetime.now().strftime("%Y_%m_%d_%H_%M")}.json', 'w') as f:
            f.write(results)
        logger.info(f'Results written to output/results_icapital_jobs_{datetime.now().strftime("%Y_%m_%d_%H_%M")}.json')
        print(results)
    except Exception as e:
        logger.error(f"Application error: {e}")
        raise

if __name__ == "__main__":
    main() 