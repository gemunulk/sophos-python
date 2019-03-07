from step_impl.pages.page_factory import PageFactory
from step_impl.pages.page_factory import before_suite
from step_impl.pages.page_factory import after_suite
import time
import logging
import getpass
from selenium.common.exceptions import TimeoutException


def main():
  user_name = input("Username: ")
  password = getpass.getpass('Password: ')

  before_suite()
  logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
  
  while 1:
    is_online = PageFactory.login_page.is_online("http://192.168.10.84/projects") 
    #is_online = False
    if not is_online:
      logging.info('Website is offline')
      try:
        PageFactory.login_page.visit()
        PageFactory.login_page.login(user_name, password)
        PageFactory.reservation_page.click_vpn()
        PageFactory.reservation_page.validate_reservation_page()
        PageFactory.reservation_page.click_ie_connection_red_icon()
        PageFactory.reservation_page.click_ok_button()
        PageFactory.logout_page.visit()        
      except TimeoutException as e:
        logging.info(e)
        PageFactory.logout_page.visit()
      else:
        PageFactory.logout_page.visit()

    time.sleep(10)

  after_suite()    
  
if __name__== "__main__":
  main()