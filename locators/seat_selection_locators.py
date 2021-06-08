from appium.webdriver.common.mobileby import MobileBy


class SeatSelectionLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.btn_continue = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Продолжить"`]')
        self.img_screen = (self.ACCESSIBILITY_ID, 'Screen')
        self.btn_back = (self.ACCESSIBILITY_ID, 'Назад')