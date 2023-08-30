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

#