"""auxiliary methods for working with driver"""

# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import math
# from .locators import BasePageLocators
# from .locators import MainPageLocators

from splinter import Browser
import pytest_splinter
import splinter

class BasePage():
    def __init__(self, browser):
        self.browser = browser
        self.selenium_driver = self.browser.driver
        splinter_selenium_implicit_wait = 10
        # self.url = url
        # self.browser.implicitly_wait(timeout)

    # def is_element_present(self, how, what):
    #     try:
    #         self.browser.find_element(how, what)
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def is_not_element_present(self, how, what, timeout=4):
    #     """checking that element is not present on page during timeout time"""
    #     try:
    #         WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
    #     except TimeoutException:
    #         return True
    #     return False
    #
    # def is_disappeared(self, how, what, timeout=4):
    #     """checking that an element is disappearing"""
    #     try:
    #         WebDriverWait(self.browser, timeout, 1, TimeoutException). \
    #             until_not(EC.presence_of_element_located((how, what)))
    #     except TimeoutException:
    #         return False
    #
    #     return True
    #
    # def get_product_name(self, how, what):
    #     try:
    #         name = self.browser.find_element(how, what).text
    #     except NoSuchElementException:
    #         return False
    #     return name
    #
    # def get_product_price(self, how, what):
    #     try:
    #         price = self.browser.find_element(how, what).text
    #     except NoSuchElementException:
    #         return False
    #     return price
    #
    # def go_to_login_page(self):
    #     link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)  # *says that we gave pair of parameters and this cortege should be unpacked
    #     link.click()
    #
    # def go_to_basket(self):
    #     basket_button = self.browser.find_element(*MainPageLocators.BASKET_VIEW)  # *says that we gave pair of parameters and this cortege should be unpacked
    #     basket_button.click()
    #
    # def open(self):
    #     self.browser.get(self.url)
    #
    # def should_be_login_link(self):
    #     assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    #
    # def should_be_authorized_user(self):
    #     assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
    #                                                                  " probably unauthorised user"
    # def solve_quiz_and_get_code(self):
    #     alert = self.browser.switch_to.alert
    #     x = alert.text.split(" ")[2]
    #     answer = str(math.log(abs((12 * math.sin(float(x))))))
    #     alert.send_keys(answer)
    #     alert.accept()
    #     try:
    #         alert = self.browser.switch_to.alert
    #         alert_text = alert.text
    #         print(f"Your code: {alert_text}")
    #         alert.accept()
    #     except NoAlertPresentException:
    #         print("No second alert presented")
    #
