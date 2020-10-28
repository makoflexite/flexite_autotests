import time
import allure

from .base_page import BasePage
from .locators import FullWebPageLocators
from .locators import WebLoginPageLocators
from .locators import Process1InitiatePageLocators
from allure_commons.types import AttachmentType

class FullWebPage(BasePage):
    @allure.step
    def process_1_initiate_click(self):
        process1_menu = self.browser.find_by_css(FullWebPageLocators.PROCESS_1_ITEM).click()
        initiate = self.browser.find_by_css(FullWebPageLocators.PROCESS_1_INITIATE).click()

    @allure.step
    def process_1_initiate_finish(self):
        if self.browser.is_element_present_by_text('Process 1 - Initiate', wait_time=5):
            with (self.one_iframe('#iframe_content_id_ti0', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#ButtonsFrame', 'ButtonsFrame', 'ButtonsFrame')) as iframe:
                    next_btn = iframe.find_by_css(Process1InitiatePageLocators.PROCESS_1_INITIATE_NEXT_BUTTON).click()
                    if self.browser.is_element_present_by_text('E-mail receivers', wait_time=5):
                        next_btn = iframe.find_by_css(Process1InitiatePageLocators.PROCESS_1_INITIATE_NEXT_BUTTON).click()


    @allure.step
    def go_to_settings(self):
        settings_icon = self.browser.find_by_css(FullWebPageLocators.SETTINGS_ICON)
        settings_icon.click()
        assert self.browser.is_element_present_by_css(".tab_body#tab_title_ti0", wait_time=10), "Settings are not loaded yet"

    @allure.step
    def should_be_web_loaded_with_left_menu(self):
        assert self.browser.is_element_present_by_css(FullWebPageLocators.LEFT_MENU_COLUMN, wait_time=3), "Left menu is not loaded but has to be"

    @allure.step
    def should_be_swedish_strings(self):
        tools_label = self.browser.find_by_css(FullWebPageLocators.TOOLS_LABEL).text
        assert tools_label == "Verktyg", "Not Swedish language is on main page"

    @allure.step
    def should_be_english_strings(self):
        tools_label = self.browser.find_by_css(FullWebPageLocators.TOOLS_LABEL).text
        assert tools_label == "Tools", "Not English language is on main page"

    @allure.step
    def should_be_correct_username(self, usname):
        username = self.browser.find_by_css(FullWebPageLocators.LOGGED_IN_USER).text
        assert username == usname, "Incorrect user is logged in"
#         FullWebPageLocators.ORDINARY_USER_FULL_NAME


class SettingsTab(BasePage):
    @allure.step
    def should_be_swedish_language_in_settings(self):
        if self.browser.is_element_present_by_text('Inställningar', wait_time=5):
           with (self.one_iframe('#iframe_content_id_ti0', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', 'iframe1', 'mainFrame')) as iframe:
                    lang_combo = iframe.find_by_css(FullWebPageLocators.SETTINGS_LANG_COMBOBOX)
                    lang_combo.click()
                    assert iframe.find_by_css("[selected]")[1].text == 'Svenska', "Not Swedish language is choosen on language combo box"

    @allure.step
    def should_be_english_language_in_settings(self):
        if self.browser.is_element_present_by_text('Settings', wait_time=5):
             with (self.one_iframe('#iframe_content_id_ti0', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', 'iframe1', 'mainFrame')) as iframe:
                    lang_combo = iframe.find_by_css(FullWebPageLocators.SETTINGS_LANG_COMBOBOX)
                    lang_combo.click()
                    assert iframe.find_by_css("[selected]")[1].text == 'English', "Not English language is choosen on language combo box"


    @allure.step
    def should_be_autotests_department_1(self):
        if self.browser.is_element_present_by_text('Inställningar', wait_time=5):
            with (self.one_iframe('#iframe_content_id_ti0', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', 'iframe1', 'mainFrame')) as iframe:
                    dep_field = iframe.find_by_css(FullWebPageLocators.SETTINGS_DEPARTMENT_FIELD).value
                    assert dep_field == WebLoginPageLocators.DUPLICATE_USER_DEP_1_LABEL, f"Not '{WebLoginPageLocators.DUPLICATE_USER_DEP_1_LABEL}' is in Department field"
