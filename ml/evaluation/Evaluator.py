from ml.evaluation.Measures import Measures


class Evaluator:

    def __init__(self, classifier):
        self.__classifier = classifier
        self.__measures = Measures()

    def setTrain(self, X_train, y_train):
        self.__X_train = X_train
        self.__y_train = y_train

    def setTest(self, X_test, y_test):
        self.__X_test = X_test
        self.__y_test = y_test

    def evaluate(self):
        i = 0
        for unlabeledInstance in self.__X_test:
            predicted = self.__classifier.predict(unlabeledInstance)

            if int(predicted[0]) == 0 and int(self.__y_test[i][0]) == 0:
                self.__measures.increaseTn()
            if int(predicted[0]) == 1 and int(self.__y_test[i][0]) == 1:
                self.__measures.increaseTp()
            if int(predicted[0]) == 0 and int(self.__y_test[i][0]) == 1:
                self.__measures.increaseFn()
            if int(predicted[0]) == 1 and int(self.__y_test[i][0]) == 0:
               self.__measures.increaseFp()

            i += 1

    def printFullEvaluations(self):
            print 'Precission: ' + str(self.__measures.precission())
            print 'Recall: ' + str(self.__measures.recall())
            print 'Accuracy: ' + str(self.__measures.accuracy())
            print 'f-Meassure: ' + str(self.__measures.fscore())
            print 'Confussion matrix: '
            print '       R    '
            print '     +    -  '
            print 'E + ' + str(self.__measures.tp()) + "|" + str(self.__measures.fp())
            print '  - ' + str(self.__measures.fn()) + "|" + str(self.__measures.tn())