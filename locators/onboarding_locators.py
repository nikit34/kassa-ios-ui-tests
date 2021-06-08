from appium.webdriver.common.mobileby import MobileBy


class OnboardingPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.text_title = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Никаких очередей!"`]')
        self.btn_drive = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Поехали"`]')
        self.text_location = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Доступ к геолокации"`]')
        self.btn_allow_location = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Разрешить"`]')
        self.btn_choice_city = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Выбрать город"`]')
        self.btn_choice = (self.ACCESSIBILITY_ID, 'selectButton')
        self.input_field = (self.ACCESSIBILITY_ID, 'Введите город')
        self.title_choice_city = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar[`name == "Город"`]')
        self.list_cities = (self.ACCESSIBILITY_ID, 'tableView')
        self.btn_pass = (self.ACCESSIBILITY_ID, 'Пропустить')
        self.btn_enable_notification = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Включить уведомления"`]')
        self.text_enable_notification = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Включить уведомления"`][1]')
