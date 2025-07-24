from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope='function')
def init_driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://demo.suiteondemand.com/index.php?module=Users&action=Login")
    request.cls.driver = driver
    yield
    driver.quit()