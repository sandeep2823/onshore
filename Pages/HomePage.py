import json
sourcefile = open('./Webelement/homepage.json', "r")
json_data = json.load(sourcefile)


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.shop_id = json_data['shop_id']

    def click_on_home(self):
        self.driver.find_element_by_link_text(self.home_link_text).click()

    def click_on_shop(self):
        self.driver.find_element_by_id(self.shop_id).click()

    def click_on_random_automation(self):
        self.driver.find_element_by_xpath(self.random_automation_link_text).click()

    def navigate_to_url(self):
        self.driver.get(json_data['url'])
