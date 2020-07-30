# from selenium.webdriver.common.by import By

# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#     BASKET_VIEW = (By.CSS_SELECTOR, ".btn-group>a")

class WebLoginPageLocators():
    LOGIN_PAGE_LINK = "http://172.28.10.163:8081/9510TE/jsp/index_ms.jsp"
    USERNAME = "#login_form #name1"
    PASSWORD = "#login_form #password1"
    LANG_LABEL = ".login_lable label"
    LANG_COMBOBOX = "select"
    LOGIN_BTN = ".login_btn #LoginButton"

class FullWebPageLocators():
    SETTINGS_ICON = "#settings-icon"
    SETTINGS_LANG_COMBOBOX = "select#change-language"
    SETTINGS_FORM = "MainForm"
    LOGGED_IN_USER = "#menu-wrapper > div.topwrapper > div.login-name"
    TOOLS_LABEL = "#mt0 > div > div.menu_top_title.menu_top_closed_title.menu-top-title-processes"
    LEFT_MENU_COLUMN = "#menu_column"




# class BasketPageLocators():
#     EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "# content_inner>p>a")
#     PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
