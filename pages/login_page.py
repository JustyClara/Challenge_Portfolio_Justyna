# from pages.base_page import BasePage
#
#
# class LoginPage(BasePage):
#     login_field_xpath = "//*[@id='login']"
#     login_field_xpath = "//*[contains(@for, "login")]"
#     login_field_xpath = "//*[text()='Login']"
#
#     password_field_xpath = "/*[contains(@id, "password-label")]"
#     password_field_xpath = "//*[contains(@for, "password")]"
#     password_field_xpath = "//*[text()='Password']"
#
#     sign_in_button_xpath = "/button[starts-with(@class,"MuiButtonBase-root")]"
#     sign_in_button_xpath = "/*[contains(@type, "submit")]"
#     sign_in_button_xpath = "//button[starts-with(@class,"MuiButtonBase-root MuiButton-root")]"
#
#     remind_password_xpath = "//a[starts-with(@class,"MuiTypography-root")]"
#     remind_password_xpath = "//*[contains(@class, "MuiTypography-root MuiLink")]"
#     remind_password_xpath = "//*[text()='Remind password']"
#
#     language_selection_xpath = "//div[starts-with(@class,"MuiSelect-root")]"
#     language_selection_xpath = "//*[contains(@role, "button")]"
#     language_selection_xpath = "//*[text()='English']"
#
#     title_scouts_panel_xpath = "//h5[starts-with(@class, "MuiTypography-root")]"
#     title_scouts_panel_xpath = "//*[contains(@class, "MuiTypography-h5")]"
#     title_scouts_panel_xpath = "//*[text()='Scouts Panel']"
#
#     def type_in_email(self, email):
#         self.field_send_keys(self.login_field_xpath, email)
