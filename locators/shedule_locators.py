from appium.webdriver.common.mobileby import MobileBy


class ShedulePageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()
        
        self.btn_back = (self.ACCESSIBILITY_ID, 'Close')
        self.btn_map = (self.ACCESSIBILITY_ID, 'mapButton')
        self.search_field = (self.ACCESSIBILITY_ID, 'textField')
        self.template_text_second_filters = [self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == ""`]']
        self.template_base_second_filters = [self.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "dateBackgroundView"`][]']
        self.template_ticket_top = [self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == ""`][1]']
