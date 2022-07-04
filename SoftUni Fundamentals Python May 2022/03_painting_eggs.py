size_egg = input()
color_egg = input()
count_painting = int(input())
price = 0
if size_egg == "Large":
    if color_egg == 'Red':
        price = 16
    elif color_egg == 'Green':
        price = 12
    else:
        price = 9
elif size_egg == "Medium":
    if color_egg == 'Red':
        price = 13
    elif color_egg == 'Green':
        price = 9
    else:
        price = 7
else:
    if color_egg == 'Red':
        price = 9
    elif color_egg == 'Green':
        price = 8
    else:
        price = 5
total_sum = (price * count_painting) * 0.65
print(f"{total_sum:.2f} leva.")
