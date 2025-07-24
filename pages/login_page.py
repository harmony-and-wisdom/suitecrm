import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID,'user_name')
        self.password_input = (By.ID,'username_password')
        self.login_button = (By.ID,'bigbutton')
        self.error = (By.XPATH, "//span[text()='You must specify a valid username and password.']")
        self.field_required = (By.XPATH,'//span[text()="Required"]')

    def login(self,username,password):
        username_input = self.driver.find_element(*self.username_input)  #star use to unpack (By.NAME,'username') as it is a tuple
        username_input.send_keys(Keys.CONTROL + 'a')
        username_input.send_keys(Keys.DELETE)
        time.sleep(1)
        username_input.send_keys(username)
        password_input = self.driver.find_element(*self.password_input)
        password_input.send_keys(Keys.CONTROL + 'a')
        password_input.send_keys(Keys.DELETE)
        time.sleep(1)
        password_input.send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.login_button).click()


    def get_invalid_message(self):
        try:
            return self.driver.find_element(*self.error).text
        except:
            return None



