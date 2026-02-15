import time
import random

def detect_vehicle_density():
    """
    Simulates vehicle detection using random numbers.
    Returns number of vehicles detected.
    """
    vehicles = random.randint(0, 50)
    print(f"\nDetected Vehicles: {vehicles}")
    return vehicles

def calculate_green_time(vehicle_count):
    """
    AI Logic:
    More vehicles = longer green signal
    """
    if vehicle_count < 10:
        return 10
    elif vehicle_count < 25:
        return 20
    else:
        return 30

def traffic_signal():
    while True:
        vehicles = detect_vehicle_density()
        green_time = calculate_green_time(vehicles)

        print("\n🔴 RED Light ON")
        time.sleep(5)

        print("🟡 YELLOW Light ON")
        time.sleep(2)

        print(f"🟢 GREEN Light ON for {green_time} seconds")
        time.sleep(green_time)

        print("\nCycle Complete 🚦")
        print("-" * 40)

if __name__ == "__main__":
    traffic_signal()
