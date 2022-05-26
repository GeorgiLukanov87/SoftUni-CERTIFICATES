num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
bol = False
for pair1 in range(num1, (num1+num3) + 1):
    for i in range(2, pair1):
        if (pair1 % i) == 0:
            break
    else:
        for pair2 in range(num2, (num2+num4) + 1):
            for j in range(2, pair2):
                if (pair2 % j) == 0:
                    break
            else:
                print(f"{pair1}{pair2}")
