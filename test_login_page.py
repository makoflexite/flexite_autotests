# from selenium import webdriver
import pytest
import splinter
import pytest_splinter
import time

from .pages.web_login_page import WebLoginPage
from .pages.full_web_page import FullWebPage

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
    time.sleep(3)
    page1.go_to_settings()

    page2 = FullWebPage(browser)
    page2.should_be_swedish_language_in_settings()

