from .habit import Habit # Ensure Habit is imported

class User:
    def __init__(self, username):
        self.username = username
        self.habits = [] # List of Habit objects

    def add_habit(self, habit):
        if not isinstance(habit, Habit):
            raise ValueError("Can only add Habit objects to a user.")
        self.habits.append(habit)

    def get_habits(self):
        return self.habits

    def to_dict(self):
        return {
            "username": self.username,
            "habits": [habit.to_dict() for habit in self.habits]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data['username'])
        user.habits = [Habit.from_dict(h_data) for h_data in data.get('habits', [])]
        return user
