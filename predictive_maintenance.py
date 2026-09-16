import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


def generate_machine_data(size=1000):
    np.random.seed(42)

    temperature = np.random.normal(
        70,
        10,
        size
    )

    vibration = np.random.normal(
        3,
        1,
        size
    )

    operating_hours = np.random.randint(
        100,
        10000,
        size
    )

    pressure = np.random.normal(
        100,
        15,
        size
    )

    failure = (
        (temperature > 85)
        | (vibration > 4.5)
        | (pressure > 125)
    ).astype(int)

    return pd.DataFrame({
        "temperature": temperature,
        "vibration": vibration,
        "operating_hours": operating_hours,
        "pressure": pressure,
        "failure": failure
    })


def train_model(df):
    features = [
        "temperature",
        "vibration",
        "operating_hours",
        "pressure"
    ]

    X = df[features]
    y = df["failure"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=6,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    prediction = model.predict(X_test)

    print(
        "Accuracy:",
        round(
            accuracy_score(y_test, prediction),
            4
        )
    )

    print("\nClassification Report")
    print(
        classification_report(
            y_test,
            prediction
        )
    )

    return model


def predict_machine(model):
    machine = pd.DataFrame({
        "temperature": [91],
        "vibration": [5.2],
        "operating_hours": [7500],
        "pressure": [118]
    })

    result = model.predict(machine)[0]

    probability = model.predict_proba(machine)[0][1]

    print("===== New Machine Prediction =====")
    print(machine)

    print(
        "Failure Prediction:",
        "Danger" if result == 1 else "Normal"
    )

    print(
        f"Failure Probability: {probability:.2%}"
    )


def main():
    dataset = generate_machine_data()

    print("Dataset size:", dataset.shape)

    model = train_model(dataset)

    predict_machine(model)


if __name__ == "__main__":
    main()
