from appium.webdriver.common.mobileby import MobileBy


class TheatersPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.tab = (self.ACCESSIBILITY_ID, 'ТЕАТРЫ')
        self.base_cover = (self.ACCESSIBILITY_ID, 'teaserTableCell')
        self.text_event_name = (self.ACCESSIBILITY_ID, 'eventNameLabel')
        self.text_place_name = (self.ACCESSIBILITY_ID, 'nearestPlaceLabel')
        self.text_date = (self.ACCESSIBILITY_ID, 'dateLabel')
        self.text_time = (self.ACCESSIBILITY_ID, 'timeLabel')
        self.btn_buy = (self.ACCESSIBILITY_ID, 'gradientButton')
        self.text_place_name = (self.ACCESSIBILITY_ID, 'dateLabel')