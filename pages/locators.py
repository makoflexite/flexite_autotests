# from selenium.webdriver.common.by import By

# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#     BASKET_VIEW = (By.CSS_SELECTOR, ".btn-group>a")

class WebLoginPageLocators():
    LOGIN_PAGE_LINK = "http://172.28.10.163:8081/9510TE/jsp/index_ms.jsp"
    USERNAME = "#login_form #name1"
    PASSWORD = "#login_form #password1"
    LOGIN_BTN = ".login_btn #LoginButton"

# class RegistrationPageLocators():
#     EMAIL = (By.CSS_SELECTOR, "#register_form #id_registration-email")
#     PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
#     PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
#     REG_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-lg")
#
# class ProductPageLocators():
#     ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
#     PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
#     PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>p")
#     BASKET_SUM = (By.CSS_SELECTOR, ".alert-info .alertinner>p>strong")
#     SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success  .alertinner strong")
#
# class BasePageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#     LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
#     USER_ICON = (By.CSS_SELECTOR, ".icon-user")
#
# class BasketPageLocators():
#     EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "# content_inner>p>a")
#     PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
