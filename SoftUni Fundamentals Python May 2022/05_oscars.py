actor_name = input()
academy_points = float(input())
n = int(input())
points_reached = 0
total_points_reached = 0
for i in range(1, n + 1):
    if total_points_reached > 1250:
        break
    judge_name = input()
    judge_points = float(input())
    points_reached += (len(judge_name) * judge_points) / 2
    total_points_reached = points_reached + academy_points
    diff = abs(1250.5 - total_points_reached)
if total_points_reached < 1250.5:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points_reached:.1f}!")
