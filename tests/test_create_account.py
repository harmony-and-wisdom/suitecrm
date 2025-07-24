import json
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from pages.login_page import LoginPage
from pages.dashboard import DashboardPage
from pages.create_account import CreateAccountPage

@pytest.mark.usefixtures("init_driver")
class TestCreateAccount:

    def test_create_account(self):
        login = LoginPage(self.driver)
        login.login("will", "will")

        dashboard = DashboardPage(self.driver)
        dashboard.go_to_create_account()

        with open(r'..\data\account_create_data.json') as f:
            data = json.load(f)
        account_data = data["valid_account"]

        create_account = CreateAccountPage(self.driver)
        create_account.fill_account_form(account_data["name"], account_data["website"], account_data["phone"],account_data["fax"],account_data["email"])
        create_account.save_account()


