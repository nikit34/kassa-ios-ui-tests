from appium.webdriver.common.mobileby import MobileBy


class CommonLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.tab_trend = (self.ACCESSIBILITY_ID, 'В ТРЕНДЕ')
        self.tab_search = (self.ACCESSIBILITY_ID, 'СОБЫТИЯ')
        self.tab_ticket = (self.ACCESSIBILITY_ID, 'БИЛЕТЫ')
        self.tab_places = (self.ACCESSIBILITY_ID, 'МЕСТА')
        self.tab_profile = (self.ACCESSIBILITY_ID, 'ПРОФИЛЬ')
