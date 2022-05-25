count_persons = int(input())
count_score = float(input())
season = input()
destination = input()
result = 0
if destination == 'Abroad':
    result = (count_score * count_persons)*1.50
    if season == 'summer':
        result *= 0.90
    elif season == 'winter':
        result *= 0.85

elif destination == 'Bulgaria':
    result = (count_score * count_persons)
    if season == 'summer':
        result *= 0.95
    elif season == 'winter':
        result *= 0.92

charity_result = result * 0.75
print(f"Charity - {charity_result:.2f}")
rest_money = result - charity_result
print(f"Money per dancer - {rest_money/count_persons:.2f}")

