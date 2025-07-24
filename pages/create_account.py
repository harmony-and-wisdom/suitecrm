import time

from selenium.webdriver.common.by import By



class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.account_name = (By.NAME, 'name')
        self.website = (By.NAME, 'website')
        self.office_phone = (By.NAME, 'phone_office')
        self.fax = (By.ID, 'phone_fax')
        self.add_email = (By.XPATH,"//button[@title='Add Email Address ']")
        self.email_input = (By.XPATH, "//input[@id='Accounts0emailAddress0']")
        self.save_button = (By.ID, 'SAVE')

    def fill_account_form(self, name, website,phone,fax,email):
        self.driver.find_element(*self.account_name).send_keys(name)
        self.driver.find_element(*self.website).send_keys(website)
        self.driver.find_element(*self.office_phone).send_keys(phone)
        self.driver.find_element(*self.fax).send_keys(fax)
        self.driver.find_element(*self.add_email).click()
        self.driver.find_element(*self.email_input).send_keys(email)
        time.sleep(2)

    def save_account(self):

        self.driver.find_element(*self.save_button).click()
        time.sleep(5)
