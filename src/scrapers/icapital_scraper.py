from typing import Dict, Any, List
import json
import logging
from src.browser.browser_manager import PlaywrightBrowserManager
from src.utils.navigation import PageNavigator, FilterManager
from src.scrapers.job_scraper import JobScraper, JobDataExporter
from src.models.job_listing import JobListing

logger = logging.getLogger(__name__)

class ICapitalJobScraper:
    """Main scraper class"""
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.browser_manager = PlaywrightBrowserManager(
            headless=config.get('headless', True),
            timeout=config.get('timeout', 50000)
        )
        self.jobs: List[JobListing] = []

    def scrape(self) -> str:
        """Main scraping method"""
        try:
            self.browser_manager.initialize()
            page = self.browser_manager.get_page()

            # Navigate to page
            navigator = PageNavigator(page)
            navigator.navigate_to(self.config['page_url'])

            # Apply filters
            filter_manager = FilterManager(page)
            filter_manager.apply_filters({
                '#filter_dep': self.config['department_filter'],
                '#filter_office': self.config['office_filter'],
                '#filter_emp_type': self.config['employment_type_filter']
            })

            # Scrape jobs
            scraper = JobScraper(page)
            visible_jobs = scraper.get_visible_jobs()
            logger.info(f"Found {len(visible_jobs)} jobs to process")

            # Process each job
            for job_element in visible_jobs:
                if job_details := scraper.extract_job_details(job_element):
                    self.jobs.append(job_details)

            return JobDataExporter.to_json(self.jobs)

        except Exception as e:
            logger.error(f"Scraping failed: {e}")
            return json.dumps({"error": str(e)})
        finally:
            self.browser_manager.cleanup() 