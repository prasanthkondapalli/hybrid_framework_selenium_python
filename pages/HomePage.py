from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    email_field = "//input[@type='email']"
    password_field = "//input[@type='password']"
    login_button = "//button[@type='submit']"

    def enter_text_into_field(self, field_path, given_text):
        self.driver.find_element(By.XPATH, field_path).clear()
        self.driver.find_element(By.XPATH, field_path).send_keys(given_text)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()
