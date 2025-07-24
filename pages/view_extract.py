import time
import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ViewAccountsPage:
    def __init__(self, driver):
        self.driver = driver
        self.sales_tab = (By.ID, "grouptab_0")
        self.accounts_option = (By.XPATH, "//a[text()='Accounts']")
        self.view_accounts = (By.XPATH, "//div[text()='View Accounts']")
        self.table_header = (By.XPATH, "//table[contains(@class,'list')]//thead//th")
        self.table_rows = (By.XPATH, "//table[contains(@class,'list')]/tbody/tr")

    def navigate_to_accounts(self):
        actions = ActionChains(self.driver)
        sales = self.driver.find_element(*self.sales_tab)
        actions.move_to_element(sales).perform()
        time.sleep(2)
        self.driver.find_element(*self.accounts_option).click()
        time.sleep(2)

    def click_view_accounts(self):
        self.driver.find_element(*self.view_accounts).click()
        time.sleep(3)

    def extract_table_and_save(self, file_name="../data/view_accounts_data.json"):
        headers = self.driver.find_elements(*self.table_header)
        header_names = []

        for h in headers:
            text = h.text.strip()
            if text:
                header_names.append(text)
            else:
                header_names.append("IGNORE")

        rows = self.driver.find_elements(*self.table_rows)
        all_data = []

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            row_data = [col.text.strip() for col in cols]

            if row_data and len(row_data) >= len(header_names):
                filtered_data = {
                    header: value
                    for header, value in zip(header_names, row_data)
                    if header != "IGNORE"
                }
                all_data.append(filtered_data)

        os.makedirs(os.path.dirname(file_name), exist_ok=True)

        existing_data = []
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []

        existing_data.extend(all_data)

        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=4)

        return file_name
