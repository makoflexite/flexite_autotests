import os
import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from splinter import Browser
import allure
from allure_commons.types import AttachmentType

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
    # elif browser_name == "iexplorer":
    #     print("\nstart ie browser for test..")
    #     browser = Browser('iexplorer')

    else:
        raise pytest.UsageError("--browser_name parameter should be Chrome or Firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


# next 2 functions are for making screenshot when a test failures
@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function")
def screenshot_on_failure(request, browser):
    def fin():
        attach = browser.screenshot('d:/autotests_materials/autotests_screenshots/scr', full=True)
        if request.node.rep_setup.failed:
            allure.attach(request.function.__name__, attach, allure.attachment_type.PNG)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                allure.attach(request.function.__name__, attach, allure.attachment_type.PNG)
    request.addfinalizer(fin)