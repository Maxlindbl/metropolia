import random
from prettytable import PrettyTable, from_db_cursor



class Race:
    def __init__(self, race_name, race_distance, participants):
        self.race_name = race_name
        self.race_distance = race_distance
        self.cars_list = []
        number = 1
        for i in range(participants):
            self.cars_list.append(Racecar("abc-" + str(number), random.randint(100, 200), 0, 0))
            number = number + 1

    def One_hour(self,):
        for Racecar in self.cars_list:
            Racecar.Accelerate(random.randint(-10, 15))
            Racecar.Moving(1)

    def Print_status(self,):
        my_table = PrettyTable()
        my_table.field_names = ["rekisterinumero", "ajettu matka", "huippunopeus"]
        for Racecar in self.cars_list:
            my_table.add_row([Racecar.license_plate, Racecar.distance, Racecar.max_speed])
        my_table.sortby = "ajettu matka"
        my_table.reversesort = True
        print(my_table)


    def Race_over(self,):
        maxdistance = 0
        for Racecar in self.cars_list:
            if Racecar.distance >= maxdistance:
                maxdistance = Racecar.distance
        return maxdistance > self.race_distance




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



race = Race("Suuri romuralli", 8000, 10)
hour = 10
while race.Race_over()  is False:
    for i in range(10):
        if race.Race_over():
            break
        race.One_hour()
    print(f"kisan tilanne tunti {hour}")
    hour = hour + 10
    race.Print_status()
print("kisa on ohi ja tulokset on")
race.Print_status()

