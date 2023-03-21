from tests.precondition_test import LoginSessionRunner
from teachua.pages.home_page import HomePage
from teachua.pages.tasks_page import AddTaskPage
from teachua.database.models import Task
from parameterized import parameterized
from utils.functions import get_photo_path
from utils.constants import Urls
import allure

ERROR_MESSAGES = [
    "Поле 'Заголовок' не може бути пустим",
    "Поле 'Заголовок' може містити тільки українські та англійські літери, цифри та спеціальні символи",
    "Поле 'Заголовок' може містити мінімум 40 максимум 3000 символів"
]


class TestUiDatabase(LoginSessionRunner):

    @parameterized.expand([
        (24, 12, 2025, "test-img-1.jpg", "test-name-1", "", 
         ("test-description-1" * 5), 1, ERROR_MESSAGES[0]),
        (24, 12, 2025, "test-img-1.jpg", "test-name-2", ("Aussätzige|Прокаженные" * 5), 
         ("test-description-2" * 5), 2, ERROR_MESSAGES[1]),
        (24, 12, 2025, "test-img-1.jpg", "test-name-3", "test-title",
         ("test-description-3" * 5), 3, ERROR_MESSAGES[2]),
        (24, 12, 2025, "test-img-1.jpg", "test-name-4", ("title-title" * 300),
         ("test-description-4" * 5), 4, ERROR_MESSAGES[2])
    ])
    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-524", "TUA-524")
    @allure.severity(allure.severity_level.NORMAL)
    def test_task_title_invalid(self, day, month, year, photo_path, name, title, 
                                description, challenge_idx, expected_alert_msg):
        home_page = HomePage(self.driver)
        add_task_page = AddTaskPage(self.driver)

        are_fields_empty = home_page.header \
            .move_to_admin_menu() \
            .move_to_tasks() \
            .click_add_task() \
            .are_fields_empty()

        actual_alert_msg = add_task_page \
            .select_start_date(day, month, year) \
            .upload_photo(get_photo_path(photo_path)) \
            .enter_task_name(name) \
            .enter_task_title(title) \
            .enter_description(description) \
            .choose_challenge(challenge_idx) \
            .click_save_button() \
            .get_alert_msg()
        
        sql_query = self.session.query(Task).filter_by(name=name).first()

        self.assertTrue(are_fields_empty)
        self.assertListEqual([actual_alert_msg, sql_query], [expected_alert_msg, None])
    
    def test_task_photo_invalid(self):
        pass
