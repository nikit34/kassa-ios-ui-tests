from appium.webdriver.common.mobileby import MobileBy


class ProfilePageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.img_icon = (self.ACCESSIBILITY_ID, 'avatarImageView')
        self.btn_settings = (self.ACCESSIBILITY_ID, 'settingsButton')
        self.btn_row_event = (self.ACCESSIBILITY_ID, 'События')
        self.btn_row_place = (self.ACCESSIBILITY_ID, 'Места')
        self.btn_search_events = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Найти события"`]')

