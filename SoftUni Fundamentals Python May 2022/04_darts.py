player_name = input()
total_sum = 301
current_shot = 0
counter_shots = 0
fail_shot_counter = 0
retired = False
while total_sum != 0:
    shoot = input()
    if shoot == 'Retire':
        print(f"{player_name} retired after {fail_shot_counter} unsuccessful shots.")
        retired = True
        break
    points = int(input())
    counter_shots += 1
    if shoot == 'Single':
        if points > total_sum:
            fail_shot_counter += 1
        else:
            current_shot += points
            total_sum -= points
    elif shoot == 'Double':
        if 2 * points > total_sum:
            fail_shot_counter += 1
        else:
            total_sum -= points * 2
            current_shot += points
    else:
        if 3 * points > total_sum:
            fail_shot_counter += 1
        else:
            total_sum -= points * 3
            current_shot += points
if not retired:
    print(f"{player_name} won the leg with {counter_shots-fail_shot_counter} shots.")








