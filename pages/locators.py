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
    COMBOBOX2 = '[name="_16184"]'
    COMBOBOX3 = '[name="_16185"]'
    COMBOBOX4 = '[name="_16186"]'




