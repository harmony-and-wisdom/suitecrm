
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.create_button = (By.LINK_TEXT, "CREATE")
        self.create_account_option = (By.LINK_TEXT, "Create Accounts")

    def go_to_create_account(self):
        wait = WebDriverWait(self.driver, 10)


        create = wait.until(EC.visibility_of_element_located(self.create_button))
        ActionChains(self.driver).move_to_element(create).perform()

        create_account = wait.until(EC.element_to_be_clickable(self.create_account_option))
        create_account.click()

