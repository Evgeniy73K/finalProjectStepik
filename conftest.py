import pytest
from selenium.webdriver.chrome import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--language')


@pytest.fixture(scope="function")
def browser(language=None):
    browser = webdriver.Chrome()
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
