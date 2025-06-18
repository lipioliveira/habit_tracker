from src import create_user, login_user, User, Habit
import datetime

def display_habits(user):
    habits = user.get_habits()
    if not habits:
        print("No habits yet. Add one!")
        return

    print("\n--- Your Habits ---")
    for i, habit in enumerate(habits):
        today_str = datetime.date.today().isoformat()
        status = "Done" if habit.is_completed_on(datetime.date.today()) else "Pending"
        print(f"{i+1}. {habit.name} ({habit.frequency}) - Today: {status}")
    print("--------------------")

def main_menu(current_user):
    while True:
        print(f"\nLogged in as: {current_user.username}")
        display_habits(current_user)
        print("\nWhat would you like to do?")
        print("1. Add a new habit")
        print("2. Mark habit as complete (for today)")
        print("3. View habit details (not implemented yet)")
        print("4. Logout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter habit name: ")
            description = input("Enter habit description: ")
            frequency = input("Enter habit frequency (e.g., daily, weekly): ")
            habit = Habit(name, description, frequency)
            current_user.add_habit(habit)
            print(f"Habit '{name}' added.")
        elif choice == '2':
            habits = current_user.get_habits()
            if not habits:
                print("No habits to mark.")
                continue
            try:
                habit_num = int(input("Enter habit number to mark as complete: "))
                if 1 <= habit_num <= len(habits):
                    habits[habit_num-1].mark_complete()
                    print(f"Habit '{habits[habit_num-1].name}' marked as complete for today.")
                else:
                    print("Invalid habit number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            print("This feature is not implemented yet.")
        elif choice == '4':
            print("Logging out...")
            return # Goes back to login/signup
        elif choice == '5':
            print("Exiting Habit Tracker. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Welcome to Habit Tracker!")
    current_user = None

    while True:
        if not current_user:
            print("\nPlease login or create an account:")
            print("1. Login")
            print("2. Create User")
            print("3. Exit")
            auth_choice = input("Enter your choice: ")

            if auth_choice == '1':
                username = input("Enter username: ")
                user = login_user(username)
                if user:
                    current_user = user
                    print(f"Welcome back, {username}!")
                else:
                    print("Login failed. User not found.")
            elif auth_choice == '2':
                username = input("Enter new username: ")
                try:
                    current_user = create_user(username)
                    print(f"User '{username}' created successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
            elif auth_choice == '3':
                print("Exiting Habit Tracker. Goodbye!")
                break
            else:
                print("Invalid choice.")
        else:
            main_menu(current_user)
            current_user = None # Reset after logout to show login/signup again

if __name__ == "__main__":
    main()
