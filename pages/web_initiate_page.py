import allure

from .base_page import BasePage
from .locators import FullWebPageLocators
from .locators import Process1InitiatePageLocators
from .python_sql_connect import *


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

        if self.browser.is_element_present_by_text('Process 1 - Initiate', wait_time=5):
            assert self.browser.is_element_present_by_css("#iframe_content_id_ti1", wait_time=5), "iframe0 is not found!"
            with self.browser.get_iframe(1) as iframe:
                assert iframe.is_element_present_by_css("#mainFrame", wait_time=5), "#mainFrame is not found!"
                with iframe.get_iframe('mainFrame') as iframe1:
                    """move to checking part"""
                    # string1 = iframe1.find_by_css(Process1InitiatePageLocators.STRING1)
                    # assert string1.value == 'user00', 'macro %%%USER_NAME works incorrectly'
                    string2 = iframe1.find_by_css(Process1InitiatePageLocators.STRING2)
                    string2.fill('test value string2')

    @allure.step
    def process_1_delete_all_drafts_templates(self):
        try:
            sql = Sql(db_name, db_user, db_password)
            cursor = sql.cnxn.cursor()

            mySQLQuery = ("""
                             DELETE FROM ACT_HISTORY WHERE AH_ID in 
                             (SELECT  AH.AH_ID  FROM   REG_TD RT,  ACT_HISTORY AH  WHERE   RT.REGISTRATION_ID = 155   AND AH.AH_ID = RT.AH_ID    AND (RT.TD_TYPE IN (1, 2, 3)))
                          """)
            cursor.execute(mySQLQuery)
            sql.cnxn.commit()
            sql.cnxn.close()
        except Exception:
            print ("Can't connect to database")

    @allure.step
    def process_1_open_Preview_tab(self):
        with self.browser.get_iframe(1) as iframe:
            assert iframe.is_element_present_by_css("#mainFrame", wait_time=5), "mainFrame is not found!"
            with iframe.get_iframe('mainFrame') as iframe1:
                assert iframe1.is_element_present_by_css("#tabFrame", wait_time=5), "tabFrame is not found!"
                with iframe1.get_iframe('tabFrame') as iframe2:
                    preview = iframe2.find_by_css(Process1InitiatePageLocators.PREVIEW_TAB)
                    preview.mouse_over()
                    preview.click()

    @allure.step
    def should_be_correct_data_process_1_Preview(self):
        pass

    @allure.step
    def process_1_initiate_Finish_click(self):
        pass

    @allure.step
    def process_1_initiate_Alert_Your_registration_saved_closing(self):
        pass

    @allure.step
    def process_1_initiate_open_detail_view(self):
        pass

    @allure.step
    def should_be_correct_data_process_1_detail_view(self):
        pass
