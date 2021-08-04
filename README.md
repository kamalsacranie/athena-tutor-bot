# Athena Job Scraper

## Plan of action

1. Main script calls
	- bs4 function to grab all job listings
	- Parse html -> create list of jobs
  - pickle list after each run so we have only the latest list
  - send myself an email
1. Host on google cloud to schedule the script to run once a day
