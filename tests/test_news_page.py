from tests.precondition_test import LoginRunner
from teachua.pages.home_page import HomePage
from teachua.pages.news_page import NewsPage
from utils.functions import sort_dates
from parameterized import parameterized
from utils.constants import Urls
import allure


class TestNewsPage(LoginRunner):

    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-31", "TUA-31")
    @allure.severity(allure.severity_level.NORMAL)
    @parameterized.expand([
        ("Київ", "Гуртки у місті Київ"),
        ("Харків", "Гуртки у місті Харків"),
        ("Дніпро", "Гуртки у місті Дніпро"),
        ("Одеса", "Гуртки у місті Одеса"),
        ("Львів", "Гуртки у місті Львів")
    ])
    def test_button_activity(self, location, expected_clubs_title):
        home_page = HomePage(self.driver)

        actual_news_buttons = []
        news_amount = home_page.header.click_news_button().get_all_news()

        for i in range(news_amount):
            actual_news_buttons.append(
                home_page.header \
                    .click_news_button() \
                    .choose_news_card(i) \
                    .click_details_button() \
                    .is_donate_button_enabled()
            )
        
        actual_clubs_buttons = []
        clubs_amount = home_page.header.click_news_button().get_all_clubs()

        for i in range(clubs_amount):
            actual_clubs_buttons.append(
                home_page.header \
                    .click_news_button() \
                    .choose_club_card(i) \
                    .click_details_button() \
                    .is_subscribe_button_enabled()
            )
        
        actual_clubs_title = home_page.header \
            .click_location_button() \
            .choose_location(location) \
            .click_news_button() \
            .get_clubs_title()
        
        self.assertEqual(actual_news_buttons, [True, True, True, True])
        self.assertEqual(actual_clubs_buttons, [True, True, True])
        self.assertEqual(actual_clubs_title, expected_clubs_title)
    
    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-146", "TUA-146")
    @allure.severity(allure.severity_level.NORMAL)
    def test_news_blocks_order(self):
        home_page = HomePage(self.driver)
        news_page = NewsPage(self.driver)

        actual_news_date = []

        news_amount = home_page.header \
            .click_news_button() \
            .get_all_news()
        
        for i in range(news_amount):
            actual_news_date.append(
                news_page.choose_news_card(i).get_news_date()
            )
        
        self.assertListEqual(
            actual_news_date, sorted(actual_news_date, key=sort_dates, reverse=True)
        )
