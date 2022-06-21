import math
h = int(input())
size = int(input())
percent_not_paint = int(input())
before_percent = h * size * 4
to_paint = before_percent-((percent_not_paint*before_percent)/100)
start_paint = math.ceil(to_paint)
all_ltrs_paint = 0
left_ltrs_paint = 0
command = input()
condition = False
while command != 'Tired!':
    current_paint_ltrs = int(command)
    all_ltrs_paint += current_paint_ltrs
    left_ltrs_paint += all_ltrs_paint - current_paint_ltrs
    to_paint -= current_paint_ltrs
    if to_paint < 0:
        print(f"All walls are painted and you have {abs(to_paint):.0f} l paint left!")
        condition = True
        break
    elif start_paint == all_ltrs_paint:
        print(f"All walls are painted! Great job, Pesho!")
        condition = True
        break
    command = input()
if not condition:
    print(f"{to_paint:.0f} quadratic m left.")
