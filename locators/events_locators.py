from appium.webdriver.common.mobileby import MobileBy


class EventsPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.tab = (self.ACCESSIBILITY_ID, 'СОБЫТИЯ')
        self.btn_try_yet = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Попробовать ещё раз"`]')
        self.text_error = (self.ACCESSIBILITY_ID, 'Хьюстон, у нас проблемы!')
        self.input_search_field = (self.ACCESSIBILITY_ID, 'textField')
        self.btn_first_under_input_field = (self.ACCESSIBILITY_ID, 'Премьеры')
        self.btn_first_up_input_field = (self.ACCESSIBILITY_ID, 'КИНО')
        self.btn_card_price = (self.XPATH, '(//XCUIElementTypeButton[@name="buyButton"])[1]')
        self.btn_card_release_date = (self.XPATH, '(//XCUIElementTypeStaticText[@name="releaseDateLabel"])[1]')

