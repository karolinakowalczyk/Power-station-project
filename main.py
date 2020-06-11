from PowerPlant import PowerPlant

pp = PowerPlant()
pp.generateLines(2,20)
pp.generateWorkers(10)

pp.runSimulation(10, 10*24*60)