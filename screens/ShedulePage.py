import json
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from random import randint

from locators.shedule_locators import ShedulePageLocators
from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout


class ShedulePage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.shedule_locators = ShedulePageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    @staticmethod
    def get_content_creations_movie_schedule(dbg_api):
        for req_line in dbg_api.read_buffer(name_file='redis_filter.log'):
            sep_req_line = req_line.split(';', 4)
            return json.loads(sep_req_line[4])
        raise ValueError('[FAILED] dont found')

    @staticmethod
    def get_first_row_filters(content):
        first_row = []
        content_filters = content['composedFilters'][0]['filters']
        for content_filter in content_filters:
            content_filter_options = content_filter['options']
            first_row_item = {}
            for content_filter_option in content_filter_options:
                first_row_item['title'] = content_filter_option['title']
                first_row_item['isSelected'] = content_filter_option['isSelected']
                first_row_item['isDisabled'] = content_filter_option['isDisabled']
            first_row.append(first_row_item)
        return first_row

    @staticmethod
    def get_datetime_options(content):
        datetime_struct = []
        content_options = content['filters'][1]['options']
        for content_option in content_options:
            datetime_obj = datetime.strptime(content_option['value'], '%Y-%m-%d')
            datetime_struct.append(datetime_obj)
        return datetime_struct

    @staticmethod
    def get_second_row_filters(content, get_datetime_options):
        def convert_name_day(datetime_name_day):
            name_day = None
            if datetime_name_day == 'Sunday':
                name_day = 'Вс'
            elif datetime_name_day == 'Monday':
                name_day = 'Пн'
            elif datetime_name_day == 'Tuesday':
                name_day = 'Вт'
            elif datetime_name_day == 'Wednesday':
                name_day = 'Ср'
            elif datetime_name_day == 'Thursday':
                name_day = 'Чт'
            elif datetime_name_day == 'Friday':
                name_day = 'Пт'
            elif datetime_name_day == 'Saturday':
                name_day = 'Сб'
            if name_day is not None:
                return name_day
            raise ValueError('[ERROR] name_day is not valid format')

        datetime_sort = get_datetime_options(content)
        datetime_sort.sort()
        second_row = []
        first_row_item = {}
        for datetime_obj in datetime_sort:
            datetime_name_day = datetime_obj.strftime("%A")
            first_row_item['number_day'] = datetime_obj.day
            first_row_item['name_day'] = convert_name_day(datetime_name_day)
            second_row.append(first_row_item.copy())
        return second_row

    def _find_first_filter(self, locators, count_swipe):
        try:
            self.find_element(*locators)
        except NoSuchElementException:
            if count_swipe < 8:
                self.act.swipe(80, 33, 20, 33)
                count_swipe += 1
                self._find_first_filter(locators, count_swipe)
            else:
                raise NoSuchElementException('elem of first filter dont found')
        for _ in range(count_swipe):
            self.act.swipe(20, 33, 80, 33)

    def check_first_row_filters(self, row):
        for item_row in row:
            selector = item_row['title']
            if selector != 'IMAX':
                selector = selector.capitalize()
            locators = (self.shedule_locators.ACCESSIBILITY_ID, selector)
            self._find_first_filter(locators, 0)

    def check_second_row_filters(self, row):
        current_base_locator_copy = self.shedule_locators.template_base_second_filters.copy()
        number_text_locator_copy = self.shedule_locators.template_text_second_filters.copy()
        name_text_locator_copy = self.shedule_locators.template_text_second_filters.copy()
        text_split_second_filter_selector = self.shedule_locators.template_text_second_filters[1].split('"')
        for i, item_row in enumerate(row):
            if i < 5:
                current_base_locator_copy[1] = self.shedule_locators.template_base_second_filters[1][:-1] + str(
                    i + 1) + ']'
                base_filter = self.find_element(*current_base_locator_copy)
                number_text_locator_copy[1] = text_split_second_filter_selector[0] + '"' + str(
                    item_row['number_day']) + '"' + text_split_second_filter_selector[2]
                base_filter.find_element(*number_text_locator_copy)
                name_text_locator_copy[1] = text_split_second_filter_selector[0] + '"' + item_row['name_day'] + '"' + \
                                            text_split_second_filter_selector[2]
                try:
                    base_filter.find_element(*name_text_locator_copy)
                except NoSuchElementException:
                    name_text_locator_copy[1] = name_text_locator_copy[1] + '[1]'
                    base_filter.find_element(*name_text_locator_copy)

    def check_rows_filters(self, dbg_api):
        content = self.get_content_creations_movie_schedule(dbg_api)
        first_row_filters = self.get_first_row_filters(content)
        self.check_first_row_filters(first_row_filters)
        second_row_filters = self.get_second_row_filters(content, self.get_datetime_options)
        self.check_second_row_filters(second_row_filters)

    @staticmethod
    def get_tickets(content):
        tickets = []
        for ticket in content['placeSchedules']:
            ticket_name = ticket['place']['name']
            ticket_address = ticket['place']['address']
            sessions = []
            for current_session in ticket['sessions']:
                sessions.append(current_session['time'])
            metros = []
            if 'metro' in ticket['place']:
                for current_metro in ticket['place']['metro']:
                    metros.append(current_metro['name'])
            ticket = {
                'ticket_name': ticket_name,
                'ticket_address': ticket_address,
                'sessions': sessions,
                'metros': metros
            }
            tickets.append(ticket)
        return tickets

    def _get_locators_ticket_single_field(self, ticket, ticket_field, text_split_ticket_top_selector):
        template_ticket_copy = self.shedule_locators.template_ticket_top.copy()
        template_ticket_copy[1] = text_split_ticket_top_selector[0] + '"' + \
                                       ticket[ticket_field] + '"' + \
                                       text_split_ticket_top_selector[2]
        return template_ticket_copy

    def _get_locators_ticket_more_field(self, ticket, ticket_field, text_split_ticket_top_selector):
        template_ticket_copy = self.shedule_locators.template_ticket_top.copy()
        templates_ticket_more_copy = []
        for m in ticket[ticket_field]:
            template_ticket_copy[1] = text_split_ticket_top_selector[0] + '"' + m + '"' + \
                                            text_split_ticket_top_selector[2]
            templates_ticket_more_copy.append(template_ticket_copy)
        return templates_ticket_more_copy
    
    def _search_ticket(self, template_ticket_name_copy, template_ticket_address_copy, templates_ticket_metro_copy):
        self.find_element(*template_ticket_name_copy)
        self.find_element(*template_ticket_address_copy)
        random_index_metro = randint(0, len(templates_ticket_metro_copy) - 1)
        self.find_element(*templates_ticket_metro_copy[random_index_metro])

    def _find_or_swipe_ticket(self, ticket):
        text_split_ticket_top_selector = self.shedule_locators.template_ticket_top[1].split('"')
        template_ticket_name_copy = self._get_locators_ticket_single_field(ticket, 'ticket_name', text_split_ticket_top_selector)
        template_ticket_address_copy = self._get_locators_ticket_single_field(ticket, 'ticket_address', text_split_ticket_top_selector)
        templates_ticket_metro_copy = self._get_locators_ticket_more_field(ticket, 'metros', text_split_ticket_top_selector)
        last_wait = self.get_last_wait()
        self.set_custom_wait(5)
        try:
            self._search_ticket(template_ticket_name_copy, template_ticket_address_copy, templates_ticket_metro_copy)
        except NoSuchElementException:
            self.act.swipe(50, 60, 50, 40)
            self._search_ticket(template_ticket_name_copy, template_ticket_address_copy, templates_ticket_metro_copy)
        self.set_custom_wait(last_wait)

    def _search_ticket_by_datetime_options(self, tickets, datetime_options, i):
        for j, ticket in enumerate(tickets):
            datetime_options_day = str(datetime_options[i].day)
            if len(datetime_options_day) == 1:
                datetime_options_day = '0' + datetime_options_day
            count_coincidences = 0
            for session in ticket['sessions']:
                ticket_day = session[8:10]
                if datetime_options_day == ticket_day:
                    count_coincidences += 1
            if count_coincidences <= len(ticket['sessions']):
                self._find_or_swipe_ticket(ticket)
            else:
                raise ValueError("[FAILED] There are sessions for other days")

    def _click_next_second_filter(self, text_locator, text_split_second_filter_selector, datetime_options):
        text_locator[1] = text_split_second_filter_selector[0] + '"' + str(datetime_options[i + 1].day) + '"' + \
                          text_split_second_filter_selector[2]
        elem = self.find_element(*text_locator)
        self.click_elem(elem)

    def compare_date(self, datetime_options, tickets, dbg_api):
        text_locator = self.shedule_locators.template_text_second_filters
        text_split_second_filter_selector = text_locator[1].split('"')
        len_section_options = 4
        for i in range(len_section_options):
            self._search_ticket_by_datetime_options(tickets, datetime_options, i)
            self._click_next_second_filter(text_locator, text_split_second_filter_selector, datetime_options)
            content = self.get_content_creations_movie_schedule(dbg_api)
            tickets = self.get_tickets(content)
            self.compare_date(datetime_options, tickets, dbg_api)

    def compare_tickets_datetime_options_second_filter(self, dbg_api):
        content = self.get_content_creations_movie_schedule(dbg_api)
        datetime_options = self.get_datetime_options(content)
        tickets = self.get_tickets(content)
        datetime_options.sort()
        self.compare_date(datetime_options, tickets, dbg_api)

    @staticmethod
    def url_creations_movie_schedule_filter(msg):
        req_line = msg['data'].decode('utf-8')
        sep_req_line = req_line.split(';', 4)
        if len(sep_req_line) == 5 \
                and sep_req_line[1] == 'response' \
                and sep_req_line[2] == 'GET' \
                and '/creations/movie/' in sep_req_line[3] \
                and '/schedule' in sep_req_line[3]:
            with open('../../app/redis_filter.log', 'w') as f:
                f.write(req_line)