# iCapital Job Scraper

A Python-based web scraper for extracting job listings from iCapital's careers page. The scraper uses Playwright for browser automation and provides structured job data in JSON format.

Inside this project you will see file proof_of_concept.py where you can find my first approach.

## Project Structure

```
src/
├── models/
│   └── job_listing.py      # Data model for job listings
├── browser/
│   └── browser_manager.py  # Browser management and automation
├── scrapers/
│   ├── icapital_scraper.py # Main scraper implementation
│   └── job_scraper.py      # Job extraction logic
└── utils/
    └── navigation.py       # Page navigation and filtering utilities
```

## Features

- Automated browser control using Playwright
- Configurable job filters (department, office, employment type)
- Structured data extraction
- JSON output format
- Comprehensive logging
- Docker support

## Prerequisites

- Python 3.11 or higher
- Docker (optional, for containerized execution)

## Installation

### Local Installation

1. Clone the repository:
```bash
git clone git@github.com:ctactuk/icapital_web_scraper.git
cd icapital_web_scraper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install chromium
playwright install-deps
```

### Docker Installation

1. Build the Docker image:
```bash
docker compose up -d --build
```

## Usage

### Local Execution

Run the scraper directly:
```bash
python app.py
```

### Docker Execution

Run the scraper in a container:
```bash
docker run icapital-scraper
```

## Configuration

The scraper can be configured by modifying the `config` dictionary in `app.py`:

```python
config = {
    'page_url': 'https://icapital.com/careers',
    'department_filter': "All Departments",
    'office_filter': "CA ON - Toronto",
    'employment_type_filter': "Full-time",
    'headless': True,
    'timeout': 50000
}
```

## Output

The scraper outputs job listings in JSON format with the following structure inside folder output in json file:

```json
[
  {
    "position_title": "Job Title",
    "location": "Job Location",
    "role_description": "Job Description"
  }
]
```

## Logging

Logs are written to both:
- Console output
- `logs/job_scraper.log` file

## Development

The project follows a modular architecture:

- `models/`: Data structures and models
- `browser/`: Browser automation and management
- `scrapers/`: Core scraping functionality
- `utils/`: Helper utilities and tools

## License

[Your License Here]

## Contributing

[Your Contribution Guidelines Here] 