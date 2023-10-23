class Car:
    def __init__(self, regNum, maxSpeed, crntSpeed = 0, distance = 0):
        self.regNum = regNum
        self.maxSpeed = maxSpeed
        self.crntSpeed = crntSpeed
        self.distance = distance


myCar = Car("ABC-123", 142)

print("The specifications of my new car are:")
print(f"Registration number: {myCar.regNum}\nMaximum speed: {myCar.maxSpeed}km/h\n"
      f"Current speed: {myCar.crntSpeed}km/h\nTraveled distance: {myCar.distance}km")


