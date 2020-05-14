from Line import Line
import malfunctions
import random

class PowerPlant:
    def __init__(self):
        self.lines = list()
        self.balance = 5000

    def generateLines(self, count: int, lineSize: int):
        for i in range(0, count):
            self.lines.append(Line(lineSize))


    def runSimulation(self, deltaTime: int, totalTime: int):
        currentTime = 0
        while(currentTime < totalTime):
            for line in self.lines:
                if(line.get_status() == "working"):
                    line.simulate_malfunction()
                else:
                    line.fix_line(deltaTime)
                line.update_line()
                print("TIME:" + str(currentTime) + " Id:"+ str(line.id) + " status:" + str(line.get_status()))
                if(line.get_status() != "working"):
                    print("Remaining repair: " + str(line.timeToRepair))
                print(line)
            currentTime += deltaTime