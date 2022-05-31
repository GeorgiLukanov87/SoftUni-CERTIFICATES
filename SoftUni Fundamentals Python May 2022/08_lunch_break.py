import math
serial_name = input()
episode = int(input())
all_time = int(input())

relax_time = 1 / 4 * all_time
lunch_time = 1 / 8 * all_time

left_time = abs(all_time - (lunch_time + relax_time))
result = abs(left_time-episode)

if left_time >= episode:
    print(f"You have enough time to watch {serial_name} "
          f"and left with {math.ceil(result)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, "
          f"you need {math.ceil(result)} more minutes.")

