import numpy as np
from jobspy import scrape_jobs

def fetch_jobs(search_term, location="Dallas, TX", results_wanted=20, hours_old=72):
    # Fetch jobs using the scraper
    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
        search_term=search_term,
        location=location,
        results_wanted=results_wanted,
        hours_old=hours_old,
        country_indeed='USA',
    )
    
    # Convert DataFrame to list of dicts and handle NaN values
    job_list = []
    for job in jobs.to_dict(orient='records'):  # Convert DataFrame to list of dicts
        job_data = {
            'id': job.get('id'),
            'site': job.get('site'),
            'job_url_direct': job.get('job_url'),
            'title': job.get('title'),
            'company': job.get('company'),
            'location': job.get('location'),
            'logo_photo_url': job.get('logo_photo_url')
        }
        
        # Replace NaN values with None
        job_data = {key: (None if isinstance(value, float) and np.isnan(value) else value) for key, value in job_data.items()}
        
        job_list.append(job_data)
    
    return job_list
