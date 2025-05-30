from playwright.sync_api import sync_playwright
import json
import sys
from abc import ABC, abstractmethod

page_url = 'https://icapital.com/careers'
department_filter = "All Departments"
office_filter = "CA ON - Toronto"
employment_type_filter = "Full-time"
launch_timeout = 50000


def scrape_icapital_jobs():
    try:
        with sync_playwright() as p:
            jobs = []

            # initialize browser by default use chromium
            browser = p.chromium.launch(headless=True, timeout=launch_timeout)
            page = browser.new_page()

            # navigate to the page
            page.goto(page_url)
            page.wait_for_load_state('networkidle')

            page.select_option('#filter_dep', label=department_filter)
            page.wait_for_timeout(3000)

            page.select_option('#filter_office', label=office_filter)
            page.wait_for_timeout(3000)

            page.select_option('#filter_emp_type',
                               label=employment_type_filter)
            page.wait_for_timeout(3000)

            all_jobs_container = page.wait_for_selector('.all_jobs')

            found_jobs = all_jobs_container.query_selector_all(
                '.job:not([style*="display: none"])')

            for job_element in found_jobs:
                position_title = job_element.query_selector(
                    '.job_title').inner_text()

                location_element = job_element.query_selector(
                    '.display_location')
                location = location_element.inner_text() if location_element else "N/A"

                role_header = job_element.query_selector(
                    'p strong:has-text("About the Role")')
                role_description = "N/A"
                if role_header:
                    next_p_element = role_header.evaluate_handle(
                        'node => node.parentElement.nextElementSibling')
                    if next_p_element:
                        role_description = next_p_element.inner_text()

                jobs.append({
                    "position_title": position_title,
                    "location": location,
                    "role_description": role_description
                })

            browser.close()

            if not jobs:
                return json.dumps("No jobs found")

            return json.dumps(jobs, indent=2)

    except Exception as e:
        return json.dumps(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        results = scrape_icapital_jobs()
        with open('output/results.json', 'w') as f:
            f.write(results)
        print(results)
    except Exception as e:
        print(f"Application error: {e}")
        sys.exit(1)
