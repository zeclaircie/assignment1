class Car:
    def __init__(self, regNum, maxSpeed, crntSpeed=0, distance=0):
        self.regNum = regNum
        self.maxSpeed = maxSpeed
        self.crntSpeed = crntSpeed
        self.distance = distance

    def accelerate(self, speedChange):
        newSpeed = self.crntSpeed + speedChange
        if 0 <= newSpeed <= self.maxSpeed:
            self.crntSpeed = newSpeed
        elif newSpeed > self.maxSpeed:
            self.crntSpeed = self.maxSpeed
        else:
            self.crntSpeed = 0
        return

    def drive(self, hours):
        newDistance = self.crntSpeed * hours
        self.distance += newDistance
