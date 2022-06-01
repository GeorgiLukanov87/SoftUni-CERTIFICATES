num_pairs = int(input())
max_diff = 0
current_sum = 0
sum_first_pair = 0
diff = 0
for i in range(1, 2 * num_pairs + 1):
    number = int(input())
    current_sum += number
    if i % 2 == 0 and i != 2:
        diff = abs(current_sum - sum_first_pair)
        if diff > max_diff:
            max_diff = diff
        sum_first_pair = current_sum
        current_sum = 0
    elif i == 2:
        sum_first_pair = current_sum
        current_sum = 0

if max_diff == 0:
    print(f'Yes, value={sum_first_pair}')
else:
    print(f'No, maxdiff={max_diff}')