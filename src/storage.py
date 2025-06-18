import json
import datetime
from .user import User
from .habit import Habit

def serialize_datetime(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    raise TypeError("Type not serializable")

def deserialize_datetime(iso_date_str):
    return datetime.date.fromisoformat(iso_date_str)

def save_data(users_dict, filepath="data.json"):
    data_to_save = {
        username: user.to_dict() for username, user in users_dict.items()
    }
    with open(filepath, 'w') as f:
        json.dump(data_to_save, f, default=serialize_datetime, indent=4)

def load_data(filepath="data.json"):
    try:
        with open(filepath, 'r') as f:
            loaded_data = json.load(f)

        users_from_data = {}
        for username, user_data in loaded_data.items():
            users_from_data[username] = User.from_dict(user_data)
        return users_from_data
    except FileNotFoundError:
        return {} # Return empty dict if no data file
    except json.JSONDecodeError:
        print("Error decoding data.json. Starting with empty data.")
        return {}
