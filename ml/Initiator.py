from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC

import numpy as py
import warnings

from ml.evaluation.Evaluator import Evaluator


def main():
    warnings.filterwarnings('ignore')

    train = py.genfromtxt('/home/ekaitz/Escritorio/ml/diabetes_train.csv', delimiter=',', dtype='str')
    test = py.genfromtxt('/home/ekaitz/Escritorio/ml/diabetes_test.csv', delimiter=',', dtype='str')

    X_train = train[1:, :-1] #attrs of all instances
    y_train = train[1:, -1:] #classes of all instances

    X_test = test[1:, :-1]
    y_test = test[1:, -1:]

    #classifier = KNeighborsClassifier(n_neighbors=3)

    #classifier = SVC(C=0.001, degree=2, kernel='poly')
    #classifier.fit(X_train, y_train)

    cParam = 0.0001
    bestCParam = cParam
    #degreeParam = 2

    maxFScore = 0.0
    for i in range(10):
        #for j in range(2):
        classifier = LinearSVC(C=cParam)
        classifier.fit(X_train, y_train)

        evaluator = Evaluator(classifier)
        evaluator.setTrain(X_train, y_train)
        evaluator.setTest(X_test, y_test)

        evaluator.evaluate()

        print 'C: ' + str(cParam)
        #print 'Degree: ' + str(degreeParam)
        evaluator.printFullEvaluations()
        if(evaluator.fMeassure() > maxFScore and evaluator.fMeassure() != 'N/A'):
            maxFScore = evaluator.fMeassure()
            bestCParam = cParam

        #degreeParam += 1
        cParam *= 10
        #degreeParam = 1

    print 'best C param: ' + str(bestCParam)

if __name__ == "__main__":
    main()