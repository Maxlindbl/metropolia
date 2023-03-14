import random
class Racecar:
    def __init__(self, license_plate, max_speed, speed, distance):
        self.license_plate = license_plate
        self.max_speed = max_speed
        self.speed = speed
        self.distance = distance

    def Accelerate(self, speed_up):
        self.speed = self.speed + speed_up
        # asetetaan raja-arvot  nopeudelle
        if self.speed >= self.max_speed:
            self.speed = self.max_speed
        if self.speed <= 0:
            self.speed = 0
        #print(f"auton nopeus on {self.speed}km/h {self.license_plate}")
        return

    def Moving(self, time):
        # lasketaan kuljettu matka
        self.distance = self.speed * time + self.distance
        #print(f"auton kulkema matka {self.distance}km")
        return


class Electric_car(Racecar):
    def __init__(self, license_plate, max_speed, battery_size, speed, distance):
        super().__init__(license_plate, max_speed, speed, distance)
        self.battery_size = battery_size

class Gas_car(Racecar):
    def __init__(self, license_plate, max_speed, gas_tank, speed, distance):
        super().__init__(license_plate, max_speed, speed, distance)
        self.gas_tank = gas_tank

gas_car = Gas_car("ABC-15", 180, 32.2, 70, 0)
electric_car = Electric_car("ACD-123", 165, 52.5, 80, 0)

gas_car.Accelerate(random.randint(-10, 15))
electric_car.Accelerate(random.randint(-10, 15))
gas_car.Moving(3)
electric_car.Moving(3)
print(f"sähköauton auton {electric_car.license_plate} matkamittari {electric_car.distance}")
print(f"bensa auton {gas_car.license_plate} matkamittari {gas_car.distance}")
