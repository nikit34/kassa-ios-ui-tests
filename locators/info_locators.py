from appium.webdriver.common.mobileby import MobileBy


class InfoPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.btn_switch_allow = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[`value == "0"`]')
        self.btn_covid_cancel = (self.ACCESSIBILITY_ID, 'Отмена')
        self.btn_covid_next = (self.ACCESSIBILITY_ID, 'Подтвердить')
        self.btn_covid_next_old = (self.ACCESSIBILITY_ID, 'Продолжить')
        self.link_detail_conditions = (self.ACCESSIBILITY_ID, 'ПОДРОБНЫЕ УСЛОВИЯ')