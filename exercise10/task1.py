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


hissi = Elevator(10, 0, 0)
hissi.go_to_floor(5)
hissi.go_to_floor(0)

