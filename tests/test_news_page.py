from tests.precondition_test import LoginRunner
from teachua.pages.home_page import HomePage
from parameterized import parameterized


class TestNewsPage(LoginRunner):

    """Implementation of TUA-31
    """
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
