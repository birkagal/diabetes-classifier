import pickle
import json

# Load model from picke file
mlpc = pickle.load(open("./src/classifiers/mlpc.pickle", "rb"))
ptc = pickle.load(open("./src/classifiers/ptc.pickle", "rb"))


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
    result = []
    result.append(list(ptc.predict(predict)))
    result.append(list(mlpc.predict(predict)))
    if [0] in result:
        return False
    else:
        return True