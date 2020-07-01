import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

print("Random number 1 is: ", num1)
print("Random number 2 is: ", num2)

if num1 >> num2:
    print("Number 1 is bigger")
elif num2 > num1:
	print("Number 2 is bigger")
elif num1==num2:
	print("Numbers are equal")