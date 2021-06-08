from appium.webdriver.common.mobileby import MobileBy


class PopupLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.btn_allow_once = (self.ACCESSIBILITY_ID, 'Allow Once')
        self.btn_allow_while_using_app = (self.ACCESSIBILITY_ID, 'Allow While Using App')
        self.btn_dont_allow = (self.ACCESSIBILITY_ID, 'Don’t Allow')
        self.text_allow_location = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Allow “Касса” to use your location?"`]')

        self.btn_allow = (self.ACCESSIBILITY_ID, 'Allow')
        self.btn_allow_location = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Разрешить"`]')