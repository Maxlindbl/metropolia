class Car:
    def __init__(self, license_plate, max_speed, speed, distance):
        self.license_plate = license_plate
        self.max_speed = max_speed
        self.speed = speed
        self.distance = distance

    def Accelerate(self,speed_up):
        self.speed = self.speed + speed_up
        if self.speed >= self.max_speed:
            self.speed = self.max_speed
        if self.speed <= 0:
            self.speed = 0
        print(f"auton nopeus on {self.speed}km/h")
        return


new_car = Car("abc-123", 142, 0, 0)
new_car.Accelerate(+ 30)
new_car.Accelerate(+ 70)
new_car.Accelerate(+ 50)
new_car.Accelerate(- 200)

print(f"auton rekkari on {new_car.license_plate:s} ja maksimi nopeus {new_car.max_speed:d}")