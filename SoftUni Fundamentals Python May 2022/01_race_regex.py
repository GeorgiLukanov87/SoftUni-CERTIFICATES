names = input().split(', ')
command = input()
names_points = {}
while not command == 'end of race':
    new_name = ""
    sum_points = 0
    for ch in command:
        if ch.isalpha():
            new_name += ch
        if ch.isdigit():
            sum_points += int(ch)
    if new_name in names:
        if new_name not in names_points.keys():
            names_points[new_name] = 0
        names_points[new_name] += sum_points

    command = input()
counter = 0
for name, points in sorted(names_points.items(), key=lambda kv: -kv[1]):
    counter += 1
    if counter == 1:
        print(f'1st place: {name}')
    elif counter == 2:
        print(f'2nd place: {name}')
    elif counter == 3:
        print(f'3rd place: {name}')
        break