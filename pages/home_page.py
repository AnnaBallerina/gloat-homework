from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    accept_cookies_button = (By.XPATH, "//*[@id='ez-accept-all']")
    dismiss_add_button = (By.XPATH, "//*[@id='dismiss-buttondismiss-button']")

    temperature_button = (By.XPATH, "//*[@title='Temperature Conversion']")
    # temperature_button = (By.XPATH, "//*[@class='typeConv temperature bluebg']")
    length_button = (By.XPATH, "//*[@class='typeConv weight bluebg']")
    weight_button = (By.XPATH, "//*[@title='typeConv length bluebg']")

    unit_from_dropdown = (By.XPATH, "//*[@id='unitFrom']")

    # example below should help to choose metric i want
    # fruit_field = browser.find_element_by_xpath("//input[@name='fruits']")
    # fruit_field.send_keys("Mango")

    # heading = (By.XPATH, "//*[@class='oxd-topbar-header-breadcrumb']/h6")
    # assign_leave_option = (By.XPATH, "//*[@title='Assign Leave']")
    # time_at_work_option = (By.XPATH, "//*[@title='Time at Work']")
    #

    def click_button(self, button):
        self.find(button).click()

    def select_from_dropdown(self, dropdown, option):
        self.find_by_id(dropdown).send_keys(option)

    def close_add(self):
        try:
            self.click_button(self.dismiss_add_button)
        except:
            print("No button")
    # def actual_heading(self):
    #     return self.find(self.heading).text
    #
    # def assign_leave_displayed(self):
    #     return self.find(self.assign_leave_option).is_displayed()
    #
    # def time_at_work_displayed(self):
    #     return self.find(self.assign_leave_option).is_displayed()
