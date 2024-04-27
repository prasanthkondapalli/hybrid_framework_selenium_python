import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from path.paths import driver_path, app_url


@pytest.fixture()
def setup_and_teardown(request):
    ser = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=ser)
    driver.maximize_window()
    driver.get(app_url)
    request.cls.driver = driver
    # if hasattr(request.cls, 'driver'):
    #     request.cls.driver = driver
    yield driver
    driver.quit()
