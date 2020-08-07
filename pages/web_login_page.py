import pytest
import allure
from allure_commons.types import AttachmentType
# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
from .base_page import BasePage
from .locators import WebLoginPageLocators

class WebLoginPage(BasePage):
    @allure.step("Inputting login/password on Login page")
    def input_login_password(self):
        self.browser.visit(WebLoginPageLocators.LOGIN_PAGE_LINK)
        username = self.browser.find_by_css(WebLoginPageLocators.USERNAME)
        username.fill(WebLoginPageLocators.ORDINARY_USER_NAME)
        password = self.browser.find_by_css(WebLoginPageLocators.PASSWORD)
        password.fill(WebLoginPageLocators.ORDINARY_USER_PASS)

    @allure.step("Choosing English language on Login page")
    def choose_english_lang(self):
        lang_combo = self.browser.find_by_css(WebLoginPageLocators.LANG_COMBOBOX)
        lang_combo.click()
        self.browser.find_by_css("[value='0']").click()

    @allure.step("Checking that Login page is on Swedish language")
    def should_be_swedish_language_on_lang_label(self):
        assert self.browser.find_by_css(WebLoginPageLocators.LANG_LABEL)[2].text=="Språk", "Strings on login form are not Swedish"

    @allure.step("Checking that 'Svenska' is chosen as language on Login page")
    def should_be_swedish_language_in_lang_combobox(self):
        lang_combo = self.browser.find_by_css(WebLoginPageLocators.LANG_COMBOBOX)
        lang_combo.click()
        assert self.browser.find_by_css("[selected]").text == 'Svenska', "Not Swedish language is choosen on language combo box"

    @allure.step("Pressing Login btn on Login page")
    def press_login_btn(self):
        if self.browser.is_element_visible_by_css(WebLoginPageLocators.LOGIN_BTN, wait_time=5):
            self.browser.find_by_css(WebLoginPageLocators.LOGIN_BTN).click()

