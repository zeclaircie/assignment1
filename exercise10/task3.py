class Elevator:
    def __init__(self, topfloor, bottomfloor):
        self.topfloor = topfloor
        self.bottomfloor = bottomfloor
        self.crtfloor = bottomfloor

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
    def __init__(self, topfloor, bottomfloor, elevatornum):
        self.topfloor = topfloor
        self.bottomfloor = bottomfloor
        self.elevatornum = elevatornum
        self.elevators = {}
        for i in range(self.elevatornum):
            self.elevators[i+1] = Elevator(topfloor, bottomfloor)

    def run_elevator(self, elenum, destfloor):
        print(f"Elevator {elenum} selected. Going to floor {destfloor}.")
        self.elevators[elenum].go_to_floor(destfloor)

    def fire_alarm(self):
        print(f"FIRE! FIRE! FIRE! All elevators to floor {self.bottomfloor}!!")
        for i in range(1, self.elevatornum+1):
            self.elevators[i].crtfloor = self.bottomfloor


building = Building(20, 0, 5)
building.run_elevator(3, 10)
building.run_elevator(2, 7)
print(f"Elevator 3 is now at floor {building.elevators[3].crtfloor}.")
print(f"Elevator 2 is now at floor {building.elevators[2].crtfloor}.")
building.fire_alarm()

print(f"Elevator 3 is now at floor {building.elevators[3].crtfloor}.")
print(f"Elevator 2 is now at floor {building.elevators[2].crtfloor}.")
