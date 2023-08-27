import math

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
values = [int(n) for n in values]
valueSum = sum(values)
valueProd = math.prod(values)
valueAvg = valueSum / len(values)
valueResult = "Their sum is {}, their product is {}, and their average is {}.".format(valueSum, valueProd, valueAvg)
print(valueResult)

#