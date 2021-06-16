from appium.webdriver.common.mobileby import MobileBy


class MoviesDetailsPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.text_event_name = (self.ACCESSIBILITY_ID, 'eventTitleLabel')
        self.btn_screen_mode = (self.ACCESSIBILITY_ID, 'screenModeButton')
        self.btn_volume = (self.ACCESSIBILITY_ID, 'volumeButton')
        self.text_time = (self.ACCESSIBILITY_ID, 'eventTagLabel')
        self.btn_view_timetable = (self.ACCESSIBILITY_ID, 'buyTicketButton')
        self.btn_back = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Назад"`]')
        self.img_gallery = (self.ACCESSIBILITY_ID, 'imageView')
        self.btn_popup_next = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "ПОНЯТНО"`]')
        self.text_popup_header = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Топовые события"`]')
        self.btn_time_session = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[`name == "sessionCollectionCell"`][1]')