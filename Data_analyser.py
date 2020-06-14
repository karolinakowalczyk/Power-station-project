import csv
import copy
import matplotlib.pyplot as plt
import numpy as np

class Data_analyser:

    def __init__(self):
        self.simulations = list()
        self.workersBefore = list()
        self.workersAfter = list()

    def load_lifetimes(self, simulations_count:int, lines_count:int, poles:int):
        #initiates lists on which time will be loaded

        lines = list()
        for i in range(0,lines_count):
            posts = list()
            for j in range(0,poles):
                posts.append(0)
            lines.append(posts)
        for i in range(0, simulations_count):
            #deepcopy to avoid issues with refferencing same list
            self.simulations.append(copy.deepcopy(lines))

        #open files and initiate counters
        with open("poles_life_times.csv") as csv_file:    
            csv_reader = csv.reader(csv_file, delimiter=',')
            current_sim = -1
            current_line = 0
            current_post = 0
            for row in csv_reader:
                #check if new simulation
                if row == ['###']:
                    current_sim +=1
                    if current_sim == simulations_count:
                        break
                #check if new Line
                elif row[0] == 'Linia':
                    current_line = int(row[1])
                    current_post = 0
                else:
                #update [sim][line][pole]
                    #print("sim:", current_sim, "current post: ",current_post, "value: ", int(row[0]))
                    self.simulations[current_sim][current_line][current_post] = int(row[0])
                    current_post += 1
            #if you want to see the data from n-th simulation print simulations[n]
            #print(self.simulations[0])

        #loads info about worker efficiency before and after last simulation
    def loadWorkers(self):
        with open('workers_efficient_before.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter =',')
            for row in csv_reader:
                self.workersBefore.append(int(row[0]))

        with open('workers_efficient_after.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                self.workersAfter.append(int(row[0]))
        #if you want to see the data
        #print(self.workersBefore)
        #print(self.workersAfter)


    def generate_lifetime_histogram(self, simulations:int, pole:int):
        #validate data, if given value is too big, take max value instead
        if len(self.simulations) < simulations:
            simulations = len(self.simulations)-1
        if pole > len(self.simulations[0]):
            pole = len(self.simulations[0][0])-1

        #labels - nr of simulation
        x_labels = range(1,simulations+1)
        #converting to numpy array
        x = np.arange(len(x_labels))
        #each x tick is labeled
        correction = 0.5
        plt.xticks(x+correction, x_labels)
        #lifetimes of given pole in n simulations
        y = [self.simulations[i][0][pole] for i in range(0,simulations)]
        yMax = max(y)
        #making bar chart with x from 0 to simulations and y from 0 to yMax*1.25
        plt.bar(x+correction, y, label='Czas dzialania')
        plt.axis([0, simulations, 0, yMax*1.25])
        #metadata
        plt.xlabel('Nr proby')
        plt.ylabel('Czas dzialania slupka')
        title = 'Czas życia słupka nr ' + str(pole) + ' w ' + str(simulations) + ' probach [min]'
        plt.title(title)
        plt.show()

    def generate_workers_comparison(self):

        labels = [i for i in range(1, len(self.workersBefore)+1)]
        x = np.arange(len(labels))
        yMax = max(max(self.workersBefore), max(self.workersAfter))
        width = 0.35

        #placing labels on x axis
        plt.xticks(x + width, labels)
        #fix: chart didnt fit
        correction = 0.2
        #placing bars
        plt.bar(x+correction, self.workersBefore, width, label='Efektywnosc przed symulacjami')
        plt.bar(x+width+correction, self.workersAfter, width, label='Efektywnosc po symulacjach')
        #metadata
        plt.legend()
        plt.title("Porownanie efektywnosci pracownikow")
        plt.xlabel("Nr pracownika")
        plt.ylabel("Efektywnosc pracownika [%]")
        plt.axis([0, len(self.workersAfter), 0, yMax*1.25])
        plt.show()