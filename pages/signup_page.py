from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupPage(BasePage):
    # Locators
    JOB_SEEKER_BUTTON = (By.XPATH, '//button[@class="flex-1 py-2 rounded-lg text-sm font-semibold bg-indigo-500 text-white"]')
    FIRST_NAME_INPUT = (By.XPATH, "//div[@class='grid grid-cols-2 gap-3']//input[1]")
    LAST_NAME_INPUT = (By.XPATH, "//div[@class='grid grid-cols-2 gap-3']//input[2]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='Phone Number']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email (optional)']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def select_job_seeker(self):
        self.click_element(self.JOB_SEEKER_BUTTON)

    def fill_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)

    def fill_last_name(self, last_name):
        self.enter_text(self.LAST_NAME_INPUT, last_name)

    def fill_phone(self, phone):
        self.enter_text(self.PHONE_INPUT, str(phone))

    def fill_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    def fill_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, str(password))

    def submit_form(self):
        self.click_element(self.SUBMIT_BUTTON)
