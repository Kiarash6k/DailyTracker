from os import system


def show_menu():
    print("1. Add a new task.")
    print("2. Delete an existing task.")
    print("3. View all existing tasks.")
    print("4. Update an existing task.")
    print("5. Exit.")
    chosen_option = input("Enter option: ")
    system("clear")
    return chosen_option
