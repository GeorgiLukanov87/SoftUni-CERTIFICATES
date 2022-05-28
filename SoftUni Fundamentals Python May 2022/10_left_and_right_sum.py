n = int(input())
left_sum = 0
right_sum = 0

for number in range(1, n + 1):
    new_num = int(input())
    left_sum = left_sum + new_num

for number in range(1, n + 1):
    new_num = int(input())
    right_sum = right_sum + new_num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
