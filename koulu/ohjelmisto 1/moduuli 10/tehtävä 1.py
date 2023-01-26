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
elevator = Elevator(9,0,0)
elevator.Go_floor(8)
elevator.Go_floor(0)