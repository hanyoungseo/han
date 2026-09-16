from collections import Counter
from datetime import datetime
import random


LOG_LEVELS = [
    "INFO",
    "INFO",
    "INFO",
    "WARNING",
    "ERROR"
]

MESSAGES = {
    "INFO": [
        "User login success",
        "Database connection success",
        "Request processed",
        "Server started"
    ],
    "WARNING": [
        "High memory usage",
        "Slow database response",
        "CPU usage exceeded"
    ],
    "ERROR": [
        "Database connection failed",
        "Request timeout",
        "Internal server error"
    ]
}


def generate_logs(count=100):
    logs = []

    for _ in range(count):
        level = random.choice(LOG_LEVELS)
        message = random.choice(MESSAGES[level])

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        log = f"{timestamp} | {level} | {message}"
        logs.append(log)

    return logs


def save_logs(logs, filename="server.log"):
    with open(filename, "w", encoding="utf-8") as file:
        for log in logs:
            file.write(log + "\n")


def analyze_logs(filename):
    level_counter = Counter()
    error_messages = Counter()

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(" | ")

            if len(parts) != 3:
                continue

            timestamp, level, message = parts

            level_counter[level] += 1

            if level == "ERROR":
                error_messages[message] += 1

    return level_counter, error_messages


def print_report(levels, errors):
    print("===== Server Log Report =====")

    print("\nLog Level")
    for level, count in levels.items():
        print(f"{level:<10}: {count}")

    print("\nError Messages")
    for message, count in errors.most_common():
        print(f"{message}: {count}")


def main():
    logs = generate_logs(200)

    save_logs(logs)

    levels, errors = analyze_logs("server.log")

    print_report(levels, errors)


if __name__ == "__main__":
    main()
