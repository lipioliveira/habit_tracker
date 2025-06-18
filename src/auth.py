from .user import User
from .storage import save_data, load_data # Import persistence functions

# Load users from file when the module is initialized
users = load_data() # This now returns a dict of User objects

def create_user(username):
    """Creates a new user if the username doesn't already exist and saves all users."""
    if username in users:
        raise ValueError(f"User '{username}' already exists.")
    user = User(username)
    users[username] = user
    save_data(users) # Save after creating a new user
    return user

def login_user(username):
    """Logs in a user if the username exists. Data is loaded at startup."""
    return users.get(username)

def get_all_users():
    """Returns a dictionary of all users."""
    return users

# It's good practice to have an explicit save function if needed elsewhere,
# but for now, create_user handles the saving.
# def save_all_users_data():
#     save_data(users)
