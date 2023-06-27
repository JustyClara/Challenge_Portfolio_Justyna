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
    pass














