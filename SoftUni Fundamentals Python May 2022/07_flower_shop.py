import math

magnoles = int(input())
zumbules = int(input())
roses = int(input())
cactus = int(input())
gift_amount = float(input())
total_sum_after_pay = 0
magnoles_price = magnoles * 3.25
zumbules_price = zumbules * 4
roses_price = roses * 3.50
cactus_price = cactus * 8

total_sum = magnoles_price + zumbules_price + roses_price + cactus_price
total_sum_after_pay = total_sum - (total_sum * 0.05)

final_sum = total_sum_after_pay-gift_amount

if final_sum < 0:
    print(f"She will have to borrow {abs(math.floor(total_sum_after_pay-gift_amount))} leva.")
else:
    print(f"She is left with {math.floor(total_sum_after_pay-gift_amount)} leva.")

