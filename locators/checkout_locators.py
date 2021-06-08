from appium.webdriver.common.mobileby import MobileBy


class CheckoutPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.block_ticket = (self.ACCESSIBILITY_ID, 'checkoutOrderDetailsTableCell')
        self.btn_buy = (self.ACCESSIBILITY_ID, 'continueButton')
        self.btn_buy_ipay = (self.ACCESSIBILITY_ID, 'applePayButton')
