from .base_page import BasePage
import time
from .locators import WebLoginPageLocators

class WebLoginPage(BasePage):


    def pass_login(self):
        self.browser.visit(WebLoginPageLocators.LOGIN_PAGE_LINK)
        # self.browser.visit("http://172.28.10.163:8081/9510TE/jsp/index_ms.jsp")
        username = self.browser.find_by_css(WebLoginPageLocators.USERNAME)
        username.fill('realboss')
        password = self.browser.find_by_css(WebLoginPageLocators.PASSWORD)
        password.fill('flexite')
        self.browser.find_by_css(WebLoginPageLocators.LOGIN_BTN).click()
        time.sleep(5)
