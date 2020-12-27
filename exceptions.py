import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except:
    print("Invalid input")
    exit(1)

try:
    result = x/y
    print(f"{x} / {y} = {result}")
except:
    print("Cannot divided by zero")
    exit(1)