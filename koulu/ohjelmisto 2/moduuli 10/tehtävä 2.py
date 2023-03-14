class House:
    def __init__(self,house_top_floor, house_bottom_floor, ammount):
        self.house_top_floor = house_top_floor
        self.house_bottom_floor = house_bottom_floor
        self.elevators = []
        self.ammount = ammount
        self.elevator_floor = house_bottom_floor
        for i in range(self.ammount):
            self.elevators.append(Elevator(self.house_top_floor, self.house_bottom_floor, self.elevator_floor))

    def Action(self,elevator_number, floor_number):
        print(f"hissi {elevator_number}")
        self.elevators[elevator_number - 1].Go_floor(floor_number)



class Elevator:
    def __init__(self,top_floor, bottom_floor, floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.floor = floor
#määrittellään pitääkö hissin mennä ylös vai alas
    def Go_floor(self, go_to):
        while self.floor != go_to:
            if self.floor < go_to:
                self.Go_up()
            if self.floor > go_to:
                self.Go_down()
        print(f"olet perillä kerroksessa {self.floor}")
#hissi ylös
    def Go_up(self,):
        self.floor = self.floor + 1
        print(self.floor)
#hissi alas
    def Go_down(self,):
        self.floor = self.floor - 1
        print(self.floor)



#kutsutaan hissiä

house = House(25,0,3)

house.Action(1,20)
house.Action(3,15)
house.Action(1,10)
house.Action(2,8)