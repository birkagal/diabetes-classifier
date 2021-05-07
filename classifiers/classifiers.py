from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
)
import pickle

## Importing the dataset
dataset = read_csv("./data.csv")

## Data Preprocessin
# Normalizing the Age
dataset["Age"] = [age / 100 for age in dataset["Age"]]

# Transforming text values into numeric values
dataset["Gender"] = dataset["Gender"].map({"Male": 1, "Female": 0})
dataset["Class"] = dataset["Class"].map({"Positive": 1, "Negative": 0})
dataset["Polyuria"] = dataset["Polyuria"].map({"Yes": 1, "No": 0})
dataset["Polydipsia"] = dataset["Polydipsia"].map({"Yes": 1, "No": 0})
dataset["Sudden Weight Loss"] = dataset["Sudden Weight Loss"].map({"Yes": 1, "No": 0})
dataset["Weakness"] = dataset["Weakness"].map({"Yes": 1, "No": 0})
dataset["Polyphagia"] = dataset["Polyphagia"].map({"Yes": 1, "No": 0})
dataset["Genital Thrush"] = dataset["Genital Thrush"].map({"Yes": 1, "No": 0})
dataset["Visual Blurring"] = dataset["Visual Blurring"].map({"Yes": 1, "No": 0})
dataset["Itching"] = dataset["Itching"].map({"Yes": 1, "No": 0})
dataset["Irritability"] = dataset["Irritability"].map({"Yes": 1, "No": 0})
dataset["Delayed Healing"] = dataset["Delayed Healing"].map({"Yes": 1, "No": 0})
dataset["Partial Paresis"] = dataset["Partial Paresis"].map({"Yes": 1, "No": 0})
dataset["Muscle Stiffness"] = dataset["Muscle Stiffness"].map({"Yes": 1, "No": 0})
dataset["Alopecia"] = dataset["Alopecia"].map({"Yes": 1, "No": 0})
dataset["Obesity"] = dataset["Obesity"].map({"Yes": 1, "No": 0})

# Splitting dataset into Test set and Train set
X = dataset[list(dataset.columns)[1:]]  # Taking all columns EXCEPT "class"
y = dataset["Class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# Check for overfitting in the model
print("\nChecking for overfitting:\n")
for i in range(9):
    dtc = DecisionTreeClassifier(max_depth=i + 1, criterion="gini", random_state=0)
    dtc.fit(X_train, y_train)
    y_pred = dtc.predict(X_test)
    print(
        f"depth={i+1} \t train acc={dtc.score(X_train, y_train):.10f} \t test acc={dtc.score(X_test, y_test)}"
    )

## DECISION TREE CLASSIFIER
dtc = DecisionTreeClassifier(max_depth=7, criterion="gini", random_state=0)

# Feeding model with training data
dtc.fit(X_train, y_train)

# Give data test set and predict result
y_pred = dtc.predict(X_test)

# Model results
print("\nModel Results:\n")
# Calculate model accuracies
print(f"Training accuracy = {dtc.score(X_train,y_train)}")
print(f"Testing accuracy = {dtc.score(X_test,y_test)}")

# Calculate confusion matrix
print(f"Confusion matrix =\n{confusion_matrix(y_test, y_pred)}")

# Classification report
print(f"final report =\n{classification_report(y_pred, y_test)}")


## Percpetron Classifier
ptc = Perceptron(random_state=0)

# Feeding model with training data
ptc.fit(X_train, y_train)

# Give data test set and predict result
y_pred = ptc.predict(X_test)

# Model results
print("\nModel Results:\n")
# Calculate model accuracies
print(f"Training accuracy = {ptc.score(X_train,y_train)}")
print(f"Testing accuracy = {ptc.score(X_test,y_test)}")

# Calculate confusion matrix
print(f"Confusion matrix =\n{confusion_matrix(y_test, y_pred)}")

# Classification report
print(f"final report =\n{classification_report(y_pred, y_test)}")

## MLP Classifier
mlpc = MLPClassifier(random_state=0, max_iter=300)

# Feeding model with training data
mlpc.fit(X_train, y_train)

# Give data test set and predict result
y_pred = mlpc.predict(X_test)

# Model results
print("\nModel Results:\n")
# Calculate model accuracies
print(f"Training accuracy = {mlpc.score(X_train,y_train)}")
print(f"Testing accuracy = {mlpc.score(X_test,y_test)}")

# Calculate confusion matrix
print(f"Confusion matrix =\n{confusion_matrix(y_test, y_pred)}")

# Classification report
print(f"final report =\n{classification_report(y_pred, y_test)}")

classifiers = [mlpc, dtc, ptc]

# MLP Classifier has the best result, pickle it to be used in https://diabetesclassifier.herokuapp.com/
pickle.dump(mlpc, open("mlpc.pickle", 'wb'))