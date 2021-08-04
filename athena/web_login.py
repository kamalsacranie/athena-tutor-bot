from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
LOGINPAGE_XPATHS = {
    'username_xpath': '//*[@id="id_username"]',
    'password_xpath': '//*[@id="id_password"]',
    'submit_xpath': '//*[@id="email-signin"]',
}

class Session(object):

    options = Options()

    def __init__(
        self,
        url: str,
        headless: bool = True,
        options=options) -> None:

        self.options = options
        self.options.headless = headless

        self.driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=self.options)
        self.url = self._remove_trailing_slash(url)
    
    def get_tutorcrunch(self):

        self.driver.get(self.url)
    
    def login(self, username: str, password: str):

        for xpath in LOGINPAGE_XPATHS:
            form_element = self.driver.find_element_by_xpath(LOGINPAGE_XPATHS[xpath])
            if xpath == 'username_xpath':
                form_element.send_keys(username)
            elif xpath == 'password_xpath':
                form_element.send_keys(password)
            elif xpath == 'submit_xpath':
                form_element.click()
    
    def nav_to_page(self, route: str) -> None:
        self.driver.get(f'{self.url}/{route}')

        # Checking if user can access authentication blocked page. If not we exit
        if '?next=' in self.driver.current_url:
            print('Login was unsuccessful or user is not logged in')
            exit()
    
    def page_source(self, quit: bool=True):
        source = self.driver.page_source
        if quit:
            self.driver.quit()
            return source
        return source

    def _remove_trailing_slash(self, url: str):
        if len(url) > 1:
            if url[-1] == '/':
                url = url[0:len(url)]
        return url
