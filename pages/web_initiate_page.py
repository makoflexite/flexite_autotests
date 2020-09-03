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
    def process_1_initiate_next_click(self):
        if self.browser.is_element_present_by_text('Process 1 - Initiate', wait_time=5):
            with self.browser.get_iframe(1) as iframe:
                assert iframe.is_element_present_by_css("#ButtonsFrame", wait_time=5), "ButtonsFrame is not found!"
                with iframe.get_iframe('ButtonsFrame') as iframe1:
                    next_btn = iframe1.find_by_css(FullWebPageLocators.PROCESS_1_INITIATE_NEXT_BUTTON).click()
                    # if self.browser.is_element_present_by_text('E-mail receivers', wait_time=5):
                    #     next_btn = iframe1.find_by_css(FullWebPageLocators.PROCESS_1_INITIATE_NEXT_BUTTON).click()

    @allure.step
    def process_1_fill_form_1(self):
        # label1 = self.browser.find_by_css(Process1InitiatePageLocators.LABEL1).click()
        # proceed opening of new tab with link and returning back

        # assert self.browser.is_element_visible_by_css(Process1InitiatePageLocators.LABEL2, wait_time=5), 'label2 is not visible but should be'
        if self.browser.is_element_present_by_text('StartForm', wait_time=5):
            string1 = self.browser.find_by_css(Process1InitiatePageLocators.STRING1)
            assert string1.text == 'user00', 'macro %%%USER_NAME works incorrectly'
            string2 = self.browser.find_by_css(Process1InitiatePageLocators.STRING2)
            string2.fill('test value string2')
