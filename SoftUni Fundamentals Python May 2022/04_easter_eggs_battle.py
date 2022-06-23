egg_1st_player = int(input())
egg_2nd_player = int(input())
total_eggs_1st = egg_1st_player
total_eggs_2nd = egg_2nd_player
condition = False
command = input()
status = ""
while command != 'End':
    status = command
    if status == 'one':
        total_eggs_2nd -= 1
    else:
        total_eggs_1st -= 1
    if total_eggs_1st == 0:
        print(f"Player one is out of eggs. Player two has {total_eggs_2nd} eggs left.")
        condition = True
        break
    elif total_eggs_2nd == 0:
        print(f"Player two is out of eggs. Player one has {total_eggs_1st} eggs left.")
        condition = True
        break
    command = input()
if not condition:
    print(f"Player one has {total_eggs_1st} eggs left.")
    print(f"Player two has {total_eggs_2nd} eggs left.")
