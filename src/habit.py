import datetime

class Habit:
    def __init__(self, name, description, frequency):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.completed_dates = [] # List of datetime.date objects

    def mark_complete(self, date=None):
        if date is None:
            date = datetime.date.today()
        if not isinstance(date, datetime.date): # Ensure it's a date object
            raise ValueError("Completed date must be a datetime.date object")
        if date not in self.completed_dates:
            self.completed_dates.append(date)
        self.completed_dates.sort() # Keep dates sorted

    def is_completed_on(self, date):
        if not isinstance(date, datetime.date): # Ensure it's a date object
            raise ValueError("Date to check must be a datetime.date object")
        return date in self.completed_dates

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "frequency": self.frequency,
            "completed_dates": [d.isoformat() for d in self.completed_dates]
        }

    @classmethod
    def from_dict(cls, data):
        habit = cls(data['name'], data['description'], data['frequency'])
        habit.completed_dates = sorted([datetime.date.fromisoformat(d_str) for d_str in data.get('completed_dates', [])])
        return habit
