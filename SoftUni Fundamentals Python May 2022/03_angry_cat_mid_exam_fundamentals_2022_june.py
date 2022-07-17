ratings = list(map(int, input().split(', ')))
start_index = int(input())
type_items = input()
left_side = ratings[:start_index][::-1]
right_side = ratings[start_index+1:]

left_damage = []
right_damage = []
entry_point = ratings[start_index]

for item in left_side:
    if type_items == 'cheap':
        if item < entry_point:
            left_damage.append(item)
    elif type_items == 'expensive':
        if item >= entry_point:
            left_damage.append(item)

for item in right_side:
    if type_items == 'cheap':
        if item < entry_point:
            right_damage.append(item)
    elif type_items == 'expensive':
        if item >= entry_point:
            right_damage.append(item)

if sum(left_damage) >= sum(right_damage):
    print(sum(left_damage))
else:
    print(sum(right_damage))
