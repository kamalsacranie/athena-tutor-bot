import pickle

from athena.web_login import Session
from athena.job_list import JobSoup
from constants import username, password


url = 'https://secure.tutorcruncher.com'
route = 'cal/con/service/'

driver = Session(url)
driver.get_tutorcrunch()
driver.login(username, password)
driver.nav_to_page(route)

jobs_parser = JobSoup(driver.page_source)
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
        pass

pickle.dump(jobs, open('store/last_listed_jobs.p', 'wb'))