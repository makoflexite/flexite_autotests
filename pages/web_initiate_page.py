import allure
import time
import datetime
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.common.keys import Keys

# from .base_page import BasePage
# from .locators import FullWebPageLocators
# from .locators import Process1InitiatePageLocators
# from .locators import Process1InitiatePageLocatorsStartForm1
from .locators import *
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
                    """Strings ! need to work more !"""
                    # string1 = iframe1.find_by_css(Process1InitiatePageLocators.STRING1)
                    # assert string1.value == 'user00', 'macro %%%USER_NAME works incorrectly'
                    string2 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.STRING2).fill('test value string2')
                    """Memo"""
                    memo1 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.MEMO2).fill('test value memo2')
                    """Numbers"""
                    number2 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.NUMBER2).fill('-3')
                    number3 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.NUMBER3).fill('10')
                    number4 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.NUMBER4).fill('1.25')
                    """Dates"""
                    date8 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.DATE8).fill('01/01/2021')
                    iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.DATE9_BUTTON).click()
                    iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.DATE9_CALENDAR_TODAY).click()
                    """Check boxes"""
                    iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.CHECKBOX3).click()
                    iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.CHECKBOX4).click()
                    """Combo boxes"""
                    combobox1 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.COMBOBOX1).click()
                    combobox1_value1 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.COMBOBOX1_VALUE1).click()
                    combobox3 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.COMBOBOX3).click()
                    combobox3_value3 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.COMBOBOX3_VALUE3).click()
                    combobox4 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.COMBOBOX4).click()
                    combobox4_value2 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.COMBOBOX4_VALUE2).click()
                    radiogroup_combobox5_value5 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.RADIOGROUP_COMBOBOX5_VALUE5).click()
                    radiogroup_combobox5_value5 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.RADIOGROUP_COMBOBOX5_VALUE4).click()
                    combobox7 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.COMBOBOX7).click()
                    # search in combobox7
                    iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.COMBOBOX7_INPUT).fill('ne')
                    time.sleep(1)
                    combobox7_search = len(iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.COMBOBOX7_SEARCH))
                    assert combobox7_search == 3, f'Incorrect search result: it should be 3, but it is {combobox7_search}'
                    # to select value 'Nine' in combobox7
                    combobox7_value_Nine = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.COMBOBOX7_VALUE_NINE).click()
                    # iframe1.find_by_css('#MainForm').click()
                    """Check list boxes"""
                    with (self.one_iframe('#__16193', '#__16193', 'frame__16193')) as iframe:
                        checklistbox1_value1 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.CHECKLISTBOX1_1).click()

            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    with (self.one_iframe('#__16194', '#__16194', 'frame__16194')) as iframe:
                        checklistbox2_value2 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.CHECKLISTBOX2_2).click()
                        checklistbox2_value3 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.CHECKLISTBOX2_3).click()
                        checklistbox2_value5 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.CHECKLISTBOX2_5).click()
                    # time.sleep(2)
                    # print(iframe1.find_by_css(Process1InitiatePageLocators.TIME1_1).value)
                    # iframe1.find_by_css(Process1InitiatePageLocators.TIME1_2).fill('23')
                    """Time"""
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.TIME1_1).fill('16')
                    iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.TIME1_2).fill('23')
                    # CrossDataVariables.CURRENT_TIME = datetime.datetime.now().strftime("%H:%M")
                    # print(CrossDataVariables.CURRENT_TIME)
                    """Tree"""
                    with (self.one_iframe('#frame16925', 'frame16925', 'frame16925')) as iframe:
                        iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.TREE1_PLUS).click()
                        iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.TREE1_1_1).click()
                        iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.TREE1_3).click()
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    with (self.one_iframe('#frame16926', 'frame16926', 'frame16926')) as iframe:
                        iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.TREE2_PLUS).click()
                        iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.TREE2_1_1).click()
                        iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.TREE2_3).click()
            # with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
            #     with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
            #         """Radio groups"""
            #         radiogroup1_value1 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.RADIOGROUP1_1).click()
            #         radiogroup3_value3 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.RADIOGROUP3_3).click()
            #         radiogroup4_value2 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.RADIOGROUP4_2).click()
            #         radiogroup_radiogroup5_value5 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.RADIOGROUP_RADIOGROUP5_VALUE5).click()
            #         radiogroup_radiogroup5_value4 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.RADIOGROUP_RADIOGROUP5_VALUE4).click()
            #         """Radio list box"""
            #         with (self.one_iframe('#__16935', '#__16935', 'frame__16935')) as iframe:
            #             radiolistbox1_value1 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.RADIOLISTBOX1_1).click()
            # with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
            #     with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
            #         with (self.one_iframe('#__16937', '#__16937', 'frame__16937')) as iframe:
            #             radiolistbox1_value1 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm1.RADIOLISTBOX3_3).click()

    @allure.step
    def process_1_fill_form_2(self):
        if self.browser.is_element_present_by_text('Process 1 - Initiate', wait_time=5):
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    """Radio groups"""
                    radiogroup1_value1 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.RADIOGROUP1_1).click()
                    radiogroup3_value3 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.RADIOGROUP3_3).click()
                    radiogroup4_value2 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.RADIOGROUP4_2).click()
                    radiogroup_radiogroup5_value5 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.RADIOGROUP_RADIOGROUP5_VALUE5).click()
                    radiogroup_radiogroup5_value4 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.RADIOGROUP_RADIOGROUP5_VALUE4).click()
                    """Radio list box"""
                    with (self.one_iframe('#__16935', '#__16935', 'frame__16935')) as iframe:
                        radiolistbox1_value1 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.RADIOLISTBOX1_1).click()
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    with (self.one_iframe('#__16937', '#__16937', 'frame__16937')) as iframe:
                        radiolistbox3_value3 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.RADIOLISTBOX3_3).click()
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    with (self.one_iframe('#__16938', '#__16938', 'frame__16938')) as iframe:
                        radiolistbox4_value2 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.RADIOLISTBOX4_2).click()
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    radiogroup_radiolist5_value3 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.RADIOGROUP_RADIOLIST5_VALUE3).click()
                    radiogroup_radiolist5_value2 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.RADIOGROUP_RADIOLIST5_VALUE2).click()
                    """User component"""
                    user1 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.USER1).click()
                    time.sleep(1)
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                # user_dialog = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.USER1_DIALOG)
                user1_dialog_cross_button = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.USER_POPUP_CROSS_BUTTON).click()
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    user3 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.USER3_INPUT).type(Keys.BACKSPACE)
                    # time.sleep(3)
                    user4 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.USER4).click()
                    time.sleep(1)
            # with (self.one_iframe('#PersonFrame', 'PersonFrame', 1)) as iframe:
            #     user4_user00 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.USER4_USER00).click()

            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)):
                assert self.browser.find_by_id('frameId_component_authlist_inc'), "frameId_component_authlist_inc NOT FOUND"
                with (self.one_iframe('#frameId_component_authlist_inc', 'frameId_component_authlist_inc', self.browser.find_by_id('frameId_component_authlist_inc')[0])) as iframe:
                # with (self.one_iframe('#PersonFrame', 'PersonFrame', 'PersonFrame')) as iframe:
                #     user4_user00 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.USER4_USER00).click()
                    with (self.one_iframe('#ButtonFrame', 'ButtonFrame', 'ButtonFrame')) as iframe:
                        iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.USER_POPUP_SELECT_USER_BUTTON).click()
            #time.sleep(5)
            """Org unit components"""
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    org_unit1 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.ORG_UNIT1)
                    assert org_unit1.value == '', "Org unit1 is not empty, it is {} instead".format(org_unit1.value)
                    org_unit1.click()
            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)):
                assert self.browser.find_by_id('frameId_select_department_id'), "frameId_select_department_id NOT FOUND"
                with (self.one_iframe('#frameId_select_department_id', 'frameId_select_department_id', self.browser.find_by_id('frameId_select_department_id')[0])) as iframe:
                    iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.ORG_UNIT1_VALUE_AUTOTEST_DEP_2).double_click()
            time.sleep(1)

            with (self.one_iframe('#iframe_content_id_ti1', 'iframe0', 1)) as iframe:
                with (self.one_iframe('#mainFrame', '#mainFrame', 'mainFrame')) as iframe:
                    org_unit2 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.ORG_UNIT2)
                    assert org_unit2.value == 'Autotests department 1', "Org unit2 should be 'Autotests department 1', but '{}' instead".format(org_unit2.value)
                    org_unit2.type(Keys.BACKSPACE)

                    org_unit4 = iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.ORG_UNIT4)
                    assert org_unit4.value == 'Administration', "Org unit4 should be 'Administration', but '{}' instead".format(org_unit4.value)
                    org_unit4.click()
            with (self.one_iframe('#iframe_content_id_ti2', 'iframe0', 1)):
                assert self.browser.find_by_id('frameId_select_department_id'), "frameId_select_department_id NOT FOUND"
                with (self.one_iframe('#frameId_select_department_id', 'frameId_select_department_id', self.browser.find_by_id('frameId_select_department_id')[0])) as iframe:
                    iframe.find_by_css(Process1InitiatePageLocatorsStartForm2.ORG_UNIT4_VALUE_TEST1).double_click()
            time.sleep(1)






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
                        assert process1_initiation_data[caption] == value, 'Component "{}": Value "{}" in Preview table is not same as in dictionary "{}"'.format(caption, value, process1_initiation_data[caption])


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
