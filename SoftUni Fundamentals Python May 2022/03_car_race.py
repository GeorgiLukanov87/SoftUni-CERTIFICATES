time = list(map(int, input().split(" ")))
divisor = len(time)//2
left_time = time[:divisor]
right_time = time[:divisor:-1]
left_racer_time = 0
for index in range(len(left_time)):
    if left_time[index] == 0:
        left_racer_time *= 0.80
    left_racer_time += left_time[index]
right_racer_time = 0
for index in range(len(right_time)):
    if right_time[index] == 0:
        right_racer_time *= 0.80
    right_racer_time += right_time[index]
if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
