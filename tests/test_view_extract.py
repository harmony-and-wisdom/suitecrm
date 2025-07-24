# Tests/test_view_extract.py

import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from pages.login_page import LoginPage
from pages.view_extract import ViewAccountsPage

@pytest.mark.usefixtures("init_driver")
class TestViewAccountsExtract:

    def test_extract_accounts_table(self):
        # Login first
        login = LoginPage(self.driver)
        login.login("will", "will")

        # Navigate to View Accounts
        view_page = ViewAccountsPage(self.driver)
        view_page.navigate_to_accounts()
        view_page.click_view_accounts()

        # Extract and save table
        file_path = view_page.extract_table_and_save()
        print(f"\nData saved to {file_path}")
