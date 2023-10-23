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


myCar = Car("ABC-123", 142)
myCar.accelerate(30)
print(myCar.crntSpeed)
myCar.accelerate(70)
print(myCar.crntSpeed)
myCar.accelerate(50)
print(myCar.crntSpeed)
myCar.accelerate(-200)
print(myCar.crntSpeed)

