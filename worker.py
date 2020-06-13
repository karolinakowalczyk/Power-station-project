from malfunctions import Malfunctions
from enum import Enum
import random


# Enum for worker status
class Status(Enum):
    IDLE = "idle"
    WORKING = "working"


class Worker:
    # eff parameter means efficiency of the worker.
    # We can assume that the value of 100 is a default value.
    def __init__(self, number, eff: int, salary: int):
        self.number = number
        self.eff = eff
        self.salary = salary  # monthly payment in eurogąbki
        self.status = Status.IDLE
        self.malfunction = None

    def __str__(self):
        if self.status == Status.IDLE:
            return "Worker no. " + str(self.number) + " is idle"
        else:
            return "Worker no. " + str(self.number) + " is working on malfunction " + self.malfunction.get_malname()

    # Workers are sometimes tired, sometimes excited at work. Their efficiency should vary from day to day.
    def randomize_eff(self):
        self.eff += random.randint(-5, 5)

    # Method should be called when the worker is expected to work on a particular malfunction.
    def repair(self, mal: Malfunctions):
        self.randomize_eff()
        self.status = Status.WORKING
        self.malfunction = mal

    # Method should be called when their assigned malfunction has been fixed.
    def stop_working(self):
        self.status = Status.IDLE
        self.malfunction = None

    def get_eff(self):
        return self.eff