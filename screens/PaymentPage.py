from templates.action import Action
from templates.base import Wait
from templates.error import base_error
from templates.statistic import RecordTimeout


class PaymentPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_status_switcher(self, *locator, status=True):
        elem = self.find_element(*locator)
        try:
            if status:
                assert elem.text == '1', f'[FAILED] {locator} has not choices'
            else:
                assert elem.text == '0', f'[FAILED] {locator} has choices'
        except AssertionError as error:
            raise base_error(self.driver, error, *locator, crash_site='click', msg='has choices')
