# from selenium import webdriver
import pytest
import splinter
import pytest_splinter
import time
# import allure
# from allure_commons.types import AttachmentType

from .pages.web_login_page import WebLoginPage
from .pages.full_web_page import FullWebPage

@pytest.mark.testdebug
def test_ordinary_user_can_login_to_web_with_swedish_def_lang(browser):
    page = WebLoginPage(browser)
    page.input_login_password()
    page.should_be_swedish_language_on_lang_label()
    page.should_be_swedish_language_in_lang_combobox()
    page.press_login_btn()
    page1 = FullWebPage(browser)
    page1.should_be_web_loaded_with_left_menu()
    page1.should_be_correct_username()
    page1.should_be_swedish_strings()
    page1.go_to_settings()
    page2 = FullWebPage(browser)
    page2.should_be_swedish_language_in_settings()

# @pytest.mark.testdebug
def test_ordinary_user_can_login_to_web_with_eng_lang(browser):
    page = WebLoginPage(browser)
    page.input_login_password()
    page.choose_english_lang()
    time.sleep(2) #! think of how to avoid time.sleep() function. Need to add explicit wait somewhere.
    page.press_login_btn()
    page1 = FullWebPage(browser)
    page1.should_be_web_loaded_with_left_menu()
    page1.should_be_correct_username()
    page1.should_be_english_strings()
    # time.sleep(3)
    page1.go_to_settings()
    page2 = FullWebPage(browser)
    page2.should_be_english_language_in_settings()

# def test_duplicate_not_absent_user_can_login_to_web(browser):
#     page = WebLoginPage(browser)