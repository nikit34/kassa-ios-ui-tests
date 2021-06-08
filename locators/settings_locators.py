from appium.webdriver.common.mobileby import MobileBy


class SettingsPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.btn_cancel = (self.ACCESSIBILITY_ID, 'closeButton')
        self.row_card = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Мои карты"`]')
        self.row_bonus_card = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Бонусные карты"`]')
        self.row_support = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Техподдержка"`]')
        self.row_faq = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "FAQ"`]')
        self.row_geolocation = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Геолокация"`]')
        self.btn_geolocation = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[`label == "Геолокация"`]')
        self.row_city = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Абдулино"`]')
        self.row_notifications = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Уведомления"`]')
        self.btn_notifications = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[`label == "Уведомления"`]')
        self.row_themes = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Темы"`]')
        self.row_about_app  = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "О приложении"`]')
        self.input = (self.ACCESSIBILITY_ID, 'citySearchBar')
        self.btn_login = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Войти"`]')
        self.btn_choice = (self.ACCESSIBILITY_ID, 'Выбрать')



