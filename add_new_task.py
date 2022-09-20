
from blinking import blink
from os import system
from time import sleep
import termcolor

tasks={}
def add_task():
    while True:
        task = input("Enter a new task: ")
        if  task=="":
            blink("Invalid Input, Try Again!!")
        else:
            break

    while True:
        chapters_to_study = input("Enter the number of chapters to study: ")
        if not chapters_to_study:
            blink("Invalid Input, Try Again!!")
        else:
            break
    tasks[task] = [chapters_to_study, 0]
    sleep(.5)
    termcolor.cprint("Task added successfully.", "green")
    sleep(.5)
    system("clear")
    with open("tasks.txt", "a") as f:
        f.write(f"{task} {chapters_to_study} 0\n")

