from PowerPlant import PowerPlant
import csv
from Data_analyser import Data_analyser

case = input("If you want to simulate enter 1, if you want to analyze data enter 2. \nIf you want to quit enter 0.\n")
# how many sims you want to run/import
sims = 5000
lines = 2
poles = 20
case = int(case)
if case == 1:
    pp = PowerPlant()
    pp.generateLines(lines, poles)

    #prints line count and poles per line to file
    with open('poles_life_times.csv', 'a', encoding='utf-8', newline='') as csvfile2:
        csvwriter = csv.writer(csvfile2)
        csvwriter.writerow([lines, poles])
    #runs the simulation in a loop
    for i in range(0, sims):
        pp.generateWorkers(10)
        #saves workers efficiency before a particular simulation to compare it with efficiency after
        if (i == 9):
            with open('workers_efficient_before.csv', 'w', encoding='utf-8', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                for j in range(0, len(pp.workers)):
                    csvwriter.writerow([str(pp.workers[j].get_eff())])
        pp.runSimulation(10, 10 * 24 * 60)
        #saves workers efficiency after a particular simulation
        if (i == 9):
            with open('workers_efficient_after.csv', 'w', encoding='utf-8', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                for j in range(0, len(pp.workers)):
                    csvwriter.writerow([str(pp.workers[j].get_eff())])

elif case == 2:
    da = Data_analyser()
    da.load_lifetimes(sims)
    da.loadWorkers()
    da.generate_five_point(sims, 7)
    da.generate_boxplot(sims, 7)
    da.generate_lifetime_histogram(sims, 7)
    da.generate_workers_comparison()
    da.generate_poles_life_expectancy(sims, poles)
    da.generate_poles_stdev(sims, poles)
    print("\nSredni czas zycia wszystkich slupkow: " + str(da.total_avg(sims, poles)) + " s")

elif case == 0:
    SystemExit