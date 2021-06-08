from appium.webdriver.common.mobileby import MobileBy


class BrowserLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.link_address = (self.ACCESSIBILITY_ID, 'Address')
        self.btn_back_app = (self.ACCESSIBILITY_ID, 'Return to Касса')

