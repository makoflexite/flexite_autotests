import pytest
import time
import allure

from .pages.web_login_page import WebLoginPage
from .pages.full_web_page import FullWebPage
from .pages.web_initiate_page import WebInitiatePage
from .pages.locators import *

@allure.feature('Initiation tests')
@pytest.mark.testdebug
def test_initiation_ordinary_user_Process_1_from_WEB(browser, screenshot_on_failure):
    page = WebLoginPage(browser)
    page.input_login_password(WebLoginPageLocators.ORDINARY_USER_NAME, WebLoginPageLocators.ORDINARY_USER_PASS)
    page.choose_english_lang()
    time.sleep(2)  # ! think of how to avoid time.sleep() function. Need to add explicit wait somewhere.
    page.press_login_btn()
    page1 = FullWebPage(browser)
    page1.should_be_web_loaded_with_left_menu()
    page2 = WebInitiatePage(browser)
    page2.process_1_initiate_click()
    page2.process_1_fill_forms()
    page2.process_1_initiate_finish()
    # time.sleep(5)