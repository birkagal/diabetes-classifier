import pickle

import sklearn.linear_model
import sklearn.neural_network
import sklearn.tree


# Load model from picke file
mlpc: sklearn.neural_network.MLPClassifier = pickle.load(open("./src/classifiers/mlpc.pickle", "rb"))
ptc: sklearn.linear_model.Perceptron = pickle.load(open("./src/classifiers/ptc.pickle", "rb"))
dtc: sklearn.tree.DecisionTreeClassifier = pickle.load(open("./src/classifiers/dtc.pickle", "rb"))


def classify(data):
    predict = [[]]

    # Set predict list using given data
    for key in data:
        if key == "age":
            predict[0].append(int(data[key]) / 100)
        elif key == "gender":
            if data[key] == "male":
                predict[0].append(1)
            else:
                predict[0].append(0)
        else:
            if data[key] == "yes":
                predict[0].append(1)
            else:
                predict[0].append(0)

    # Apply the model to the predict data
    result = [
        list(ptc.predict(predict)),
        list(mlpc.predict(predict)),
        list(dtc.predict(predict)),
    ]
    if [0] in result:
        return False
    else:
        return True
