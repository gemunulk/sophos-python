from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage
import time


class ReservationPageLocators:
    """A class for Reservation page locators. All login page locators should come here"""
    VPN_LINK   = (By.XPATH, "//a[text()='VPN']")
    IE_CONNECTION_RED_ICON = (By.XPATH, "//a[text()='IE_Mitra']/following::td[5]/div/div/div[@class='deactive_active manageicon']")
    OK_BUTTON = (By.XPATH, "//input[@name='messegeEle' and @value='OK']")

class ReservationPage(BasePage):
    URL = '{}/mercuryreservation.php'.format(BasePage.MAIN_URL)
    
    """Reservation page actions """
    def visit(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def validate_reservation_page(self):
        assert self.is_displayed(ReservationPageLocators.VPN_LINK), "VPN_LINK not displayd" 

    def click_vpn(self):
        time.sleep(3)
        self.click(ReservationPageLocators.VPN_LINK)
        time.sleep(5)

    def click_ie_connection_red_icon(self):
        self.click(ReservationPageLocators.IE_CONNECTION_RED_ICON)

    def click_ok_button(self):
        time.sleep(3)
        self.click(ReservationPageLocators.OK_BUTTON)
        time.sleep(3)

        
