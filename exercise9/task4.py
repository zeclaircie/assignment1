import random
from tabulate import tabulate

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


cars = []
for i in range(10):
    regnum = f"ABC-{i+1}"
    mspeed = random.randrange(100, 200)
    cars.append(Car(regnum, mspeed))

stop = False
while not stop:
    for car in cars:
        if car.distance >= 10000:
            stop = True
        car.accelerate(random.randrange(-10, 15))
        car.drive(1)


tbl = tabulate({"Registration Number": [car.regNum for car in cars],
                "Maximum Speed": [car.maxSpeed for car in cars],
                "Current Speed": [car.crntSpeed for car in cars],
                "Travelled Distance": [car.distance for car in cars]}, headers="keys")
print(tbl)
