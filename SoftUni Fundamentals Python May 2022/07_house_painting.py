x = float(input())
y = float(input())
h = float(input())

side1 = (2 * (x * y) - 2 * (1.5 * 1.5)) / 3.4  # both sides without - 2 * windows
side2 = (2 * (x * x) - (1.2 * 2)) / 3.4  # /3.4 green paint

roof1 = ((2 * (x * h / 2)) / 4.3)  # trianle side of roof * 2
roof2 = ((2 * (x * y)) / 4.3)  # left space of roof(top roof) * 2

green_paint = side1 + side2
red_paint = roof1 + roof2

print('%.2f' % green_paint)
print('%.2f' % red_paint)
