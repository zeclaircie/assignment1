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
    elevators = []
    def __init__(self,topfloor, bottomfloor, elevator):
        self.topfloor = topfloor
        self.bottomfloor = bottomfloor
        self.elevator = elevator
        for i in range(self.elevator):
            Building.elevators.append(Elevator(topfloor, bottomfloor))

    def run_elevator(self, num):
        