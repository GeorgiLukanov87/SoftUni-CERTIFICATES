import math
x = int(input())
y = float(input())
z = int(input())
workers = int(input())

grapes = x * y
wine = (grapes * 0.40) / 2.5
result = math.ceil(wine-z)

if wine >= z:
    print(f"Good harvest this year! Total wine: {math.ceil(wine)} liters.")
    print(f"{result} liters left -> {math.ceil(result/workers)} liters per person.")
else:
    print(f"It will be a tough winter! More {abs(result)} liters wine needed.")
