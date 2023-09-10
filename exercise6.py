import random
import math


# function that generate a dice roll
def roll_dice():
    roll = random.randrange(1, 7)
    return roll


# main program to roll the dice until get 6
while True:
    result = roll_dice()
    if result == 6:
        print("Yeah! You rolled a 6!")
        break
    else:
        print(f"You rolled a {result}.")


# modified dice function that takes the dice sides as a parameter
def roll_dice_side(side):
    roll = random.randrange(1, side+1)
    return roll


# main program that uses roll_dice_side till get the largest number
userSetDice = int(input("How many sides does your dice have?\n"))
while True:
    newResult = roll_dice_side(userSetDice)
    if newResult == userSetDice:
        print(f"Yay! You rolled a {userSetDice}.")
        break
    else:
        print(f"You rolled a {newResult}.")


# convert gallon to liters
def gallon_to_liter(gallon):
    liter = gallon * 3.78541
    return liter


# convert user gallon input into liters till user input negative number
while True:
    userGallon = float(input("How many gallons?\n"))
    if userGallon < 0:
        print("Gallons can't be negative. Exit program.")
        break
    else:
        userLiter = gallon_to_liter(userGallon)
        print(f"{userGallon} gallons are about {userLiter} liters.")


# function that returns the sum of a list of integers
def get_sum(lst):
    listsum = sum(lst)
    return listsum


# main program where user create a list and get the sum
userNum = input("This program will give you the sum of your list. Enter integers. "
                "Separate them with comma.\n").split(",")
userNum = [int(num) for num in userNum]
userSum = get_sum(userNum)
print(f"Their sum is {userSum}.")


# function that returns all the even integers of a list
def get_even(lst):
    even = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
    return even


# main program for printing the user's list and all the even numbers in the list
userNum2 = input("This program will print out the even integers in your list. "
                 "Enter integers. Separate them with comma.\n").split(",")
userNum2 = [int(num) for num in userNum2]
userEven = get_even(userNum2)
print(f"The original numbers are: {userNum2}")
print(f"The even numbers are:{userEven}")


# function that returns the per square meter pizza price
def pizza_price(diameter, euro):
    area = math.pi * (diameter/200)**2
    unit = euro / area
    return unit


# program that compare two pizza's prices
size1, price1 = input("Tell me the diameter of pizza A in centimeter and its price in euros. "
                      "For example: 20,10\n").split(",")
size2, price2 = input("Tell me the diameter of pizza B in centimeter and its price in euros. "
                      "For example: 20,10\n").split(",")
unitPrice1 = pizza_price(float(size1), float(price1))
unitPrice2 = pizza_price(float(size2), float(price2))
if unitPrice1 < unitPrice2:
    print("Pizza A has the better price.")
elif unitPrice1 == unitPrice2:
    print("The two pizzas are about the same price.")
else:
    print("Pizza B has the better price.")
