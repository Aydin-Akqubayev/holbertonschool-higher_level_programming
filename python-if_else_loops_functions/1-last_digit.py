#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (abs(number) % 10)*(int(number/abs(number)))
str=""
if last_digit > 5:
    str = "and is greater than 5"
elif last_digit == 0:
    str = "and is 0"
elif last_digit < 6 and last_digit == 0:
    str = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {str}")
