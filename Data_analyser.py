import csv
import copy

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
        print(self.simulations[0][0][19])

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
                self.workersBefore.append(row)

        with open('workers_efficient_after.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                self.workersAfter.append(row)
        #if you want to see the data
        #print(self.workersBefore)
        #print(self.workersAfter)
