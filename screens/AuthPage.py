from selenium.common.exceptions import NoSuchElementException

from locators.auth_locators import AuthPageLocators
from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout


class AuthPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.auth_locators = AuthPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_popup(self):
        self.find_element(*self.auth_locators.btn_popup_next)
        self.find_element(*self.auth_locators.text_popup_header)

    def pass_verification(self):
        try:
            self.find_element(*self.auth_locators.text_invalid_fields)
        except NoSuchElementException as error:
            self.find_element(*self.auth_locators.text_verification_fields)


