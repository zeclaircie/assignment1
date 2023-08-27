import math
import random

# greet the user by name
name = input("What's your name?\n")
greet = f"Moi, {name}!"
print(greet)

# calculate the area of the user's circle
radius = float(input("What's the radius of your circle?\n"))
circleArea = math.pi * radius ** 2
print("The area is: {:.2f}".format(circleArea))

# calculate the perimeter and area of the user's rectangle
length = float(input("What's the length of the rectangle?\n"))
width = float(input("What's the width of the rectangle?\n"))
rectArea = length * width
rectPeri = length * 2 + width * 2
rectResult = "The area is {}, and the perimeter is {}.".format(rectArea, rectPeri)
print(rectResult)

# calculate the sum, product, and average of use's inputs
values = input("Enter three integer values seperated by comma:\n").split(",")
values = [int(value) for value in values]
valueSum = sum(values)
valueProd = math.prod(values)
valueAvg = valueSum / len(values)
valueResult = "Their sum is {}, their product is {}, and their average is {}.".format(valueSum, valueProd, valueAvg)
print(valueResult)

# convert medieval units into modern units
convertRates = [20, 32, 13.3]
medievalInputs = input("Enter weight in talents, pounds, and lots, seperated by comma:\n").split(",")
medievalInputs = [float(medievalInput) for medievalInput in medievalInputs]
sumWeight = 0
for inputID, medievalInput in enumerate(medievalInputs):
    for convertRate in convertRates[inputID:]:
        medievalInput *= convertRate
    sumWeight += medievalInput
kilos = sumWeight // 1000
grams = sumWeight % 1000
weightResult = "The weight in modern units is:\n{} kilograms and {:.2f} grams.".format(kilos, grams)
print(weightResult)

# draw a random combination of 3 integer between 0 and 9
chooseThreeFrom = [i for i in range(0, 10)]
threeDigi = random.choices(chooseThreeFrom, k=3)
threeDigiResult = f"Your code is:{threeDigi}"
print(threeDigiResult)

# draw a random combination of 4 integer between 1 and 6
chooseFourFrom = [i for i in range(1, 7)]
fourDigi = random.choices(chooseFourFrom, k=4)
fourDigiResult = f"Your code is:{fourDigi}"
print(fourDigiResult)
