
from blinking import blink
from os import system
from time import sleep
import termcolor

tasks = {}
def update_task():
    task = input("Enter the task to update: ")
    if task in tasks:
        chapters_studied = input("Enter the number of chapters studied: ")

        if int(chapters_studied) > int(tasks[task][0] or int(chapters_studied)== 0):
            blink("Invalid number of chapters studied.Try again.")
            update_task()
        else:
            tasks[task][1] = chapters_studied
            sleep(1)
            termcolor.cprint("Task updated successfully.", "green")
            sleep(1)
            with open("tasks.txt", "w") as f:
                for task in tasks:
                    f.write(f"{task} {tasks[task][0]} {tasks[task][1]}\n")
            system("clear")
    else:
        blink("Task does not exist.")
