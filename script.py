import pickle

from athena.mailer import send_update_email
from athena.web_login import Session
from athena.job_list import JobSoup
from constants import username, password


url = 'https://secure.tutorcruncher.com'
route = 'cal/con/service/'

driver = Session(url)
driver.get_tutorcrunch()
driver.login(username, password)
driver.nav_to_page(route)

jobs_parser = JobSoup(driver.page_source())
jobs = jobs_parser.job_dict_list

try:
    old_jobs = pickle.load(open('store/last_listed_jobs.p', 'rb'))
except FileNotFoundError:
    pass

if old_jobs:
    if old_jobs == jobs:
        print('No new jobs are available')
        exit()
    else:
        # Diffing the lists to get what jobs are different
        new_jobs = [i for i in jobs if i not in old_jobs]
        job_emailer = send_update_email(jobs)

pickle.dump(jobs, open('store/last_listed_jobs.p', 'wb'))