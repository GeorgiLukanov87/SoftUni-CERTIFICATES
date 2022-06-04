import math
tournaments = int(input())
start_points = int(input())
new_points = 0
sum_points = 0
wins = 0
for tours in range(tournaments):
    result = input()
    if result == "F":
        new_points = 1200
        sum_points += new_points
    elif result == "SF":
        new_points = 720
        sum_points += new_points
    elif result == "W":
        wins += 1
        new_points = 2000
        sum_points += new_points
final_result = sum_points + start_points
print(f"Final points: {final_result}")
print(f"Average points: {math.floor((sum_points / tournaments)):.0f}")
print(f"{((wins / tournaments) * 100):.2f}%")
