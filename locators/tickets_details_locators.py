from appium.webdriver.common.mobileby import MobileBy


class TicketsDetailsPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.btn_geolocation = (self.ACCESSIBILITY_ID, 'Geolocation')
        self.btn_close = (self.ACCESSIBILITY_ID, 'Close')
        self.btn_row_ticket = (self.ACCESSIBILITY_ID, 'Билеты')
        self.btn_row_moviebar = (self.ACCESSIBILITY_ID, 'Кинобар')
        self.info_table = (self.ACCESSIBILITY_ID, 'tableView')
        self.live_table = (self.ACCESSIBILITY_ID, 'LiveTicketRightSide')
        self.text_place = (self.ACCESSIBILITY_ID, 'Место')
        self.text_series = (self.ACCESSIBILITY_ID, 'Ряд')
