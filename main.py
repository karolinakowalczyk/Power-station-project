from PowerPlant import PowerPlant

pp = PowerPlant()
pp.generateLines(1,20)
pp.runSimulation(10, 365*24*60)
