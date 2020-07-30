# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
from .base_page import BasePage
from .locators import WebLoginPageLocators

class WebLoginPage(BasePage):
    def input_login_password(self):
        self.browser.visit(WebLoginPageLocators.LOGIN_PAGE_LINK)
        username = self.browser.find_by_css(WebLoginPageLocators.USERNAME)
        username.fill('user00')
        password = self.browser.find_by_css(WebLoginPageLocators.PASSWORD)
        password.fill('user00pass')

    def should_be_swedish_language_on_lang_label(self):
        assert self.browser.find_by_css(WebLoginPageLocators.LANG_LABEL)[2].text=="Språk", "Strings on login form are not Swedish"

    def should_be_swedish_language_in_lang_combobox(self):
        lang_combo = self.browser.find_by_css(WebLoginPageLocators.LANG_COMBOBOX)
        lang_combo.click()
        assert self.browser.find_by_css("[selected]").text == 'Svenska', "Not Swedish language is choosen on language combo box"

    def press_login_btn(self):
        self.browser.find_by_css(WebLoginPageLocators.LOGIN_BTN).click()
