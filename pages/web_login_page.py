import pytest
import allure
from allure_commons.types import AttachmentType
# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
from .base_page import BasePage
from .locators import WebLoginPageLocators

class WebLoginPage(BasePage):
    # @allure.step("Inputting login/password on Login page")
    @allure.step
    def input_login_password_ordinary_user(self):
        self.browser.visit(WebLoginPageLocators.LOGIN_PAGE_LINK)
        username = self.browser.find_by_css(WebLoginPageLocators.USERNAME)
        username.fill(WebLoginPageLocators.ORDINARY_USER_NAME)
        password = self.browser.find_by_css(WebLoginPageLocators.PASSWORD)
        password.fill(WebLoginPageLocators.ORDINARY_USER_PASS)

    @allure.step
    def input_login_password_duplicate_user(self):
        self.browser.visit(WebLoginPageLocators.LOGIN_PAGE_LINK)
        username = self.browser.find_by_css(WebLoginPageLocators.USERNAME)
        username.fill(WebLoginPageLocators.DUPLICATE_USER_NAME)
        password = self.browser.find_by_css(WebLoginPageLocators.PASSWORD)
        password.fill(WebLoginPageLocators.DUPLICATE_USER_PASS)

    @allure.step
    def choose_english_lang(self):
        lang_combo = self.browser.find_by_css(WebLoginPageLocators.LANG_COMBOBOX)
        lang_combo.click()
        self.browser.find_by_css("[value='0']").click()

    @allure.step
    def should_be_swedish_language_on_lang_label(self):
        assert self.browser.find_by_css(WebLoginPageLocators.LANG_LABEL)[2].text=="Språk", "Strings on login form are not Swedish"

    @allure.step
    def should_be_swedish_language_in_lang_combobox(self):
        lang_combo = self.browser.find_by_css(WebLoginPageLocators.LANG_COMBOBOX)
        lang_combo.click()
        assert self.browser.find_by_css("[selected]").text == 'Svenska', "Not Swedish language is choosen on language combo box"

    @allure.step
    def press_login_btn(self):
        if self.browser.is_element_visible_by_css(WebLoginPageLocators.LOGIN_BTN, wait_time=5):
            self.browser.find_by_css(WebLoginPageLocators.LOGIN_BTN).click()


class DuplicateLoginPage(BasePage):
    @allure.step
    def should_be_duplicate_user_form(self):
        dep1 = self.browser.find_by_css(WebLoginPageLocators.DUPLICATE_USER_DEP_1).text
        assert WebLoginPageLocators.DUPLICATE_USER_DEP_1_LABEL in dep1, f"No string '{WebLoginPageLocators.DUPLICATE_USER_DEP_1_LABEL}' in 1st duplicate user location"
        dep2 = self.browser.find_by_css(WebLoginPageLocators.DUPLICATE_USER_DEP_2).text
        assert WebLoginPageLocators.DUPLICATE_USER_DEP_2_LABEL in dep2, f"No string '{WebLoginPageLocators.DUPLICATE_USER_DEP_2_LABEL}' in 2d duplicate user location"

    @allure.step
    def choose_autotests_department_1(self):
        self.browser.find_by_css(WebLoginPageLocators.DUPLICATE_USER_DEP_1_BUTTON).click()