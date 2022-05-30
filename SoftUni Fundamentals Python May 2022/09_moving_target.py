def is_index_valid(targets, index):
    if 0 <= int(index) < len(targets):
        return True
    return False


def shoot_function(targets, command):
    action, index, power = command.split()
    index = int(index)
    power = int(power)
    if is_index_valid(targets, index):
        targets[index] -= power
        if int(targets[index]) <= 0:
            targets.remove(targets[index])
    return targets

def add_function(targets, command):
    action, index, value = command.split()
    index = int(index)
    value = int(value)
    if is_index_valid(targets, index):
        targets.insert(index, value)
        return targets
    print("Invalid placement!")


def strike_function(targets, command):
    action, index, radius = command.split()
    index = int(index)
    radius = int(radius)
    left_side = targets[:index]
    right_side = targets[index+1:]
    if radius <= len(left_side) and radius <= len(right_side) and is_index_valid(targets,index):
        for num in range(radius):
            left_side.remove(left_side[-1])
            right_side.pop(0)
        targets.clear()
        targets += left_side+right_side
        return targets
    else:
        print('Strike missed!')


targets = list(map(int, input().split()))
command = input()

while not command == 'End':
    if 'Shoot' in command:
        shoot_function(targets, command)
    elif 'Strike' in command:
        strike_function(targets, command)
    elif 'Add' in command:
        add_function(targets, command)
    command = input()

targets = ('|'.join(str(el) for el in targets))
print(targets)
