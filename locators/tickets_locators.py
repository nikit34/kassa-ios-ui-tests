from appium.webdriver.common.mobileby import MobileBy


class TicketsPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.btn_search_events = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Найти события"`]')
        self.btn_popup_next = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "ПОНЯТНО"`]')
        self.img_ticket = (self.ACCESSIBILITY_ID, 'imageView')
        self.text_title_ticket = (self.ACCESSIBILITY_ID, 'titleLabel')
        self.btn_download_ticket = (self.ACCESSIBILITY_ID, 'pdfButton')
        self.text_time_ticket = (self.ACCESSIBILITY_ID, 'timeLabel')
        self.text_status_ticket = (self.ACCESSIBILITY_ID, 'statusLabel')