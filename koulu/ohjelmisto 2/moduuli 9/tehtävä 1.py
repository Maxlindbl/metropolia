class Car:
    def __init__(self, license_plate, max_speed, speed, distance):
        self.license_plate = license_plate
        self.max_speed = max_speed
        self.speed = speed
        self.distance = distance


new_car = Car("abc-123", 142, 0, 0)

print(f"auton rekkari on {new_car.license_plate:s} ja maksimi nopeus {new_car.max_speed:d}")