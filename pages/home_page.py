from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators
    JOIN_NOW_LINK = (By.LINK_TEXT, "Join Now")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://jobnav.in"

    def navigate_to_home(self):
        self.open_url(self.url)

    def click_join_now(self):
        self.click_element(self.JOIN_NOW_LINK)
