import random
import malfunctions
"""
This is a class describing high voltage pole. 
It's used for simulating malfunctions on single pole and they are aggregated inside a Line class.
Objects of this class are supposed to be used only inside Line
"""
class Pole:
    def __init__(self, id:int):
        self.id = id
        self.status = "working"
        self.timeToRepair = 0
        self.malfunction = None

    def __str__(self):
        return str(self.id) + ": " + str(self.status)

    def get_status(self):
        return self.status

    def set_status(self, newStatus: str):
        self.status = newStatus
    """function uses predefined list of malfunctions and get
    a random one to happen on this pole. It changes its status accordingly
    to how serious the malfunction is"""
    def set_random_malfunction(self):
        malf = malfunctions.mal_list[random.randint(0,6)]
        self.malfunction = malf
        self.set_status(malf.get_status())
        self.timeToRepair = malf.get_time()

"""
A class describing high voltage line.
It agreggates posts and simulates series circuit: if one stops working every pole after that is disconnected.
"""

class Line:
    lineCount = 0 #static variable counting currently existing lines

    def __init__(self, poleCount:int):
        self.id = Line.lineCount
        Line.lineCount += 1
        self.polesList = list()
        self.status = "working"
        self.timeToRepair = 0
        self.malfunction = None
        self.workers = list()
        self.poleCount = poleCount
        for i in range(poleCount):
            self.polesList.append(Pole(i))

    def __len__(self):
        return self.polesList.__len__()

    def __str__(self):
        msg = "Line " + str(self.id) + ": " + self.status + "\n"
        for pole in self.polesList:
            msg += str(pole) + "\n"
        return msg

    def add_element(self):
        self.polesList.append(Pole(self.polesList.__len__()))

    def remove_element(self):
        self.polesList.pop(self.polesList.__len__()-1)


    def get_status(self):
        return self.status

    def set_status(self, newStatus: str):
        self.status = newStatus

    def get_pole_count(self):
        return self.poleCount

    def get_pole_list(self):
        msg = "Line " + str(self.id) + ": " + self.status + "\n"
        for pole in self.polesList:
            msg += str(pole) + "\n"
        return msg

    """
    Function checks line status and updates it if either it was working but malfunction ocurred or
    it wasnt working but is now repaired.
    Function checks for malfunction by checking status of every pole.
    If pole is broken it updates every pole connected to it (simulating serial circuit).
    Checking if line is fixed is analogical.
    """
    def update_line(self):
        if self.status == "working":
            disconnected = False
            for pole in self.polesList:
                if not disconnected:
                    if pole.get_status() != "working":
                        self.set_status(pole.get_status())
                        self.malfunction = pole.malfunction
                        disconnected = True
                else:
                    pole.set_status("disconnected")

        elif self.status == "work_in_progress":
            fixed = True
            for pole in self.polesList:
                if pole.get_status != "working":
                    fixed = False
                    break
            if fixed:
                self.set_status("working")

    #sets all posts to working status
    def fix_line(self, deltaTime):
        self.timeToRepair -= deltaTime
        if(self.timeToRepair <= 0):
            for pole in self.polesList:
                pole.set_status("working")
            self.set_status("working")
        else:
            self.set_status("work_in_progress")

    #rolls for malfunction on every post if line is currently working properly
    def simulate_malfunction(self):
        for pole in self.polesList:
            roll = random.randint(0, 100)
            if roll < 5:
                pole.set_random_malfunction()
                self.timeToRepair = pole.timeToRepair
                break