import pytest
import time
import allure

from .pages.web_login_page import WebLoginPage
from .pages.full_web_page import FullWebPage
from .pages.web_initiate_page import WebInitiatePage
from .pages.locators import *
from .pages.cross_data import *


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
    page2.process_1_delete_all_drafts_templates()
    page2.process_1_initiate_click()
    # current_time = CrossData.current_time_function(browser)
    # print('current_time=', current_time)
    # if browser.is_element_present_by_text('Process 1 - Initiate', wait_time=5):
    #     assert browser.is_element_present_by_css("#iframe_content_id_ti1", wait_time=5), "iframe0 is not found!"
    #     CURRENT_TIME = datetime.datetime.now().strftime("%H:%M")
    #     print(CURRENT_TIME)
    page2.process_1_fill_form_1()
    page2.process_1_initiate_next_click()

    page2.process_1_open_Preview_tab()
    page2.should_be_correct_data_process_1_Preview()

    page2.process_1_initiate_Finish_click()
    page2.process_1_initiate_Alert_Your_registration_saved_closing()
    page2.process_1_initiate_open_detail_view()
    page2.should_be_correct_data_process_1_detail_view()

    time.sleep(3)