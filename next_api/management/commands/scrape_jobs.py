import os
import csv
from django.core.management.base import BaseCommand
from jobspy import scrape_jobs

class Command(BaseCommand):
    help = 'Scrape job listings and save to CSV file'

    def handle(self, *args, **kwargs):
        jobs = scrape_jobs(
            site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
            search_term="software engineer",
            location="Dallas, TX",
            results_wanted=20,
            hours_old=72,  # (only Linkedin/Indeed is hour specific, others round up to days old)
            country_indeed='USA',  # only needed for indeed / glassdoor
        )

        # Define the path to save the CSV file
        csv_file_path = os.path.join('next_api', 'data', 'jobs.csv')
        os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

        # Save jobs to CSV file
        jobs.to_csv(csv_file_path, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)

        self.stdout.write(self.style.SUCCESS(f'Successfully scraped {len(jobs)} jobs and saved to {csv_file_path}'))
