from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chromium.webdriver import ChromiumDriver


class BasePage():

    def __init__(self, browser: ChromiumDriver, url, timeout: int = 10):
        self.browser: ChromiumDriver = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            self.browser.u
        except NoSuchElementException:
            return False
        return True
