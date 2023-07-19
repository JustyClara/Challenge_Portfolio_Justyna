import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddaPlayer(unittest.TestCase):

    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(10)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_player_button()
        time.sleep(10)
        add_player = AddAPlayer(self.driver)
        add_player.type_in_email('Justa@Gracz')
        add_player.type_in_name('Justa')
        add_player.type_in_surname('Gracz')
        add_player.type_in_age('16-04-1997')
        add_player.click_submit_button()
        time.sleep(7)


    @classmethod
    def tearDown(self):
        self.driver.quit()
