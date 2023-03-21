from tests.precondition_test import LoginSessionRunner
from teachua.pages.home_page import HomePage
from teachua.pages.tasks_page import AddTaskPage
from teachua.database.models import Task, Club
from parameterized import parameterized
from utils.functions import time, get_photo_path
from utils.constants import Urls
import allure
import json

ERROR_MESSAGES = [
    "Поле 'Заголовок' не може бути пустим",
    "Поле 'Заголовок' може містити тільки українські та англійські літери, цифри та спеціальні символи",
    "Поле 'Заголовок' може містити мінімум 40 максимум 3000 символів",
    "Фото не може бути пустим"
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
        
        task = self.session.query(Task).filter_by(name=name).first()

        self.assertTrue(are_fields_empty)
        self.assertListEqual([actual_alert_msg, task], [expected_alert_msg, None])
    
    @parameterized.expand([
        (10, 10, 2030, "test-name-1", ("test-title-1" * 5), 
         ("test-description-1" * 5), 1, ERROR_MESSAGES[3])
    ])
    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-522", "TUA-522")
    @allure.severity(allure.severity_level.NORMAL)
    def test_task_photo_invalid(self, day, month, year, name, title, 
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
            .enter_task_name(name) \
            .enter_task_title(title) \
            .enter_description(description) \
            .choose_challenge(challenge_idx) \
            .click_save_button() \
            .get_alert_msg()
        
        task = self.session.query(Task).filter_by(name=name).first()

        self.assertTrue(are_fields_empty)
        self.assertListEqual([actual_alert_msg, task], [expected_alert_msg, None])
    
    @parameterized.expand([
        (f"club-name-{int(time.time())}", 0, "10", "15", "1212121212",
         ("some data;" * 5), "Гурток успішно створено")
    ])
    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-506", "TUA-506")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_club(self, name, number, age_from, age_to, 
                         phone, description, expected_success_msg):
        home_page = HomePage(self.driver)

        actual_success_msg = home_page.header \
            .move_to_user_menu() \
            .click_add_club() \
            .enter_club_name(name) \
            .choose_category(number) \
            .enter_age_from(age_from) \
            .enter_age_to(age_to) \
            .click_next_step() \
            .enter_phone(phone) \
            .click_next_step() \
            .enter_description(description) \
            .click_finish_button() \
            .get_success_msg()
        
        club = self.session.query(Club).filter_by(name=name).first()
        
        self.assertEqual(actual_success_msg, expected_success_msg)
        self.assertListEqual(
            [club.name, json.loads(club.description)["blocks"][0]["text"]],
            [name, description]
        )
