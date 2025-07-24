
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pages.login_page import LoginPage
from pages.dashboard import DashboardPage


@pytest.mark.usefixtures("init_driver")
class TestDashboard:

    def test_navigate_to_create_account(self):
        login = LoginPage(self.driver)
        login.login("will", "will")

        dashboard = DashboardPage(self.driver)
        dashboard.go_to_create_account()

        # Assertion: Check if 'Create Account' form loaded
        assert "Accounts&action=EditView" in self.driver.current_url
