from appium.webdriver.common.mobileby import MobileBy


class PaymentPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.btn_payment = (MobileBy.ACCESSIBILITY_ID, 'ОПЛАТИТЬ')
        self.btn_movie_details = (MobileBy.ACCESSIBILITY_ID, 'ДЕТАЛИ')
        self.btn_apple_payment = (MobileBy.ACCESSIBILITY_ID, 'applePayButton')
        self.btn_cancel = (MobileBy.ACCESSIBILITY_ID, 'Назад')
        self.fulled_field_input_email = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "n.permyakov-rambler@yandex.ru"`]')
        self.input_phone = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "Номер телефона"`]')
        self.btn_done = (MobileBy.ACCESSIBILITY_ID, 'Готово')
        self.link_personal_access = (MobileBy.ACCESSIBILITY_ID, 'пользовательское соглашение')
        self.btn_bank_card = (MobileBy.ACCESSIBILITY_ID, 'paymentLabel')
        self.radio_bank_card = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "RadioButtonOff"`][2]')