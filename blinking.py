
from os import system
from time import sleep
import termcolor

def blink(message):
    termcolor.cprint(message, "red", attrs=["blink"])
    sleep(1)
    system("clear")

