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
class Aten_autot:



Cars = []
number = 1

random_num = random.randint(100, 200)
for i in range(10):
    Cars.append(Racecar("abc-" + str(number), random.randint(100, 200), 0, 0))
    number = number + 1
#print(Cars)

maxdistance = 0
while True:
    for Racecar in Cars:
        Racecar.Accelerate(random.randint(-10, 15))
        Racecar.Moving(1)
        if Racecar.distance >= maxdistance:
            maxdistance = Racecar.distance
    if maxdistance >= 10000:
        for Racecar in Cars:
            print(f"auto {Racecar.license_plate} kulki {Racecar.distance}km. Auton maksiminopeus oli {Racecar.max_speed}km/h")
        break

