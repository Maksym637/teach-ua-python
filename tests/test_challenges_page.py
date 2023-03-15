from tests.precondition_test import LoginRunner
from teachua.pages.home_page import HomePage
from teachua.pages.challenges_page import AddChallengePage
from parameterized import parameterized
from utils.functions import get_photo_path
from utils.constants import Urls
import allure


class TestChallengesPage(LoginRunner):

    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-151", "TUA-151")
    @allure.severity(allure.severity_level.NORMAL)
    @parameterized.expand([
        ("151", "test-name-1", "test-title-1", ("test-description-1" * 5),
         "test-img-1.jpg", "Челендж 'test-name-1' успішно доданий!"),
        ("152", "test-name-2", "test-title-2", ("test-description-2" * 5),
         "test-img-1.jpg", "Челендж 'test-name-2' успішно доданий!")
    ])
    def test_add_challenge_valid(self, sort_number, name, title,
                                 description, photo_path, expected_success_msg):
        home_page = HomePage(self.driver)
        add_challenge_page = AddChallengePage(self.driver)

        actual_success_msg = home_page.header \
            .move_to_admin_menu() \
            .move_to_challenges() \
            .click_add_challenge() \
            .enter_sort_number(sort_number) \
            .enter_challenge_name(name) \
            .enter_challenge_title(title) \
            .enter_description(description) \
            .upload_photo(get_photo_path(photo_path)) \
            .click_save_button() \
            .check_success_message()
        
        add_challenge_page \
            .go_to_challenges() \
            .search_challenge(name) \
            .click_search() \
            .click_delete_challenge() \
            .confirm_delete_challenge()
        
        self.assertEqual(actual_success_msg, expected_success_msg)
