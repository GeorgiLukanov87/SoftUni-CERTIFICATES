n = int(input())
data = {}

for _ in range(n):
    command = input().split('<->')
    plant = command[0]
    rarity = int(command[1])
    if plant not in data:
        data[plant] = [rarity] + [0]
    else:
        data[plant][0] = rarity
command = input()
while not command == 'Exhibition':
    command = command.split(": ")
    details = command[1]
    details = details.split(" - ")
    name = details[0]
    if name not in data:
        print('error')
        command = input()
        continue
    if command[0] == 'Rate':
        rate = int(details[1])
        if name in data:
            if data[name][1] == 0:
                data[name][1] += rate
            else:
                data[name][1] += rate
                data[name][1] /= 2

    elif command[0] == 'Update':
        details = command[1]
        details = details.split(' - ')
        rate = int(details[1])
        if name in data:
            data[name][0] = rate
    elif command[0] == 'Reset':
        if name in data:
            data[name][1] = 0
    command = input()
print("Plants for the exhibition:")
for el in data:
    print(f"- {el}; Rarity: {data[el][0]}; Rating: {data[el][1]:.2f}")
