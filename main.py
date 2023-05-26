import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LogingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.saucedemo.com/')
        self.browser = browser

    def tearDown(self) -> None:
        self.browser.quit()

    @parameterized.expand([
        ("standard_user", "secret_sauce")
    ])
    def test_valid_login(self, userName, password):
        browser = self.browser

        browser.find_element(By.ID, 'user-name').send_keys(userName)
        browser.find_element(By.ID, 'password').send_keys(password)
        browser.find_element(By.ID, "login-button").click()

        self.assertIn('/inventory.html', browser.current_url)

        welcome_message = browser.find_element(By.CSS_SELECTOR,'.app_logo').text
        self.assertEqual(welcome_message, 'Swag Labs')