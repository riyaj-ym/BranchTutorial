"""Author:RYM
Developer:RYM
Date: 02-01-2023"""

number = int(input("Enter Number:\n"))

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is Not prime")
        break
else:
    print(f"{number} is prime")
