# Tell the fisher if the zander meets the size limit
standardSize = 42
zanderSize = float(input("Please enter the size of the zander in centimeter:\n"))
difference = standardSize - zanderSize
sizeOkay = difference <= 0
if sizeOkay:
    print("You caught a great zander!")
else:
    zanderComment = f"Your zander is {difference}cm smaller than the standard size. Please release it back to the lake!"
    print(zanderComment)

# Print out a written description of cabin class
cabinClasses = {
    "LUX": "This is an upper-deck cabin with a balcony.",
    "A": "This is a cabin above the car deck, equipped with a window.",
    "B": "This is a windowless cabin above the car deck.",
    "C": "This is a windowless cabin below the car deck."
}
userCabin = input("Enter your cabin class:\n")
if userCabin in cabinClasses:
    print(cabinClasses[userCabin])
else:
    print("Invalid cabin class.")

# evaluate the user's hemoglobin value
bioGender = input("What is your biological gender?(M/F)\n")
hemoglobin = float(input("Enter your hemoglobin value:\n"))
if bioGender == "F":
    if hemoglobin < 117:
        print("Your hemoglobin value is low.")
    elif hemoglobin <= 155:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")
else:
    if hemoglobin < 134:
        print("Your hemoglobin value is low.")
    elif hemoglobin <= 167:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")

# identify leap year
year = int(input("Enter a year:\n"))
if year % 100 == 0:
    if year % 400 == 0:
        print("It is a leap year!")
    else:
        print("It is not a leap year!")
elif year % 4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year.")

