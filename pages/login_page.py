from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[contains(@type, 'submit')]"
    error_pass_xpath = "//*[contains(@class, 'MuiTypography-caption')]" #albo MuiTypography-colorError
    login_url = 'https://scouts.futbolkolektyw.pl/en/'
    expected_title = 'Scouts panel - sign in'
    title_of_box_xpath = '//child::div/h5'
    header_of_box = 'Scouts Panel'
    language_select_button_xpath = '//input[@class="MuiSelect-nativeInput"]'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def press_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def compare_the_login_form_title(self):
        self.assert_element_text(self.title_of_box_xpath, self.header_of_box)

    def error_enter_the_login_form(self):
        self.visibility_of_element_located(self.error_pass_xpath)
