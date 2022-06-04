data = input()

courses_dict = {}

while not data == 'end':
    data = data.split(' : ')
    course = data[0]
    name = data[1]
    if course not in courses_dict:
        courses_dict[course] = [name]
    else:
        courses_dict[course].append(name)

    data = input()

for el in courses_dict:
    print(f'{el}: {len(courses_dict[el])}')
    for name in courses_dict[el]:
        print(f'-- {name}')