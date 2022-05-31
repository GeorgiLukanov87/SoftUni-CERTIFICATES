x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x = float(input())
y = float(input())


if (y > y1 and y < y2) and (x> x1 and x < x2):
    print('Inside / Outside')
elif ((y >= y1 and y <= y2) and (x>= x1 and x <= x2)) and (x1 == x or y1 == y):
    print("Border")
elif ((y >= y1 and y <= y2) and (x>= x1 and x <= x2)) and (x2 == x or y2 == y):
    print("Border")
else:
    print("Inside / Outside")