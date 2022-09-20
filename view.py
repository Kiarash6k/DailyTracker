
from time import sleep
from os import system
import termcolor
import tqdm
from blinking import blink
tasks = {}

def view_tasks():
    with open("tasks.txt", "r") as f:
        for task in f.readlines():
            if task=="":
                pass
            task = task.split()
            tasks[task[0]] = [task[1], task[2]]
    if len(tasks) == 0:
        blink("No tasks to show.")
    else:

        for task in tasks:

            print(f"Task : {task} | Chapters to study: {tasks[task][0]} | Chapters studied: {tasks[task][1]}")
            if tasks[task][0] == tasks[task][1]:
                termcolor.cprint("Task completed.", "green")
                with tqdm.tqdm(total=int(tasks[task][0]), colour="green") as pbar:
                    for i in range(int(tasks[task][1])):
                        pbar.update(1)
                        sleep(0.1)
            else:

                with tqdm.tqdm(total=int(tasks[task][0]), colour="yellow") as pbar:
                    for i in range(int(tasks[task][1])):
                        pbar.update(1)
                        sleep(0.1)
        input("Press enter to continue.")
        system("clear")
