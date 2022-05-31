import math
group_members = int(input())
total_days = int(input())
total_coins = 0
for days in range(1, total_days+1):
    if days % 10 == 0:
        group_members -= 2
    if days % 15 == 0:
        group_members += 5
    total_coins += 50 - (group_members * 2)
    if days % 3 == 0:
        total_coins -= group_members * 3
    if days % 5 == 0:
        total_coins += 20 * group_members
        if days % 3 == 0:
            total_coins -= group_members * 2
print(f"{group_members} companions received {math.floor(total_coins/group_members)} coins each.")
