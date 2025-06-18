import unittest
import datetime
from src.user import User
from src.habit import Habit

class TestHabit(unittest.TestCase):

    def test_add_habit_to_user(self):
        user = User("testuser")
        habit = Habit("Exercise", "Daily jogging", "daily")
        user.add_habit(habit)
        self.assertIn(habit, user.get_habits())
        self.assertEqual(len(user.get_habits()), 1)
        self.assertEqual(user.get_habits()[0].name, "Exercise")

    def test_mark_habit_complete(self):
        habit = Habit("Read", "Read a book", "daily")
        test_date = datetime.date(2023, 1, 15)
        habit.mark_complete(test_date)
        self.assertIn(test_date, habit.completed_dates)

    def test_mark_habit_complete_today(self):
        habit = Habit("Meditate", "Morning meditation", "daily")
        today = datetime.date.today()
        habit.mark_complete() # Should default to today
        self.assertIn(today, habit.completed_dates)

    def test_is_completed_on(self):
        habit = Habit("Write", "Journaling", "daily")
        test_date = datetime.date(2023, 1, 20)
        habit.mark_complete(test_date)
        self.assertTrue(habit.is_completed_on(test_date))
        self.assertFalse(habit.is_completed_on(datetime.date(2023, 1, 21)))

    def test_mark_habit_complete_idempotent(self):
        habit = Habit("Water Plants", "Water all house plants", "weekly")
        test_date = datetime.date(2024, 1, 1)
        habit.mark_complete(test_date)
        habit.mark_complete(test_date) # Mark complete again for the same date
        self.assertEqual(len(habit.completed_dates), 1)


if __name__ == '__main__':
    unittest.main()
