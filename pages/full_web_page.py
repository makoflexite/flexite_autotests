from .base_page import BasePage
from .locators import FullWebPageLocators

class FullWebPage(BasePage):
    def go_to_settings(self):
        settings_icon = self.browser.find_by_css(FullWebPageLocators.SETTINGS_ICON)
        settings_icon.click()
        assert self.browser.is_element_present_by_css(".tab_body#tab_title_ti0", wait_time=10), "Settings are not loaded yet"
        # return FullWebPage(browser=self.browser)

    def should_be_web_loaded_with_left_menu(self):
        assert self.browser.is_element_present_by_css(FullWebPageLocators.LEFT_MENU_COLUMN), "Left menu is not loaded but has to be"

    def should_be_swedish_strings(self):
        tools_label = self.browser.find_by_css(FullWebPageLocators.TOOLS_LABEL).text
        assert tools_label == "Verktyg", "Not Swedish language is on main page"

    def should_be_english_strings(self):
        tools_label = self.browser.find_by_css(FullWebPageLocators.TOOLS_LABEL).text
        assert tools_label == "Tools", "Not English language is on main page"

    def should_be_correct_username(self):
        username = self.browser.find_by_css(FullWebPageLocators.LOGGED_IN_USER).text
        assert username == FullWebPageLocators.ORDINARY_USER_FULL_NAME, "Incorrect user is logged in"


    def should_be_swedish_language_in_settings(self):
         with self.browser.get_iframe(1) as iframe:
            # assert iframe.is_element_present_by_css("iframe#mainFrame", wait_time=5), "iframe is not found!"
            with iframe.get_iframe('mainFrame') as iframe1:
                # assert iframe1.is_element_present_by_css("select#change-language", wait_time=5), "Combo box is not found!"
                lang_combo = self.browser.find_by_css(FullWebPageLocators.SETTINGS_LANG_COMBOBOX)
                lang_combo.click()
                assert iframe1.find_by_css("[selected]")[1].text == 'Svenska', "Not Swedish language is choosen on language combo box"

    def should_be_english_language_in_settings(self):
         with self.browser.get_iframe(1) as iframe:
            # assert iframe.is_element_present_by_css("iframe#mainFrame", wait_time=5), "iframe is not found!"
            with iframe.get_iframe('mainFrame') as iframe1:
                # assert iframe1.is_element_present_by_css("select#change-language", wait_time=5), "Combo box is not found!"
                lang_combo = self.browser.find_by_css(FullWebPageLocators.SETTINGS_LANG_COMBOBOX)
                lang_combo.click()
                assert iframe1.find_by_css("[selected]")[1].text == 'English', "Not English language is choosen on language combo box"