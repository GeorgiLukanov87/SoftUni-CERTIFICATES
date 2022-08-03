energy = int(input())
command = input()
wins = 0
finished = False
while not command == 'End of battle':
    distance = int(command)

    if energy >= distance:
        wins += 1
        energy -= distance
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        finished = True
        break

    if wins % 3 == 0:
        energy += wins
    command = input()
if not finished:
    print(f"Won battles: {wins}. Energy left: {energy}")
