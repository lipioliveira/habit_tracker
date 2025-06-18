import unittest
from src.auth import create_user, login_user, get_all_users, users # Import users for clearing
from src.user import User

class TestAuth(unittest.TestCase):

    def setUp(self):
        # Clear users before each test to ensure isolation
        users.clear()

    def test_create_user_success(self):
        user = create_user("testuser")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser")
        self.assertIn("testuser", get_all_users())

    def test_create_user_duplicate(self):
        create_user("testuser")
        with self.assertRaises(ValueError):
            create_user("testuser")

    def test_login_user_success(self):
        create_user("testuser")
        user = login_user("testuser")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser")

    def test_login_user_not_found(self):
        user = login_user("nonexistentuser")
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
