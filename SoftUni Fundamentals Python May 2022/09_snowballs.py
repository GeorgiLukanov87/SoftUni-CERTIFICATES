import sys
n = int(input())
value = 0
max_value = - sys.maxsize
winner_value_ball = 0
win_weight = 0
win_time = 0
win_quality = 0
for i in range(1, n+1):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality
    if value > max_value:
        max_value = value
        winner_value_ball = max_value
        win_weight = weight
        win_time = time
        win_quality = quality
print(f"{win_weight} : {win_time} = {int(winner_value_ball)} ({win_quality})")
