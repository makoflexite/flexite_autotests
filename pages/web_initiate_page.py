import allure
import time
import datetime
from selenium.webdriver.support.events import EventFiringWebDriver

from .base_page import BasePage
from .locators import FullWebPageLocators
from .locators import Process1InitiatePageLocators
from .python_sql_connect import *
from .common_data import *

class WebInitiatePage(BasePage):
    @allure.step
    def process_1_initiate_click(self):
        process1_menu = self.browser.find_by_css(FullWebPageLocators.PROCESS_1_ITEM).click()
        initiate = self.browser.find_by_css(FullWebPageLocators.PROCESS_1_INITIATE).click()

    @allure.step
    def process_1_initiate_next_click(self):
        if self.browser.is_element_present_by_text('Process 1 - Initiate', wait_time=5):
            with (self.one_iframe('#iframe_content_id_ti0', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#ButtonsFrame', 'ButtonsFrame', 'ButtonsFrame')) as iframe:
                    next_btn = iframe.find_by_css(Process1InitiatePageLocators.PROCESS_1_INITIATE_NEXT_BUTTON).click()

    @allure.step
    def process_1_fill_form_1(self):
        # label1 = self.browser.find_by_css(Process1InitiatePageLocators.LABEL1).click()
        # proceed opening of new tab with link and returning back
        # assert self.browser.is_element_visible_by_css(Process1InitiatePageLocators.LABEL2, wait_time=5), 'label2 is not visible but should be'

        if self.browser.is_element_present_by_text('Process 1 - Initiate', wait_time=5):
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', 'mainFrame', 'mainFrame')) as iframe:
                    # string1 = iframe1.find_by_css(Process1InitiatePageLocators.STRING1)
                    # assert string1.value == 'user00', 'macro %%%USER_NAME works incorrectly'

                    string2 = iframe.find_by_css(Process1InitiatePageLocators.STRING2).fill('test value string2')
                    memo1 = iframe.find_by_css(Process1InitiatePageLocators.MEMO2).fill('test value memo2')
                    number2 = iframe.find_by_css(Process1InitiatePageLocators.NUMBER2).fill('-3')
                    number3 = iframe.find_by_css(Process1InitiatePageLocators.NUMBER3).fill('10')
                    number4 = iframe.find_by_css(Process1InitiatePageLocators.NUMBER4).fill('1.25')
                    date8 = iframe.find_by_css(Process1InitiatePageLocators.DATE8).fill('01/01/2021')
                    iframe.find_by_css(Process1InitiatePageLocators.DATE9_BUTTON).click()
                    iframe.find_by_css(Process1InitiatePageLocators.DATE9_CALENDAR_TODAY).click()
                    iframe.find_by_css(Process1InitiatePageLocators.CHECKBOX3).click()
                    iframe.find_by_css(Process1InitiatePageLocators.CHECKBOX4).click()
                    combobox1 = iframe.find_by_css(Process1InitiatePageLocators.COMBOBOX1).click()
                    iframe.find_by_css("[value='64137']").click()
                    combobox3 = iframe.find_by_css(Process1InitiatePageLocators.COMBOBOX3).click()
                    iframe.find_by_css("[value='64159']").click()
                    # radiogroup_combobox5 = iframe1.find_by_css(Process1InitiatePageLocators.RADIOGROUP_COMBOBOX5)
                    iframe.find_by_css("#rgv_64186").click()
                    iframe.find_by_css("#rgv_64185").click()
                    combobox7 = iframe.find_by_css(Process1InitiatePageLocators.COMBOBOX7).click()
                    iframe.find_by_css(Process1InitiatePageLocators.COMBOBOX7_INPUT).fill('ne')
                    time.sleep(1)
                    combobox7_search = len(iframe.find_by_css(Process1InitiatePageLocators.COMBOBOX7_SEARCH))
                    assert combobox7_search == 3, f'Incorrect search result: it should be 3, but it is {combobox7_search}'
                    iframe.find_by_css("[value='64205']").click()
                    # iframe1.find_by_css('#MainForm').click()
                    with (self.one_iframe('#__16193', '#__16193', 'frame__16193')) as iframe:
                        iframe.find_by_css(Process1InitiatePageLocators.CHECKLISTBOX1_1).click()

            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    with (self.one_iframe('#__16194', '#__16194', 'frame__16194')) as iframe:
                        iframe.find_by_css(Process1InitiatePageLocators.CHECKLISTBOX2_2).click()
                        iframe.find_by_css(Process1InitiatePageLocators.CHECKLISTBOX2_3).click()
                        iframe.find_by_css(Process1InitiatePageLocators.CHECKLISTBOX2_5).click()
                    # time.sleep(2)
                    # print(iframe1.find_by_css(Process1InitiatePageLocators.TIME1_1).value)
                    # iframe1.find_by_css(Process1InitiatePageLocators.TIME1_2).fill('23')
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    iframe.find_by_css(Process1InitiatePageLocators.TIME1_1).fill('16')
                    iframe.find_by_css(Process1InitiatePageLocators.TIME1_2).fill('23')
                    # CrossDataVariables.CURRENT_TIME = datetime.datetime.now().strftime("%H:%M")
                    # print(CrossDataVariables.CURRENT_TIME)
                    with (self.one_iframe('#frame16925', 'frame16925', 'frame16925')) as iframe:
                        iframe.find_by_css(Process1InitiatePageLocators.TREE1_PLUS).click()
                        iframe.find_by_css(Process1InitiatePageLocators.TREE1_1_1).click()
                        iframe.find_by_css(Process1InitiatePageLocators.TREE1_3).click()
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    with (self.one_iframe('#frame16926', 'frame16926', 'frame16926')) as iframe:
                        iframe.find_by_css(Process1InitiatePageLocators.TREE2_PLUS).click()
                        iframe.find_by_css(Process1InitiatePageLocators.TREE2_1_1).click()
                        iframe.find_by_css(Process1InitiatePageLocators.TREE2_3).click()



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
        with (self.one_iframe('#iframe_content_id_ti0', 'iframe0', 1)) as iframe:
            with (self.one_iframe('#mainFrame', 'iframe1', 'mainFrame')) as iframe:
                with (self.one_iframe('#tabFrame', 'tabFrame', 'tabFrame')) as iframe:
                # assert iframe1.is_element_present_by_css("#tabFrame", wait_time=5), "tabFrame is not found!"
                # with iframe1.get_iframe('tabFrame') as iframe2:
                    preview = iframe.find_by_css(Process1InitiatePageLocators.PREVIEW_TAB)
                    preview.mouse_over()
                    preview.click()

    @allure.step
    def should_be_correct_data_process_1_Preview(self):
        with (self.one_iframe('#iframe_content_id_ti0', 'iframe0', 1)) as iframe:
            with (self.one_iframe('#mainFrame', 'iframe1', 'mainFrame')) as iframe:
                with (self.one_iframe('#bodyFrame', 'bodyFrame', 'bodyFrame')) as iframe:
                    captions = iframe.find_by_css('#wrapper_table > tbody > tr > td > table.ReviewTable > tbody > tr > td.ReviewComponentCaption')
                    values = iframe.find_by_css('#wrapper_table > tbody > tr > td > table.ReviewTable > tbody > tr > td.ReviewComponentValue')
                    for i in range (2, len(captions)):
                        caption= captions[i].text
                        value = values[i-2].text
                        assert caption in process1_initiation_data, 'Key "{}" is not found in dictionary'.format(caption)
                        assert process1_initiation_data[caption] == value, 'Value "{}" in Preview table is not same as in dictionary "{}"'.format(value, process1_initiation_data[caption])


    @allure.step
    def process_1_initiate_Finish_click(self):
        with (self.one_iframe('#iframe_content_id_ti0', 'iframe0', 1)) as iframe:
            with (self.one_iframe('#ButtonsFrame', 'ButtonsFrame', 'ButtonsFrame')) as iframe:
                next_btn = iframe.find_by_css(Process1InitiatePageLocators.PROCESS_1_INITIATE_FINISH_BUTTON).click()

    @allure.step
    def process_1_initiate_Alert_Your_registration_saved_closing(self):
        pass

    @allure.step
    def process_1_initiate_open_detail_view(self):
        pass

    @allure.step
    def should_be_correct_data_process_1_detail_view(self):
        pass
