import csv

from Line import Line
import random
from worker import Worker
from worker import Status


class PowerPlant:

    def __init__(self):
        self.lines = list()
        self.workers = list()
        self.pole_life_time = list()

    def generateLines(self, count: int, lineSize: int):
        for i in range(0, count):
            self.lines.append(Line(lineSize))

    def tableOfPoleTimes(self, dTime: int):
        #do it once in main, not one time each iteration
        #csvwriter.writerow([len(self.lines), self.lines[0].get_pole_count()])
        for i in range(0, len(self.lines)):
            for j in range(0, self.lines[i].get_pole_count()):
                if self.lines[i].polesList[j].get_status() == "working":
                    self.pole_life_time[i][j] = self.pole_life_time[i][j] + dTime
                else:
                    self.pole_life_time[i][j] = self.pole_life_time[i][j] + 0

    def generateWorkers(self, count: int):
        self.workers = []
        for i in range(0, count):
            self.workers.append(Worker(i, random.randint(80, 120), random.randint(20, 40)))

    def findIdleWorker(self):
        for w in self.workers:
            if w.status == Status.IDLE:
                return w
        return None

    def runSimulation(self, deltaTime: int, totalTime: int):
        currentTime = 0
        self.pole_life_time = [[0] * (self.lines[0].get_pole_count()) for i in range(len(self.lines))]
        while (currentTime <= totalTime):
            for line in self.lines:
                if (line.get_status() == "working"):
                    line.simulate_malfunction()
                else:
                    while len(line.workers) < len(self.workers) / len(self.lines):
                        worker = self.findIdleWorker()
                        if worker is not None:
                            line.workers.append(worker)
                            worker.repair(line.malfunction)
                    for worker in line.workers:
                        line.fix_line(deltaTime * worker.eff / 100)
                line.update_line()
                if line.get_status() == "working":
                    for worker in line.workers:
                        worker.stop_working()
                    line.workers.clear()
                """#Prints status of all lines every deltaTime
                print("TIME:" + str(currentTime) + " Id:" + str(line.id) + " status:" + str(line.get_status()))
                if (line.get_status() != "working"):
                    print("Remaining repair: " + str(line.timeToRepair) + "\ncurrently working on malfunction:" + str(
                        len(line.workers)))
                print(line)
                """
            currentTime += deltaTime
            self.tableOfPoleTimes(deltaTime)

        with open('poles_life_times.csv', 'a', encoding='utf-8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(self.pole_life_time)
