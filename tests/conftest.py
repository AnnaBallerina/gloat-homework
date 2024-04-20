import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.metric-conversions.org/")
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.close()
