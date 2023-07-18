import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    title_scouts_panel_xpath = "//*[text()='Scouts Panel']"
    players_count_xpath = "//*[text()='Players count']"
    main_page_xpath = "//*[text()='Main page']"
    last_updated_match_xpath = "//*[text()='Last updated match']"
    last_updated_player_xpath = "//*[text()='Last updated player']"
    last_created_player_xpath = "//*[text()='Last created player']"
    last_updated_report_xpath = "//*[text()='Last updated report']"
    futbol_kolektyw_image_xpath = "//div[starts-with(@class,'MuiCardMedia-root jss130')]"
    shortcuts_xpath = "//*[text()='Shortcuts']"
    sign_out_xpath = "//*[text()='Sign out']"
    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"

    email_field_xpath = "//input[starts-with(@aria-invalid,'false')]"
    height_field_xpath = "//*[contains(@name, 'height')]"
    weight_field_xpath = "//*[contains(@name, 'weight')]"
    phone_field_xpath = "//*[contains(@name, 'phone')]"
    surname_field_xpath = "//*[contains(@name, 'surname')]"
    name_field_xpath = "//*[contains(@name, 'name')]"
    age_field_xpath = "//*[contains(@name, 'age')]"
    leg_field_xpath = "//*[contains(@id, 'mui-component-select-leg')]"
    achievements_field_xpath = "//*[contains(@name, 'achievements')]"
    laczy_nad_pilka_xpath = "//*[contains(@name, 'webLaczy')]"

    medium_page_start_reading_button_xpath = "//*[text()='Start reading']"


    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.sign_out_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player(self):
        time.sleep(5)
        assert self.click_on_the_element(self.add_player_xpath)

    pass














