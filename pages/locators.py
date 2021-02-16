# from selenium.webdriver.common.by import By

# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#     BASKET_VIEW = (By.CSS_SELECTOR, ".btn-group>a")

class WebLoginPageLocators():
    LOGIN_PAGE_LINK = "http://172.28.10.163:8081/9000TE/jsp/index_ms.jsp"
    USERNAME = "#login_form #name1"
    PASSWORD = "#login_form #password1"
    LANG_LABEL = ".login_lable label"
    LANG_COMBOBOX = "select"
    LOGIN_BTN = ".login_btn #LoginButton"
    ORDINARY_USER_NAME = 'user00'
    ORDINARY_USER_PASS = 'user00pass'
    DUPLICATE_USER_NAME = 'user01'
    DUPLICATE_USER_PASS = 'user01pass'
    DUPLICATE_USER_DEP_1 = '#logo_content > button:nth-child(2) > div > p'
    DUPLICATE_USER_DEP_1_LABEL = 'Autotests department 1'
    DUPLICATE_USER_DEP_2 = '#logo_content > button:nth-child(3) > div > p'
    DUPLICATE_USER_DEP_2_LABEL = 'Autotests department 3'
    DUPLICATE_USER_DEP_1_BUTTON = '#logo_content > .users_duplicate'

class FullWebPageLocators():
    SETTINGS_ICON = "#settings-icon"
    SETTINGS_LANG_COMBOBOX = "select#change-language"
    SETTINGS_DEPARTMENT_FIELD = "#UnitName"
    SETTINGS_FORM = "MainForm"
    LOGGED_IN_USER = "#menu-wrapper > div.topwrapper > div.login-name"
    TOOLS_LABEL = "#mt1 > div > div"
    LEFT_MENU_COLUMN = "#menu_column"
    ORDINARY_USER_FULL_NAME = 'User00Surname User00Name'
    DUPLICATE_USER_FULL_NAME = 'user01Surname user01Name'
    PROCESS_1_ITEM = '#menu_container #topmenu'
    PROCESS_1_INITIATE = '#menu_container #topmenu .menu_item_title'

class Process1InitiatePageLocators():
    PROCESS_1_INITIATE_NEXT_BUTTON = '#next-button'
    PROCESS_1_INITIATE_FINISH_BUTTON = '#next-button[value="Finish"]'
    PREVIEW_TAB = '#FormTable #_2'

class Process1InitiatePageLocatorsStartForm1():
    LABEL1 = '#CLR_DIV_16132 > div:nth-child(2) > a'
    LABEL2 = '#CLR_DIV_16133 > div:nth-child(2) > span'
    STRING1 = '[name="_16134"]'
    STRING2 = '[name="_16135"]'
    STRING3 = '[name="_16156"]'
    MEMO1 = '[name="_16136"]'
    MEMO2 = '[name="_16155"]'
    NUMBER1 = '[name="_16158"]'
    NUMBER2 = '[name="_16159"]'
    NUMBER3 = '[name="_16161"]'
    NUMBER4 = '[name="_16162"]'
    NUMBER5 = '[name="_16166"]'
    NUMBER6 = '[name="_16167"]'
    DATE8 = '[name="_16176"]'
    DATE9_BUTTON = '#A_16177 > img'
    DATE9_CALENDAR_TODAY = '.fx-drop-calendar-date-today'
    CHECKBOX3 = '.ComponentInputField.l16180'
    CHECKBOX4 = '.ComponentInputField.l16181'
    COMBOBOX1 = '[name="_16183"]'
    COMBOBOX1_VALUE1 = '[value="64137"]'
    COMBOBOX2 = '[name="_16184"]'
    COMBOBOX3 = '[name="_16185"]'
    COMBOBOX3_VALUE3 = '[value="64159"]'
    COMBOBOX4 = '[name="_16186"]'
    COMBOBOX4_VALUE2 = '[value="64168"]'
    RADIOGROUP_COMBOBOX5_VALUE4 = '#rgv_64185'
    RADIOGROUP_COMBOBOX5_VALUE5 = '#rgv_64186'
    COMBOBOX7 = '[name="_16192"]'
    COMBOBOX7_INPUT = '#ddi_16192'
    COMBOBOX7_SEARCH = '#dds_16192>option'
    COMBOBOX7_VALUE_NINE = '[value="64205"]'
    CHECKLISTBOX1_1 = '#cb64207'
    CHECKLISTBOX2_2 = '#cb64213'
    CHECKLISTBOX2_3 = '#cb64214'
    CHECKLISTBOX2_5 = '#cb64216'
    TIME1 = '[name="_16195"]'
    TIME1_1 = '#hh16195'
    TIME1_2 = '#mm16195'
    TREE1_PLUS = '#iconA35'
    TREE1_1_1 = '#checkboxA38'
    TREE1_3 = '#checkboxA37'
    TREE2_PLUS = '#iconA39'
    TREE2_1_1 = '#checkboxA40'
    TREE2_3 = '#checkboxA42'

class Process1InitiatePageLocatorsStartForm2():
    RADIOGROUP1_1 = '#rgv_64999'
    RADIOGROUP3_3 = '#rgv_65011'
    RADIOGROUP4_2 = '#rgv_65015'
    RADIOGROUP_RADIOGROUP5_VALUE4 = '#rgv_65032'
    RADIOGROUP_RADIOGROUP5_VALUE5 = '#rgv_65033'
    RADIOLISTBOX1_1 = '#rb65039'
    RADIOLISTBOX3_3 = '#rb65047'
    RADIOLISTBOX4_2 = '#rb65049'
    RADIOGROUP_RADIOLIST5_VALUE3 = '#rgv_65192'
    RADIOGROUP_RADIOLIST5_VALUE2 = '#rgv_65191'
    USER1 = '#A__17000'
    # USER1_DIALOG = '.ui-dialog'
    # USER1_POPUP_CANCEL_BUTTON = '#cancel'
    USER_POPUP_CROSS_BUTTON = '.ui-dialog-titlebar-close'
    # USER3 = '#A__17002'
    USER3_1 = '[name="__17002"]'



