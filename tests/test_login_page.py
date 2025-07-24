
import pytest
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage

with open('..\data\login_page.json','r') as f:
    data = f.read()
    json_data = json.loads(data)


@pytest.mark.usefixtures("init_driver")
class TestOrangeHRMLogin:

    @pytest.mark.parametrize("credential",json_data['valid_credentials'])
    def test_valid_login(self,credential):
        page = LoginPage(self.driver)
        page.login(credential["username"],credential["password"])
        assert "demo" in self.driver.current_url.lower()


    @pytest.mark.parametrize("credential",json_data['invalid_credentials'])
    def test_invalid_login(self,credential):
        page = LoginPage(self.driver)
        page.login(credential["username"], credential["password"])
        error = page.get_invalid_message()
        assert  "You must specify" in error
