count_painted_eggs = int(input())
max_eggs = - 1000000000
color_of_max_eggs = ""
c1 = 0
c2 = 0
c3 = 0
c4 = 0
for i in range(1, count_painted_eggs+1):
    color = input()
    if color == 'red':
        c1 += 1
        if c1 > max_eggs:
            max_eggs = c1
            color_of_max_eggs = color
    elif color == 'orange':
        c2 += 1
        if c2 > max_eggs:
            max_eggs = c2
            color_of_max_eggs = color
    elif color == 'blue':
        c3 += 1
        if c3 > max_eggs:
            max_eggs = c3
            color_of_max_eggs = color
    elif color == 'green':
        c4 += 1
        if c4 > max_eggs:
            max_eggs = c4
            color_of_max_eggs = color
print(f"Red eggs: {c1}")
print(f"Orange eggs: {c2}")
print(f"Blue eggs: {c3}")
print(f"Green eggs: {c4}")
print(f"Max eggs: {max_eggs} -> {color_of_max_eggs}")