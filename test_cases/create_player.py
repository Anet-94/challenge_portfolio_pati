import os
import unittest

from selenium import webdriver

from pages.add_players_page import AddPlayersPage
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

    def test_TC5_create_player(self):
        self.user_login.type_in_email('user01@getnada.com')
        self.user_login.type_in_password('Test-1234')
        self.user_login.press_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.press_the_add_player_button()
        add_player = AddPlayersPage(self.driver)
        add_player.type_in_name("Peter")
        add_player.type_in_surname("Pan")
        add_player.type_in_left_leg()
        add_player.type_in_age("29.08.1950")
        add_player.type_in_position("captain")
        add_player.press_the_submit_button()
        add_player.toast_success_the_form()

    @classmethod
    def tearDown(self):
        self.driver.quit()
