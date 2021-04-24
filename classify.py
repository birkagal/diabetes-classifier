import pickle
import json
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier

classifiers = []

with open('classifiers.pickle', 'rb') as f:
    classifiers = pickle.load(f)

def classify(data):
    predict = [[]]
    for key in data:
        if key == 'age':
            predict[0].append(int(data[key])/100)
        elif key == 'gender':
            if data[key] == 'male':
                predict[0].append(1)
            else:
                predict[0].append(0)
        else:
            if data[key] == 'yes':
                predict[0].append(1)
            else:
                predict[0].append(0)

    mlpc = classifiers[0]
    result = mlpc.predict(predict)
    if result == [0]:
        return False
    else:
        return True