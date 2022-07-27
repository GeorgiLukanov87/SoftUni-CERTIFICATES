total_money = int(input())
statues_price = total_money*0.70
catering_price = statues_price*0.85
sound_price = catering_price * 0.50
total_sum = total_money + statues_price + catering_price + sound_price
print(f"{total_sum:.2f}")