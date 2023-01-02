"""Author:RYM
Developer:GRM
Date: 02-01-2023
Day: Monday"""

number = int(input("Enter Number:\n"))

prime = True


def primeNumber(n):
    primeN = True
    for i in range(2, number):
        if n % i == 0:
            primeN = False
    return primeN


if primeNumber(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
