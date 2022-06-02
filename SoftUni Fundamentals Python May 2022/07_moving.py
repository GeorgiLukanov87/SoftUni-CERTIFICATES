a = int(input())
b = int(input())
h = int(input())

available_space = a * b * h
sum_box = 0
while True:
    current_box = input()
    if current_box == "Done":
        print(f"{available_space - sum_box} Cubic meters left.")
        break
    current_box = int(current_box)
    sum_box += current_box

    if sum_box >= available_space:
        print(f"No more free space! You need {sum_box - available_space} Cubic meters more.")
        break

