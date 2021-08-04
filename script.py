from bs4 import BeautifulSoup
from pprint import pprint

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