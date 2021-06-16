APPIUM_HOST = 'http://10.60.17.45:4723/wd/hub'  # host
APPIUM_LOCAL = 'http://0.0.0.0:4723/wd/hub'  # local

DESIRED_CAPS_NO_CACHE_HOST = {
    'platformName': 'iOS',
    'automationName': 'XCUITest',
    'platformVersion': '14.4',
    'deviceName': 'iPhone 12 Pro Max',  # host
    'useJSONSource': True,
    'noReset': False,
    'wdaLocalPort': 8100,
    'wdaBaseUrl': 'http://10.60.17.45'
}

DESIRED_CAPS_HOST = {
    'platformName': 'iOS',
    'automationName': 'XCUITest',
    'platformVersion': '14.4',
    'deviceName': 'iPhone 12 Pro Max',  # host
    'useJSONSource': True,
    'noReset': True,
    'wdaLocalPort': 8100,
    'wdaBaseUrl': 'http://10.60.17.45'
}

DESIRED_CAPS_NO_CACHE_LOCAL = {
    'platformName': 'iOS',
    'automationName': 'XCUITest',
    'platformVersion': '14.4',
    'deviceName': 'iPhone 12 Pro Max',  # local
    'useJSONSource': True,
    'noReset': False,
    'wdaLocalPort': 8100,
    'wdaBaseUrl': 'http://localhost',
    'app': '/Users/n.permyakov/kassa/ios-ui-tests/app/Kassa.app',  # local
}

DESIRED_CAPS_LOCAL = {
    'platformName': 'iOS',
    'automationName': 'XCUITest',
    'platformVersion': '14.4',
    'deviceName': 'iPhone 12 Pro Max',  # local
    'useJSONSource': True,
    'noReset': True,
    'wdaLocalPort': 8100,
    'wdaBaseUrl': 'http://localhost',
    'app': '/Users/n.permyakov/kassa/ios-ui-tests/app/Kassa.app',  # local
}


# treasured scroll
# any time and any questions, Nikita, @nikit34