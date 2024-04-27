import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.HomePage import HomePage
from path.paths import app_url, driver_path
import time

# @pytest.fixture()
# def setup_and_teardown(request):
#     ser = Service(executable_path=driver_path)
#     driver = webdriver.Chrome(service=ser)
#     driver.get(app_url)
#     request.cls.driver = driver
#     yield
#     driver.quit()


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_passing_values(self):
        home_page = HomePage(self.driver)
        home_page.enter_text_into_field(home_page.email_field, "hr@b.com")
        home_page.enter_text_into_field(home_page.password_field, "Fractal@123")
        home_page.click_login_button()
        time.sleep(1)
        assert home_page.title() == "Foyr || Sign-in"


    def test_login_passing_null(self):
        home_page = HomePage(self.driver)
        home_page.enter_text_into_field(home_page.email_field, "")
        home_page.enter_text_into_field(home_page.password_field, "")
        home_page.click_login_button()
        assert home_page.login_button.__getattribute__("disabled")
