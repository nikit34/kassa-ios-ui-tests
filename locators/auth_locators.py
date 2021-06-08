from appium.webdriver.common.mobileby import MobileBy


class AuthPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.btn_settings = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "settings"`]')
        self.btn_onboarding_login = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Войти"`]')
        self.btn_onboarding_sberid = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == " Войти по Сбер ID"`]')
        self.input_login_email = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "Почта"`]')
        self.input_login_password = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeSecureTextField[`value == "Пароль"`]')
        self.btn_cancel = (self.ACCESSIBILITY_ID, 'Отмена')
        self.btn_login = (self.ACCESSIBILITY_ID, 'ВОЙТИ')
        self.btn_auth_apple = (self.ACCESSIBILITY_ID, 'Continue with Apple')
        self.btn_vk = (self.ACCESSIBILITY_ID, 'ВКонтакте')
        self.btn_fb = (self.ACCESSIBILITY_ID, 'Facebook')
        self.btn_lj = (self.ACCESSIBILITY_ID, 'LiveJournal')
        self.btn_ok = (self.ACCESSIBILITY_ID, 'Одноклассники')
        self.btn_more = (self.ACCESSIBILITY_ID, 'Открыть')
        self.text_invalid_fields = (self.ACCESSIBILITY_ID, 'Неправильная почта или пароль')
        self.input_vk_login = (self.IOS_PREDICATE, 'type == "XCUIElementTypeTextField"')
        self.input_vk_password = (self.IOS_PREDICATE, 'type == "XCUIElementTypeSecureTextField"')
        self.btn_vk_login = (self.ACCESSIBILITY_ID, 'Sign in')
        self.btn_popup_next = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "ПОНЯТНО"`]')
        self.text_popup_header = (self.ACCESSIBILITY_ID, 'Профиль')
        self.text_verification_fields = (self.ACCESSIBILITY_ID, 'Пройдите верификацию, пожалуйста')
