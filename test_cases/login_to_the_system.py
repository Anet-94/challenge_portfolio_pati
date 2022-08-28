import os
import unittest

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.user_login = LoginPage(self.driver)

    def test_log_in_title_of_page(self):
        self.user_login.title_of_page()

    def test_log_in_title_in_header(self):
        self.user_login.compare_the_login_form_title()

    def test_log_in_to_the_system(self):
        self.user_login.type_in_email('user01@getnada.com')
        self.user_login.type_in_password('Test-1234')
        self.user_login.press_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()
