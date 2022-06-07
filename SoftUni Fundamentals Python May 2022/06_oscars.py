actor_name = input()
academy_points = float(input())
count_judges = int(input())
total_points = 0
needed_award_points = 1250.5

for actor in range(count_judges):
    judge_name = input()
    judge_points = float(input())
    counter_letters = len(judge_name)
    total_points += ((counter_letters * judge_points) / 2)
    if total_points+academy_points >= needed_award_points:
        break
if total_points+academy_points <= needed_award_points:
    print(f"Sorry, {actor_name} you need {needed_award_points-(abs(total_points+academy_points)):.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points+academy_points:.1f}!")


