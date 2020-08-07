import pytest
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from splinter import Browser

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="firefox", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = Browser(browser_name)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = Browser(browser_name)

    else:
        raise pytest.UsageError("--browser_name parameter should be Chrome or Firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()