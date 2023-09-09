import random

# print out all numbers divisible by three in the range of 1-1000
divisible = []
numerator = 0
while numerator <= 1000:
    numerator += 3
    divisible.append(numerator)
print(divisible)

# converts inches to centimeters until the user inputs a negative value
inches = float(input("Enter the inches:\n"))
while inches >= 0:
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters} centimeters.\n")
    inches = float(input("Enter the inches:\n"))
print("This is a negative value. Program ends.")

# ask user to input numbers till receiving a blank input, and then print max and min
numList = []
userInput = input("Enter an number. If you're done, input a blank space to quit.\n")
while userInput != " ":
    numList.append(userInput)
    userInput = input("Enter an number. If you're done, input a blank space to quit.\n")
numList = [float(num) for num in numList]
numResult = f"The largest number is {max(numList)} and the smallest number is {min(numList)}."
print(numResult)

# let the user guess a random number
answer = random.randrange(1, 11)
guess = int()
while guess != answer:
    guess = int(input("Take a guess of my number. It's between 1 and 10.\n"))
    if guess < answer:
        print("Too low!")
    if guess > answer:
        print("Too high!")
print("You are correct!")

# check username and password
user = {'python': 'rules'}
inputName = input("Enter user name:")
while inputName not in user:
    print("Non-exist user!")
    inputName = input("Enter user name:")
inputPass = input("Enter password:")
timer = 0
while inputPass != user[inputName]:
    print("Wrong password!")
    timer += 1
    if timer >= 5:
        print("Access denied.")
        exit()
    inputPass = input("Enter password:")
print("Welcome!")



