import random
from tabulate import tabulate


class Car:
    def __init__(self, regNum, maxSpeed, crntSpeed=0, traveldistance=0):
        self.regNum = regNum
        self.maxSpeed = maxSpeed
        self.crntSpeed = crntSpeed
        self.traveldistance = traveldistance

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
        self.traveldistance += newDistance


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randrange(-10, 15))
            car.drive(1)

    def print_status(self):
        tbl = tabulate({"Registration Number": [car.regNum for car in self.cars],
                        "Maximum Speed": [car.maxSpeed for car in self.cars],
                        "Current Speed": [car.crntSpeed for car in self.cars],
                        "Travelled Distance": [car.traveldistance for car in self.cars]}, headers="keys")
        print(tbl)

    def race_finished(self):
        alldistance = [car.traveldistance for car in self.cars]
        if max(max(alldistance), self.distance) == self.distance:
            return False
        else:
            return True


participants = []
for i in range(10):
    regnum = f"ABC-{i+1}"
    mspeed = random.randrange(100, 200)
    participants.append(Car(regnum, mspeed))

race = Race("Grand Demolition Derby", 8000, participants)

print(f"{race.name} now starts!")
hourCount = 0
while not race.race_finished():
    race.hour_passes()
    hourCount += 1
    if hourCount % 10 == 0:
        print("10 hours passed. Here's the current status:")
        race.print_status()

print("\nRace ends!! Here's the final result:")
race.print_status()
