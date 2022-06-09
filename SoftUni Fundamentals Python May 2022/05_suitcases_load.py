luggage_cap = float(input())
command = input()
luggage_counter = 0
condition = False
while command != 'End':
    volume_luggage = float(command)
    luggage_counter += 1
    if luggage_counter % 3 == 0:
        volume_luggage *= 1.10

    if volume_luggage > luggage_cap:
        print('No more space!')
        condition = True
        luggage_counter -= 1
        break
    luggage_cap -= volume_luggage
    command = input()
if not condition:
    print(f"Congratulations! All suitcases are loaded!")
print(f"Statistic: {luggage_counter} suitcases loaded.")
