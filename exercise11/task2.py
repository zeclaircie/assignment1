class Car:
    def __init__(self, regNum, maxSpeed):
        self.regNum = regNum
        self.maxSpeed = maxSpeed
        self.crntSpeed = 0
        self.traveldistance = 0

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


class ElectricCar(Car):
    def __init__(self, regNum, maxSpeed, battery_capacity):
        super().__init__(regNum, maxSpeed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, regNum, maxSpeed, gas_tank_volume):
        super().__init__(regNum, maxSpeed)
        self.gas_tank_volume = gas_tank_volume


car1 = ElectricCar("ABC-15", 180, 52.5)
car2 = GasolineCar("ACD-123", 165, 32.3)

car1.crntSpeed = 50
car2.crntSpeed = 80

car1.drive(3)
car2.drive(3)

print(f"{car1.regNum} travelled {car1.traveldistance} km.")
print(f"{car2.regNum} travelled {car2.traveldistance} km.")