import random
# estimate the value of Pi
total = 0
inCircle = 0
target = int(input("How many random point should I generate for Pi estimation?"))
while total < target:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x**2 + y**2 < 1):
        inCircle += 1
    total += 1
estimatedPi = 4 * inCircle / total
print(f"The value of Pi is approximately {estimatedPi}.")
