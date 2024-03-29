import pickle

from athena.mailer import send_update_email
from athena.web_login import Session
from athena.job_list import JobSoup
from constants import username, password

url = "https://secure.tutorcruncher.com"
route = "cal/con/service/"


def main():
    # Creating our session object which handles our Selenium operations
    driver = Session(url)
    driver.get_tutorcrunch()
    driver.login(username, password)
    driver.nav_to_page(route)

    # Parse our page source with BS4 using the JobSoup class which inherits
    # from the classic BeautifulSoup class
    jobs_parser = JobSoup(driver.page_source())
    jobs = jobs_parser.job_dict_list

    # Filtering out the jobs we found last time the script was run so I don't
    # send myself a duplicate. Serialised using pickle
    try:
        old_jobs = pickle.load(open("store/last_listed_jobs.p", "rb"))
    except FileNotFoundError:
        old_jobs = False

    if old_jobs:
        if old_jobs == jobs:
            print("No new jobs are available")
            exit()
        else:
            # Diffing the lists to get what jobs are different
            new_jobs = [i for i in jobs if i not in old_jobs]
            send_update_email(new_jobs)

    # Creates our pickled job list for next time
    pickle.dump(jobs, open("store/last_listed_jobs.p", "wb"))


if __name__ == "__main__":
    main()
