data = input()
loot = {}
win = ['shards', 'motes', 'fragments']
found = False
while not found:
    data = data.split()
    for el in range(0, len(data), 2):
        key = data[el + 1].lower()
        value = int(data[el])
        if key not in loot:
            loot[key] = value
        else:
            loot[key] += value
        if loot[key] >= 250:
            found = True
            break

    if not found:
        data = input()
    else:
        break

if loot['motes'] >= 250:
    print('Dragonwrath obtained!')
    loot['motes'] -= 250

elif loot['fragments'] >= 250:
    print('Valanyr obtained!')
    loot['fragments'] -= 250

elif loot['shards'] >= 250:
    print('Shadowmourne obtained!')
    loot['shards'] -= 250

if 'shards' not in loot:
    print(f"shards: 0")
else:
    print(f"shards: {loot['shards']}")

if 'fragments' not in loot:
    print(f"fragments: 0")
else:
    print(f"fragments: {loot['fragments']}")

if 'motes' not in loot:
    print(f"motes: 0")
else:
    print(f"motes: {loot['motes']}")

for el in loot:
    if el not in win:
        print(f'{el}: {loot[el]}')
