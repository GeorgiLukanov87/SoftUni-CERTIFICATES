def longest_line(x, y):
    left_side = 0
    right_side = 0
    negative = []
    positive = []
    if x < 0:
        negative.append(x)
    else:
        positive.append(x)

    if y < 0:
        negative.append(y)
    else:
        positive.append(y)

    left_side = (negative)
    right_side = (positive)

    print(f"Positive = {positive},Negative = {negative},\nLeft = {left_side},Right = {right_side}")
    if len(negative) == 0:
        negative = 0
    if len(positive) == 0:
        positive == 0

    longer_line = [positive] + [negative]
    print(longer_line)

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())
result = longest_line(x1, y1)
print(result)
result = longest_line(x2, y2)
print(result)
result = longest_line(x3, y3)
print(result)
result = longest_line(x4, y4)
print(result)
