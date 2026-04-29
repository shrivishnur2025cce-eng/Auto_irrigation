import time
import random
from datetime import datetime


class IrrigationSystem:
    def __init__(self, dry_threshold=30, wet_threshold=70):
        self.dry_threshold = dry_threshold
        self.wet_threshold = wet_threshold
        self.pump_status = "OFF"

    def read_moisture(self):
        """Simulate soil moisture sensor (0–100%)"""
        return random.randint(0, 100)

    def control_pump(self, moisture):
        """Decide pump status based on moisture"""
        if moisture < self.dry_threshold:
            self.pump_status = "ON"
            return " Dry soil → Pump ON"
        elif moisture > self.wet_threshold:
            self.pump_status = "OFF"
            return " Soil too wet → Pump OFF"
        else:
            self.pump_status = "OFF"
            return " Soil OK → Pump OFF"

    def log_data(self, moisture):
        """Save data to file"""
        with open("irrigation_log.txt", "a") as file:
            file.write(f"{datetime.now()} | Moisture: {moisture}% | Pump: {self.pump_status}\n")

    def run(self):
        """Main loop"""
        print(" Automatic Irrigation System Started\n")
        try:
            while True:
                moisture = self.read_moisture()
                status = self.control_pump(moisture)

                print(f"Moisture: {moisture}%")
                print(status)
                print("-" * 40)

                self.log_data(moisture)

                time.sleep(2)

        except KeyboardInterrupt:
            print("\nSystem Stopped.")


if __name__ == "__main__":
    system = IrrigationSystem()
    system.run()