from sklearn.neighbors import KNeighborsClassifier
import numpy as py


def main():
    train = py.loadtxt('/home/ekaitz/Escritorio/ml/diabetes_train.csv', delimiter=',', skiprows=1)
    test = py.loadtxt('/home/ekaitz/Escritorio/ml/diabetes_test.csv', delimiter=',', skiprows=1)

    X_train = train[:, :-1]
    y_train = train[:, -1:]

    X_test = test[:, :-1]
    y_test = test[:, -1:]

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    i=0
    for unlabeledInstance in X_test:
        predicted = knn.predict(unlabeledInstance)
        print 'Predicted: ' + str(predicted) + ', Real: ' + str(y_test[i])
        i+=1


if __name__ == "__main__":
    main()