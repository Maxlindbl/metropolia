class House:
    def __init__(self,house_top_floor, house_bottom_floor, elevators):
        self.house_top_floor = house_top_floor
        self.house_bottom_floor = house_bottom_floor
        self.elevators = []

    def Action(self,elevator_number, floor_number):
        self.elevators.append(Elevator)


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
        print("olet perillä")
#hissi ylös
    def Go_up(self,):
        self.floor = self.floor + 1
        print(self.floor)
#hissi alas
    def Go_down(self,):
        self.floor = self.floor - 1
        print(self.floor)



#kutsutaan hissiä
elevator = Elevator(25,0,0)
house = House(25,0,3)

elevator.Go_floor(7)
elevator.Go_floor(0)
house.Action(2,8)