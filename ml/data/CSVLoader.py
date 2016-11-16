import numpy as py

class CSVLoader:

    def __init__(self, file):
        self.__file = file

    def loadInstances(self):
        instancesWithLabels = py.loadtxt(file, delimiter=',')
        labels = instancesWithLabels[:1,:]