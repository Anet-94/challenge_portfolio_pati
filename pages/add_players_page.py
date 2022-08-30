from pages.base_page import BasePage


class AddPlayersPage(BasePage):
    name_input_xpath = "//*[@name='name']"
    surname_input_xpath = "//*[@name='surname']"
    leg_open_list_xpath = "//*[@id='mui-component-select-leg']"
    leg_right_xpath = "//*[@id='menu-leg']//li[1]"
    leg_left_xpath = "//*[@id='menu-leg']//li[2]"
    age_input_xpath = "//*[@name='age']"
    position_input_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*[@type='submit']"
    toast_success_xpath = '//*[contains(@class, "toast--success")]'

    def type_in_name(self, name):
        self.field_send_keys(self.name_input_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_input_xpath, surname)

    def type_in_left_leg(self):
        self.click_on_the_element(self.leg_open_list_xpath)
        self.click_on_the_element(self.leg_left_xpath)

    def type_in_age(self, age):
        self.field_send_keys(self.age_input_xpath, age)

    def type_in_position(self, position):
        self.field_send_keys(self.position_input_xpath, position)

    def press_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def toast_success_the_form(self):
        self.visibility_of_element_located(self.toast_success_xpath)
