from appium.webdriver.common.mobileby import MobileBy


class PaymentDetailsPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.btn_cancel = (MobileBy.ACCESSIBILITY_ID, 'Закрыть')
        self.btn_tickets = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Билеты"`][1]')
        self.btn_products = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Товары"`][1]')
        self.block_first_ticket = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Билет"`][1]')