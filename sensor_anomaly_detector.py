import pandas as pd
import numpy as np


def generate_sensor_data(size=200):
    np.random.seed(42)

    data = {
        "temperature": np.random.normal(25, 2, size),
        "humidity": np.random.normal(65, 5, size),
        "co2": np.random.normal(700, 80, size)
    }

    df = pd.DataFrame(data)

    # 임의의 이상 데이터 생성
    df.loc[30, "temperature"] = 40
    df.loc[80, "humidity"] = 20
    df.loc[150, "co2"] = 1500

    return df


def detect_anomaly_zscore(df, threshold=3):
    result = df.copy()

    for column in df.columns:
        mean = df[column].mean()
        std = df[column].std()

        z_score = (df[column] - mean) / std

        result[f"{column}_zscore"] = z_score
        result[f"{column}_anomaly"] = abs(z_score) > threshold

    return result


def print_anomaly_summary(df):
    sensor_columns = ["temperature", "humidity", "co2"]

    print("===== Sensor Anomaly Summary =====")

    for sensor in sensor_columns:
        anomaly_column = f"{sensor}_anomaly"
        count = df[anomaly_column].sum()

        print(f"{sensor}: {count} anomaly detected")

        if count > 0:
            anomaly_data = df[df[anomaly_column]]
            print(anomaly_data[[sensor, f"{sensor}_zscore"]])
            print()


def main():
    sensor_data = generate_sensor_data()

    print("Original Sensor Data")
    print(sensor_data.head())

    analyzed_data = detect_anomaly_zscore(sensor_data)

    print_anomaly_summary(analyzed_data)

    analyzed_data.to_csv(
        "sensor_anomaly_result.csv",
        index=False
    )

    print("Result saved: sensor_anomaly_result.csv")


if __name__ == "__main__":
    main()
