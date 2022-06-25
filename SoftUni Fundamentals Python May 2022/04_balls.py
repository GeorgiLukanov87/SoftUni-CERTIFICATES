count_balls = int(input())
total_points = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
other_color = 0
black_ball = 0
for i in range(1, count_balls+1):
    color = input()
    if color == 'red':
        c1 += 1
        total_points += 5
    elif color == 'orange':
        c2 += 1
        total_points += 10
    elif color == 'yellow':
        c3 += 1
        total_points += 15
    elif color == 'white':
        c4 += 1
        total_points += 20
    elif color == 'black':
        total_points //= 2
        black_ball += 1
    else:
        other_color += 1
print(f"Total points: {total_points:.0f}")
print(f"Red balls: {c1}")
print(f"Orange balls: {c2}")
print(f"Yellow balls: {c3}")
print(f"White balls: {c4}")
print(f"Other colors picked: {other_color}")
print(f"Divides from black balls: {black_ball}")