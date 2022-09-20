from time import sleep
from os import system
import termcolor
from blinking import blink
tasks = {}
def delete_task():
    task = input("Enter the task to delete: ")
    if not task:
        blink("Invalid Input, Try Again!!")
        delete_task()
    if task in tasks:
        del tasks[task]
        sleep(2)
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(f"{task} {tasks[task][0]} {tasks[task][1]}\n")
        termcolor.cprint("Task deleted successfully.", "green")
        sleep(2)
        system("clear")
    else:
        blink("Task does not exist.")
