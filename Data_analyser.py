import csv
import copy
import matplotlib.pyplot as plt
import numpy as np
import statistics as sts

class Data_analyser:

    def __init__(self):
        self.simulations = list()
        self.workersBefore = list()
        self.workersAfter = list()
        # self.

    def load_lifetimes(self, simulations_count: int):
        # initiates lists on which time will be loaded


        # open files and initiate counters
        with open("poles_life_times.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = next(csv_reader)
            lines_count = int(header[0])
            poles = int(header[1])
            #print(lines_count, poles)
            lines = list()
            for i in range(0, lines_count):
                posts = list()
                for j in range(0, poles):
                    posts.append(0)
                lines.append(posts)
            for i in range(0, simulations_count):
                # deepcopy to avoid issues with referencing same list
                self.simulations.append(copy.deepcopy(lines))
            current_line = 0
            current_sim = 0
            current_pole = 0
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                for i in range(len(row)):
                    self.simulations[current_sim][current_line][i] = int(row[i])
                    if current_pole == poles-1:
                        current_pole = 0
                        current_line += 1
                        if current_line == lines_count:
                            current_line = 0
                            current_sim += 1
                    else:
                        current_pole += 1
                if current_sim == simulations_count:
                    break

            print(self.simulations)


        # loads info about worker efficiency before and after last simulation

    def loadWorkers(self):
        with open('workers_efficient_before.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                self.workersBefore.append(int(row[0]))

        with open('workers_efficient_after.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                self.workersAfter.append(int(row[0]))
        # if you want to see the data
        # print(self.workersBefore)
        # print(self.workersAfter)

    def generate_lifetime_histogram(self, simulations: int, pole: int):
        # validate data, if given value is too big, take max value instead
        if len(self.simulations) < simulations:
            simulations = len(self.simulations) - 1
        if pole > len(self.simulations[0][0]):
            pole = len(self.simulations[0][0]) - 1


        # lifetimes of given pole in n simulations
        y = [self.simulations[i][0][pole] for i in range(0, simulations)]

        n, bins, patches = plt.hist(y, 50, orientation='horizontal')
        plt.axis((0, max(n)+1, min(y), max(y)))
        x = np.arange(max(n)+1)
        #plt.xticks(x)
        #bins_labels = [str(bins[i]) + '-' + str(bins[i+1]) for i in range(len(bins)-1)]
        #plt.yticks(bins)
        plt.xlabel('Wystapienia wynikow')
        plt.ylabel('Czas dzialania [min]')
        plt.title('Histogram zycia slupka '+str(pole)+' w '+str(simulations)+' symulacjach')
        #plt.grid(True)
        #TODO: moze jednak przedzialy?
        #plt.yticks(bins, bins_labels)
        plt.show()


    def generate_workers_comparison(self):

        labels = [i for i in range(1, len(self.workersBefore) + 1)]
        x = np.arange(len(labels))
        yMax = max(max(self.workersBefore), max(self.workersAfter))
        width = 0.35

        # placing labels on x axis
        plt.xticks(x + width, labels)
        # fix: chart didnt fit
        correction = 0.2
        # placing bars
        print(len(x), len(self.workersAfter), len(self.workersBefore))
        plt.bar(x + correction, self.workersBefore, width, label='Efektywnosc przed symulacjami')
        plt.bar(x + width + correction, self.workersAfter, width, label='Efektywnosc po symulacjach')
        # metadata
        plt.legend()
        plt.title("Porownanie efektywnosci pracownikow")
        plt.xlabel("Nr pracownika")
        plt.ylabel("Efektywnosc pracownika [%]")
        plt.axis([0, len(self.workersAfter), 0, yMax * 1.25])
        plt.show()

    def stdev_pole(self, simulations: int, poles_per_line: int, pole):
        # validate data, if given value is too big, take max value instead
        if len(self.simulations) < simulations:
            simulations = len(self.simulations) - 1
        if pole > poles_per_line:
            pole = poles_per_line - 1
        # TODO: pomijamy wyniki z drugiej linii?
        # lifetimes of given pole in n simulations
        y = [self.simulations[i][0][pole] for i in range(0, simulations)]
        y_stdev = sts.stdev(y)
        return y_stdev

    def generate_poles_stdev(self, simulations: int, poles_per_line: int):

        y = [self.stdev_pole(simulations, poles_per_line, i) for i in range(0, poles_per_line)]

        # labels - nr of pole
        x_labels = range(1, poles_per_line + 1)
        # converting to numpy array
        x = np.arange(len(x_labels))
        # each x tick is labeled
        correction = 0.5
        plt.xticks(x + correction, x_labels)

        # making bar chart with x from 0 to poles_per_line and y from 0 to yMax*1.25
        plt.bar(x + correction, y)
        plt.axis([0, poles_per_line, 0, 1.25 * max(y)])

        # metadata
        plt.legend()
        plt.title("Odchylenie standardowe zycia slupkow dla " + str(simulations) + " symulacji")
        plt.xlabel("Nr slupka")
        plt.ylabel("ODchylenie standardowe")
        plt.axis([0, poles_per_line, 0, max(y) * 1.25])
        plt.show()

    def avg_life_expectancy(self, simulations: int, poles_per_line: int, pole: int):
        # validate data, if given value is too big, take max value instead
        if len(self.simulations) < simulations:
            simulations = len(self.simulations) - 1
        if pole > poles_per_line:
            pole = poles_per_line - 1
        # TODO: pomijamy wyniki z drugiej linii?
        # lifetimes of given pole in n simulations
        y = [self.simulations[i][0][pole] for i in range(0, simulations)]
        y_avg = np.average(y)
        return y_avg

    def total_avg(self, simulations: int, poles_per_line: int):
        y = [self.avg_life_expectancy(simulations, poles_per_line, i) for i in range(0, poles_per_line)]
        return np.average(y)

    def generate_poles_life_expectancy(self, simulations: int, poles_per_line: int):

        # highly advanced two-dimensional array with nested loops which probably doesn't work

        y = [self.avg_life_expectancy(simulations, poles_per_line, i) for i in range(0, poles_per_line)]

        # labels - nr of pole
        x_labels = range(1, poles_per_line + 1)
        # converting to numpy array
        x = np.arange(len(x_labels))
        # each x tick is labeled
        correction = 0.5
        plt.xticks(x + correction, x_labels)

        # making bar chart with x from 0 to poles_per_line and y from 0 to yMax*1.25
        plt.bar(x + correction, y, label='Czas dzialania')
        plt.axis([0, poles_per_line, 0, 1.25 * max(y)])

        # metadata
        plt.legend()
        plt.title("Dlugosc zycia slupkow dla " + str(simulations) + " symulacji")
        plt.xlabel("Nr slupka")
        plt.ylabel("Sredni czas zycia [s]")
        plt.axis([0, poles_per_line, 0, max(y) * 1.25])
        plt.show()
