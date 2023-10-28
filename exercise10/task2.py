class Elevator:
    def __init__(self, topfloor, bottomfloor, crtfloor=0):
        self.topfloor = topfloor
        self.bottomfloor = bottomfloor
        self.crtfloor = crtfloor

    def go_to_floor(self, fl):
        while fl > self.crtfloor:
            self.floor_up()
        while fl < self.crtfloor:
            self.floor_down()
        print(f"Arrived at floor {fl}.")

    def floor_up(self):
        self.crtfloor += 1
        print(f"You are now at floor {self.crtfloor}")

    def floor_down(self):
        self.crtfloor -= 1
        print(f"You are now at floor {self.crtfloor}")

class Building:
    def __init__(self,topfloor, bottomfloor, elevatornum):
        self.topfloor = topfloor
        self.bottomfloor = bottomfloor
        self.elevatornum = elevatornum
        self.elevators = []
        for i in range(self.elevatornum):
            self.elevators.append(Elevator(topfloor, bottomfloor))

    def run_elevator(self, elenum, destfloor):
        print(f"Elevator {elenum} selected. Going to floor {destfloor}.")
        self.elevators[elenum-1].go_to_floor(destfloor)


building = Building(20, 0, 5)
building.run_elevator(2, 10)
