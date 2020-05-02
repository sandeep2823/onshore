from selenium import webdriver
from Pages.HomePage import HomePage
import time
import unittest
import HtmlTestRunner
import sys
import os
from selenium.webdriver.chrome.options import Options
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        # chromeOptions = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        #
        # chrome_options.add_argument("window-size=1800x1080")
        #
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # chromeOptions.add_argument("--no-sandbox")
        # chromeOptions.add_argument("--disable-setuid-sandbox")

        # chromeOptions.add_argument("--remote-debugging-port=9222")  # this

        # chromeOptions.add_argument("--disable-dev-shm-using")
        # chromeOptions.add_argument("--disable-extensions")
        # chromeOptions.add_argument("--disable-gpu")
        # chromeOptions.add_argument("start-maximized")
        # chromeOptions.add_argument("disable-infobars")
        # chromeOptions.add_argument("--headless")
        cls.driver = webdriver.Chrome(
            executable_path="./drivers/chromedriver")
            #  chrome_options=chromeOptions)
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.navigate_to_url()
        homepage.click_on_shop()
        time.sleep(3)
        self.assertEquals(self.driver.find_element_by_id(homepage.shop_id).text, 'Shop', 'Shop link is present')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/sandeepsingh/Study/projects/Python/projects/Onshore/Reports'))
