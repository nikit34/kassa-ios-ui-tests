from appium.webdriver.common.mobileby import MobileBy


class PerformancePageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.tab = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "ТЕАТРЫ"`]')
        self.text_event_title = (self.ACCESSIBILITY_ID, 'eventNameLabel')
        self.text_title = (self.ACCESSIBILITY_ID, 'PopularEventTableCell.headerView.titleLabel')
        self.text_data = (self.ACCESSIBILITY_ID, 'dateLabel')
        self.text_time = (self.ACCESSIBILITY_ID, 'timeLabel')
        self.btn_price = (self.ACCESSIBILITY_ID, 'gradientButton')
        self.video_row_carousel = (self.IOS_PREDICATE, 'name == "teaserTableCell"')
        self.text_popular_title = (self.ACCESSIBILITY_ID, 'PopularEventTableCell.headerView.titleLabel')
        self.text_popular_event_name = (self.ACCESSIBILITY_ID, 'PopularEventCollectionCell.0.titleLabel')
        self.img_popular = (self.ACCESSIBILITY_ID, 'PopularEventCollectionCell.0.overlayView')
        self.btn_popular_all = (self.ACCESSIBILITY_ID, 'PopularEventTableCell.headerView.allButton')