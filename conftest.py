import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose user languages: en/ru/es/fr.....(etc)")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    if language is not None:
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language}
        )
    browser = webdriver.Chrome(options=options)
        
   
    yield browser
    time.sleep(5)
    browser.quit()