from tests.precondition_test import LoginDatabaseRunner
from teachua.database.models import Role, User, Task


class TestDatabaseRelationship(LoginDatabaseRunner):

    def test_example(self):
        print("\n[Role]\n")
        roles = self.session.query(Role).all() # SELECT * FROM roles;
        for role in roles:
            print(role)

        print("\n[User]\n")
        users = self.session.query(User).filter_by(first_name="Анастасія").all() # SELECT * FROM users WHERE first_name = ?;
        for user in users:
            print(user)

        print("\n[Task]\n")
        task = self.session.query(Task).first() # SELECT * FROM tasks LIMIT 1;
        print(task)
