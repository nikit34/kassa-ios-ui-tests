from appium.webdriver.common.mobileby import MobileBy


class PlacesPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.tab = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "МЕСТА"`]')
        self.block_search = (self.ACCESSIBILITY_ID, 'searchView')
        self.btn_map = (self.ACCESSIBILITY_ID, 'mapButton')
        self.row_labels = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView[`name == "collectionView"`][2]')
        self.btn_allow_location = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Разрешить геолокацию"`]')
        self.btn_cancel_location = (self.ACCESSIBILITY_ID, 'Cross')
        self.btn_popup_next = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "ПОНЯТНО"`]')
        self.row_events = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable[`name == "tableView"`]/XCUIElementTypeCell[2]')