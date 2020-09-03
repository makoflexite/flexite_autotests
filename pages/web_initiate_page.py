import time
import allure

from .base_page import BasePage
from .locators import FullWebPageLocators
from.locators import Process1InitiatePageLocators


class WebInitiatePage(BasePage):
    @allure.step
    def process_1_initiate_click(self):
        process1_menu = self.browser.find_by_css(FullWebPageLocators.PROCESS_1_ITEM).click()
        initiate = self.browser.find_by_css(FullWebPageLocators.PROCESS_1_INITIATE).click()

    @allure.step
    def process_1_initiate_finish(self):
        if self.browser.is_element_present_by_text('Process 1 - Initiate', wait_time=5):
            with self.browser.get_iframe(1) as iframe:
                assert iframe.is_element_present_by_css("#ButtonsFrame", wait_time=5), "ButtonsFrame is not found!"
                with iframe.get_iframe('ButtonsFrame') as iframe1:
                    next_btn = iframe1.find_by_css(FullWebPageLocators.PROCESS_1_INITIATE_NEXT_BUTTON).click()
                    if self.browser.is_element_present_by_text('E-mail receivers', wait_time=5):
                        next_btn = iframe1.find_by_css(FullWebPageLocators.PROCESS_1_INITIATE_NEXT_BUTTON).click()

    @allure.step
    def process_1_fill_forms(self):
        pass