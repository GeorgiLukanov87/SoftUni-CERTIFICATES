import math
tennis_racket = float(input())
count_tennis_rackets = int(input())
count_shoes = int(input())
sum_tennis_racket = tennis_racket * count_tennis_rackets
sum_shoes = 1 / 8 * tennis_racket
price_shoes = 1 / 6 * tennis_racket * count_shoes
rest_equipment = (sum_tennis_racket + price_shoes) * 0.2
total_sum = rest_equipment + sum_tennis_racket + price_shoes
price1 = total_sum / 8
price2 = total_sum * 7 / 8
print(f"Price to be paid by Djokovic {math.floor(price1)}")
print(f"Price to be paid by sponsors {math.ceil(price2)}")
