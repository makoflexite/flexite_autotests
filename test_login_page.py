# from selenium import webdriver
import pytest
import splinter
import pytest_splinter
import time
import allure
# from allure_commons.types import AttachmentType

from .pages.web_login_page import WebLoginPage
from .pages.web_login_page import DuplicateLoginPage
from .pages.full_web_page import FullWebPage
from .pages.full_web_page import SettingsTab

@allure.step
def should_be_swedish_language_in_settings(self):
    if self.browser.is_element_present_by_text('Inställningar', wait_time=5):
        assert self.browser.is_element_present_by_css("#iframe_content_id_ti0", wait_time=5), "iframe0 is not found!"
        with self.browser.get_iframe(1) as iframe:
            assert iframe.is_element_present_by_css("#mainFrame", wait_time=5), "iframe1 is not found!"
            with iframe.get_iframe('mainFrame') as iframe1:
                lang_combo = self.browser.find_by_css(FullWebPageLocators.SETTINGS_LANG_COMBOBOX)
                lang_combo.click()
                assert iframe1.find_by_css("[selected]")[
                           1].text == 'Svenska', "Not Swedish language is choosen on language combo box"


@allure.step
def should_be_english_language_in_settings(self):
    if self.browser.is_element_present_by_text('Settings', wait_time=5):
        assert self.browser.is_element_present_by_css("#iframe_content_id_ti0", wait_time=5), "iframe0 is not found!"
        with self.browser.get_iframe(1) as iframe:
            assert iframe.is_element_present_by_css("#mainFrame", wait_time=5), "iframe1 is not found!"
            with iframe.get_iframe('mainFrame') as iframe1:
                lang_combo = self.browser.find_by_css(FullWebPageLocators.SETTINGS_LANG_COMBOBOX)
                lang_combo.click()
                assert iframe1.find_by_css("[selected]")[
                           1].text == 'English', "Not English language is choosen on language combo box"
    else:
        print('Settings text is not found')


@allure.step
def should_be_autotests_department_1(self):
    pass


@allure.feature('Login page tests')
# @pytest.mark.testdebug
def test_ordinary_user_can_login_to_web_with_swedish_def_lang(browser, screenshot_on_failure):
    page = WebLoginPage(browser)
    page.input_login_password_ordinary_user()
    page.should_be_swedish_language_on_lang_label()
    page.should_be_swedish_language_in_lang_combobox()
    page.press_login_btn()
    page1 = FullWebPage(browser)
    page1.should_be_web_loaded_with_left_menu()
    page1.should_be_correct_username()
    page1.should_be_swedish_strings()
    page1.go_to_settings()
    page2 = SettingsTab(browser)
    page2.should_be_swedish_language_in_settings()

# @pytest.mark.testdebug
@allure.feature('Login page tests')
def test_ordinary_user_can_login_to_web_with_eng_lang(browser, screenshot_on_failure):
    page = WebLoginPage(browser)
    page.input_login_password_ordinary_user()
    page.choose_english_lang()
    time.sleep(2) #! think of how to avoid time.sleep() function. Need to add explicit wait somewhere.
    page.press_login_btn()
    page1 = FullWebPage(browser)
    page1.should_be_web_loaded_with_left_menu()
    page1.should_be_correct_username()
    page1.should_be_english_strings()
    # time.sleep(3)
    page1.go_to_settings()
    page2 = SettingsTab(browser)
    page2.should_be_english_language_in_settings()

@pytest.mark.testdebug
@allure.feature('Login page tests')
def test_duplicate_not_absent_user_can_login_to_web(browser):
    page = WebLoginPage(browser)
    page.input_login_password_duplicate_user()
    page.press_login_btn()
    time.sleep(2)
    page1 = DuplicateLoginPage(browser)
    page1.should_be_duplicate_user_form()
    page1.choose_autotests_department_1()
    # time.sleep(3)
    page2 = FullWebPage(browser)
    time.sleep(2)
    # page2.should_be_correct_username()
    page2.go_to_settings()
    page3 = SettingsTab(browser)
    page3.should_be_autotests_department_1()