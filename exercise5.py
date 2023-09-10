import random

# roll the dice and print out the sum
rolls = int(input("How many times should I roll the dice?\n"))
results = []
for i in range(rolls):
    results.append(random.randrange(1, 7))
print(f"The sum of the numbers is {sum(results)}")

# prompt user to input numbers and print out the largest five in descending order
allNum = []
while True:
    inputNum = input("Give me a number. Enter a blank space to quit.\n")
    if inputNum == " ":
        break
    allNum.append(float(inputNum))
allNum.sort(reverse=True)
if len(allNum) < 5:
    print("You input less than five numbers. They are:")
    for num in allNum:
        print(num)
else:
    print("The largest five are:")
    for i in range(5):
        print(allNum[i])

# prompt user to input five cities one by one and print them one by one in the input order
cities = []
for i in range(5):
    city = input("Enter the name of a city:\n")
    cities.append(city)
print("The cities you gave me are:")
for city in cities:
    print(city)




