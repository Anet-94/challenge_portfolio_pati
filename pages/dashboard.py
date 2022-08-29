from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span'
    players_link_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span'
    language_select_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span'
    log_out_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span'
    dev_team_contact_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]'
    add_player_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]'
    add_player_button_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button'
    search_field_xpath = '//*[@id="__next"]/div[1]/header/div/div[1]/div[2]/input'
    download_csv_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[1]/div[2]/button'
    print_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[1]/div[2]/span[1]/span/button'
    view_column_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[1]/div[2]/span[2]/button'
    filter_table_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[1]/div[2]/span[3]/button'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    expected_title = 'Scouts panel'

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.language_select_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def press_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)
