import math
hours_need = int(input())
all_days = int(input())
workers = int(input())

all_days_left = all_days - (all_days * 0.1)

working_hours = all_days_left * 8
extra_hours = workers * (2 * all_days)

total_hours = working_hours + extra_hours
final_sum = abs(total_hours - hours_need)

if total_hours >= hours_need:
    print(f'Yes!{math.ceil(final_sum)} hours left.')
else:
    print(f'Not enough time!{math.ceil(final_sum)} hours needed.')
