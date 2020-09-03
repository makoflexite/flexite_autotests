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



# class BasketPageLocators():
#     EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "# content_inner>p>a")
#     PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
