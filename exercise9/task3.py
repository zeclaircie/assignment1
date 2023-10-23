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

myCar = Car("ABC-123", 142)
myCar.accelerate(30)
print(f"The current speed is {myCar.crntSpeed}km/h")
myCar.drive(2)
print(f"The car travelled {myCar.distance}km in total.")
myCar.accelerate(50)
myCar.drive(1)
print(f"The car travelled {myCar.distance}km in total.")
