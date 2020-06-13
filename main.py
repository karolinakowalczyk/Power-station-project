from PowerPlant import PowerPlant
from Line import Line
import csv
from TestFunctions import TestFunctions

pp = PowerPlant()

pp.generateLines(2, 20)
pp.generateWorkers(10)

with open('workers_efficient_before.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(0, len(pp.workers)):
        csvwriter.writerow(str(pp.workers[i].get_eff()))

pp.runSimulation(10, 10*24*60)

with open('workers_efficient_after.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(0, len(pp.workers)):
        csvwriter.writerow(str(pp.workers[i].get_eff()))

