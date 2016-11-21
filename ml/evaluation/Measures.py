class Measures:

    def __init__(self):
        self.__tp = 0.0
        self.__tn = 0.0
        self.__fp = 0.0
        self.__fn = 0.0

    def increaseTp(self):
        self.__tp += 1.0

    def increaseTn(self):
        self.__tn += 1.0

    def increaseFp(self):
        self.__fp += 1.0

    def increaseFn(self):
        self.__fn += 1.0

    def tp(self):
        return int(self.__tp)

    def fn(self):
        return int(self.__fn)

    def fp(self):
        return int(self.__fp)

    def tn(self):
        return int(self.__tn)

    def precission(self):
        if self.__tp + self.__fp == 0 : return 'N/A'

        return self.__tp / (self.__tp + self.__fp)

    def recall(self):
        if self.__tp + self.__fn == 0 : return 'N/A'
        return self.__tp / (self.__tp + self.__fn)

    def accuracy(self):
        return (self.__tp + self.__tn) / (self.__tp + self.__tn + self.__fp + self.__fn)

    def fscore(self):
        if self.precission() == 'N/A' or self.recall() == 'N/A' : return 'N/A'
        return (2 * self.precission() * self.recall()) / (self.precission() + self.recall())