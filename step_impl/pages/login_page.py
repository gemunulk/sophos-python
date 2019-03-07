from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage
import time


class LoginPageLocators:
    """A class for Login page locators. All login page locators should come here"""
    USER_NAME_TEXT      = (By.XPATH, "//input[@name='username']")
    PASSWORD_TEXT       = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON       = (By.XPATH, "//input[@name='loginbutton']")


class LoginPage(BasePage):
    URL = '{}/webconsole/webpages/login.jsp'.format(BasePage.MAIN_URL)
    
    """Login page actions """
    def visit(self):
        self.driver.get(self.URL)
        #self.driver.maximize_window()
    
    def login(self, user_name, password):
        self.set(LoginPageLocators.USER_NAME_TEXT, user_name)
        self.set(LoginPageLocators.PASSWORD_TEXT, password)
        self.click(LoginPageLocators.SUBMIT_BUTTON)

    def is_online(self, host):
        return self.is_website_online(host)
        
