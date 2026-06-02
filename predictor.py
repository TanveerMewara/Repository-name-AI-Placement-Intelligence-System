# import pandas as pd

# from sklearn.model_selection import train_test_split

# from sklearn.ensemble import RandomForestClassifier

# from sklearn.metrics import accuracy_score

# df = pd.read_csv("data/placement_data.csv")

# X = df.drop("Placed", axis=1)

# y = df["Placed"]

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# model = RandomForestClassifier()

# model.fit(X_train, y_train)

# predictions = model.predict(X_test)

# accuracy = accuracy_score(y_test, predictions)

# print(f"Accuracy: {accuracy:.2f}")

# student = [[8.5, 80, 78, 82, 1]]

# prediction = model.predict(student)

# if prediction[0] == 1:
#     print("Likely to be Placed")
# else:
#     print("Placement Risk")

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_model():

    df = pd.read_csv("data/placement_data.csv")

    X = df.drop("Placed", axis=1)
    y = df["Placed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    return model, accuracy


def predict_student(
    cgpa,
    dsa,
    aptitude,
    communication,
    internship
):

    model, accuracy = train_model()

    student = [[
        cgpa,
        dsa,
        aptitude,
        communication,
        internship
    ]]

    prediction = model.predict(student)

    return prediction[0], accuracy