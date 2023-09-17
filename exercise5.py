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


# tell if an integer is a prime number recursively
def is_prime_recursive(num, i=2):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % i == 0:
        return False
    else:
        is_prime_recursive(num, i+1)
    return True

# tell if an integer is a prime number with for loop
number = int(input("Enter an integer:"))
if number <= 1:
    print("It is not a prime number.")
else:
    for i in range(2, number):
        if number % i == 0:
            print("It is not a prime number!")
            break
    else:
        print("It IS a prime number!")
print(is_prime_recursive(number))

# prompt user to input five cities one by one and print them one by one in the input order
cities = []
for i in range(5):
    city = input("Enter the name of a city:\n")
    cities.append(city)
print("The cities you gave me are:")
for city in cities:
    print(city)




