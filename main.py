from PowerPlant import PowerPlant
import csv
from Data_analyser import Data_analyser

case = input("If you want to simulate enter 1, if you want to analyze data enter 2. \nIf you want to quit enter 0.\n")
# how many sims you want to run/import
sims = 20
lines = 2
poles = 20
case = int(case)
if case == 1:
    pp = PowerPlant()
    pp.generateLines(lines, poles)
    pp.generateWorkers(10)

    with open('workers_efficient_before.csv', 'w', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(0, len(pp.workers)):
            csvwriter.writerow([str(pp.workers[i].get_eff())])

    # printuje ### przed kazda symulacja
    for i in range(0, sims):
        with open('poles_life_times.csv', 'a', encoding='utf-8', newline='') as csvfile2:
            csvwriter = csv.writer(csvfile2)
            csvwriter.writerow(['###'])
        pp.runSimulation(10, 10 * 24 * 60)

    with open('workers_efficient_after.csv', 'w', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(0, len(pp.workers)):
            csvwriter.writerow([str(pp.workers[i].get_eff())])

elif case == 2:
    da = Data_analyser()
    da.load_lifetimes(sims, lines, poles)
    da.generate_lifetime_histogram(sims, 10)
    da.loadWorkers()
    da.generate_workers_comparison()
    da.generate_poles_life_expectancy(sims, poles)
    da.generate_poles_stdev(sims, poles)
    print("\nSredni czas zycia wszystkich slupkow: " + str(da.total_avg(sims, poles)) + " s")
elif case == 0:
    SystemExit
