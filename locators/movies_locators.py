from appium.webdriver.common.mobileby import MobileBy


class MoviesPageLocators(MobileBy):
    def __init__(self):
        super(MobileBy, self).__init__()

        self.text_title = (self.ACCESSIBILITY_ID, 'TopEventTableCell.headerView.titleLabel')
        self.text_movie_title = (self.ACCESSIBILITY_ID, 'eventNameLabel')
        self.text_info_block = (self.ACCESSIBILITY_ID, 'teaserEventInfoView')
        self.video_row_carousel = (self.ACCESSIBILITY_ID, 'teaserTableCell')
        self.text_place = (self.ACCESSIBILITY_ID, 'nearestPlaceLabel')
        self.row_times_sessions = (self.ACCESSIBILITY_ID, 'nearestSessionsView')
        self.btn_time_session = (self.ACCESSIBILITY_ID, 'sessionView')
        self.btn_back = (self.IOS_PREDICATE, 'label == "Назад"')
        self.btn_try_right = (self.ACCESSIBILITY_ID, '**/XCUIElementTypeButton[`label == "Попробовать ещё раз"`]')
        self.img_banner = (self.ACCESSIBILITY_ID, 'bannerImageView')
        self.img_row_top = (self.ACCESSIBILITY_ID, 'TopEventsCollectionCell.0.imageContentView')
        self.text_row_popular_title = (self.ACCESSIBILITY_ID, 'PopularEventTableCell.headerView.titleLabel')
        self.text_row_popular_all = (self.ACCESSIBILITY_ID, 'PopularEventTableCell.headerView.allButton')
        self.text_row_popular = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[`name == "PopularEventCollectionCell.0"`]/XCUIElementTypeOther')
        self.img_row_popular = (self.ACCESSIBILITY_ID, 'popularEventTableCell')
        self.text_row_premiers_title = (self.ACCESSIBILITY_ID, 'PremiereTableCell.headerView.titleLabel')
        self.text_row_premiers_all = (self.ACCESSIBILITY_ID, 'PremiereTableCell.headerView.allButton')
        self.text_row_premiers_name = (self.ACCESSIBILITY_ID, 'PremiereCollectionCell.0.titleLabel')
        self.img_row_premiers = (self.ACCESSIBILITY_ID, 'PremiereCollectionCell.0.overlayView')
        self.btn_popup_next = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "ПОНЯТНО"`]')
        self.text_popup_header = (self.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Топовые события"`]')