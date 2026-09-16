import random
import time


class SmartFarmController:

    def __init__(self):
        self.pump_status = False

        self.min_moisture = 35
        self.max_moisture = 65

        self.min_temperature = 18
        self.max_temperature = 32

    def read_soil_moisture(self):
        return round(
            random.uniform(20, 80),
            2
        )

    def read_temperature(self):
        return round(
            random.uniform(15, 38),
            2
        )

    def read_humidity(self):
        return round(
            random.uniform(40, 90),
            2
        )

    def turn_on_pump(self):
        if not self.pump_status:
            self.pump_status = True
            print("Water pump ON")

    def turn_off_pump(self):
        if self.pump_status:
            self.pump_status = False
            print("Water pump OFF")

    def control_irrigation(self, moisture):
        if moisture < self.min_moisture:
            self.turn_on_pump()

        elif moisture > self.max_moisture:
            self.turn_off_pump()

    def check_environment(
        self,
        temperature,
        humidity,
        moisture
    ):
        print("-" * 40)
        print(f"Temperature    : {temperature} C")
        print(f"Humidity       : {humidity} %")
        print(f"Soil Moisture  : {moisture} %")

        if temperature > self.max_temperature:
            print("WARNING: High temperature")

        elif temperature < self.min_temperature:
            print("WARNING: Low temperature")

        self.control_irrigation(moisture)

        pump = "ON" if self.pump_status else "OFF"

        print(f"Pump Status    : {pump}")

    def run(self, cycles=10):
        print("Smart Farm Monitoring System Started")

        for index in range(cycles):
            print(f"\nMonitoring cycle #{index + 1}")

            temperature = self.read_temperature()
            humidity = self.read_humidity()
            moisture = self.read_soil_moisture()

            self.check_environment(
                temperature,
                humidity,
                moisture
            )

            time.sleep(1)


def main():
    controller = SmartFarmController()

    controller.run(
        cycles=10
    )


if __name__ == "__main__":
    main()
