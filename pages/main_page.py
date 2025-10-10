from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

#class MainPage(BasePage):
    #def go_to_login_page(self):
        #link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #link.click()

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)        