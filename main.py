from PowerPlant import PowerPlant
from Line import Line
import csv
from TestFunctions import TestFunctions

pp = PowerPlant()

pp.generateLines(3, 5)
pp.generateWorkers(3)

with open('workers_efficient_before.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(0, len(pp.workers)):
        csvwriter.writerow(str(pp.workers[i].get_eff()))

pp.runSimulation(20, 40)

with open('workers_efficient_after.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(0, len(pp.workers)):
        csvwriter.writerow(str(pp.workers[i].get_eff()))

