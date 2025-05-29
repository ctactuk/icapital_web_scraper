from playwright.sync_api import Page
from typing import List, Any, Optional, Dict
import json
import logging
from src.models.job_listing import JobListing

logger = logging.getLogger(__name__)

class JobScraper:
    """Handles job listing extraction"""
    def __init__(self, page: Page):
        self.page = page

    def get_visible_jobs(self) -> List[Any]:
        """Get all visible job listings"""
        try:
            all_jobs_container = self.page.wait_for_selector('.all_jobs')
            return all_jobs_container.query_selector_all('.job:not([style*="display: none"])')
        except Exception as e:
            logger.error(f"Failed to get visible jobs: {e}")
            raise

    def extract_job_details(self, job_element: Any) -> Optional[JobListing]:
        """Extract details from a job listing"""
        try:
            position_title = job_element.query_selector('.job_title').inner_text()
            
            location_element = job_element.query_selector('.display_location')
            location = location_element.inner_text() if location_element else "N/A"
            
            role_description = self._extract_role_description(job_element)
            
            return JobListing(
                position_title=position_title,
                location=location,
                role_description=role_description
            )
        except Exception as e:
            logger.error(f"Failed to extract job details: {e}")
            return None

    def _extract_role_description(self, job_element: Any) -> str:
        """Extract role description from job element"""
        try:
            role_header = job_element.query_selector('p strong:has-text("About the Role")')
            if not role_header:
                return "N/A"

            next_p_element = role_header.evaluate_handle(
                'node => node.parentElement.nextElementSibling'
            )
            return next_p_element.inner_text() if next_p_element else "N/A"
        except Exception:
            return "N/A"

class JobDataExporter:
    """Handles job data export"""
    @staticmethod
    def to_json(jobs: List[JobListing]) -> str:
        """Convert job listings to JSON"""
        if not jobs:
            return json.dumps({"message": "No jobs found"})
        
        return json.dumps([job.to_dict() for job in jobs], indent=2) 