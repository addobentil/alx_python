#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    print("Last digit of",number,"is",last_digit,"and is greater than 5" , end="\n")
elif last_digit == 0:
    print("Last digit of",number,"is",last_digit,"and is 0", end="\n")
elif last_digit < 0:
    sign  = '-'
    print("Last digit of",number,"is",sign+last_digit,"and is less than 6 not 0", end="\n")
else :
    print("Last digit of",number,"is",last_digit,"and is less than 6 not 0", end="\n")