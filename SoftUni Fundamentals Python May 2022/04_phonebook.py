data = input()
contacts = {}

while not len(data) == 1:
    data = data.split("-")
    key = data[0]
    value = data[1]
    if key not in contacts:
        contacts[key] = value
    else:
        contacts[key] = value

    data = input()

n = int(data)

for name in range(n):
    searched_name = input()
    if searched_name in contacts:
        print(f'{searched_name} -> {contacts[searched_name]}')
    else:
        print(f"Contact {searched_name} does not exist.")
