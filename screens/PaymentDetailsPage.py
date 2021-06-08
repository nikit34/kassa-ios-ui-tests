from templates.base import Wait
from templates.statistic import RecordTimeout
from locators.payment_details_locators import PaymentDetailsPageLocators


class PaymentDetailsPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.payment_details_locators = PaymentDetailsPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_count_tickets(self, count_tickets=1):
        obj_locator, locator = self.payment_details_locators.block_first_ticket
        while count_tickets > 0:
            locator = locator[:-2] + str(count_tickets) + locator[-1]
            self.find_element(obj_locator, locator)
            count_tickets -= 1