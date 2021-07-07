from appium.webdriver.common.mobileby import MobileBy


class ShedulePageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()
        
        self.btn_back = (self.ACCESSIBILITY_ID, 'Назад')
        self.btn_map = (self.ACCESSIBILITY_ID, 'mapButton')
        self.search_field = (self.ACCESSIBILITY_ID, 'textField')
        self.template_text_second_filters = [self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == ""`]']
        self.template_base_second_filters = [self.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "dateBackgroundView"`][]']
        self.template_ticket_top = [self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == ""`][1]']
        self.img_screen = [self.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[`name == "eventListCollectionCell"`][1]']
        self.btn_fastbuy_ticket = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Tickets"`][1]')
        self.btn_session_data = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "premiereDateLabel"`][1]')
        self.btn_close = (self.ACCESSIBILITY_ID, 'Close')