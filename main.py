from time import sleep
from os import system
from menu import show_menu
from view import view_tasks
from add_new_task import add_task
from delete_task import delete_task
from update_task import update_task


if __name__ == '__main__':
    while True:
        option = show_menu()
        if option == "1":
            add_task()
        elif option == "2":
            delete_task()
        elif option == "3":
            view_tasks()
        elif option == "4":
            update_task()
        elif option == "5":
            break
        else:
            print("Invalid option")
            sleep(1)
            system("clear")
