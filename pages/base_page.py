from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self._action = ActionChains(self._driver)

    def find(self, locator):
        return self._driver.find_element(*locator)

    def find_by_id(self, element_id):
        return self._driver.find_element_by_id(element_id)
