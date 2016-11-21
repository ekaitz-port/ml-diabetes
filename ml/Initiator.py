from sklearn.neighbors import KNeighborsClassifier
import numpy as py
import warnings

from ml.evaluation.Evaluator import Evaluator


def main():
    warnings.filterwarnings('ignore')

    train = py.genfromtxt('/home/eka/projects/ml-diabetes/diabetes.csv', delimiter=',', dtype='str')
    test = py.genfromtxt('/home/eka/projects/ml-diabetes/diabetes.csv', delimiter=',', dtype='str')

    X_train = train[1:, :-1] #attrs of all instances
    y_train = train[1:, -1:] #classes of all instances

    X_test = test[1:, :-1]
    y_test = test[1:, -1:]

    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(X_train, y_train)

    evaluator = Evaluator(classifier)
    evaluator.setTrain(X_train, y_train)
    evaluator.setTest(X_test, y_test)

    evaluator.evaluate()

    evaluator.printFullEvaluations()


if __name__ == "__main__":
    main()