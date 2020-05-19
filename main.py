from PowerPlant import PowerPlant

pp = PowerPlant()
pp.generateLines(1,20)
pp.generateWorkers(10)

pp.runSimulation(10, 4400)
