import math
price_video_card = int(input())
price_prehodnik = int(input())
price_consume = float(input())
daily_income_for_vcard = float(input())
price_video_card *= 13
price_prehodnik *= 13
total_invested = price_prehodnik + price_video_card + 1000
print(total_invested)
daily_income_for_day = daily_income_for_vcard - price_consume
all_income = 13 * daily_income_for_day
total_days_for_return = total_invested/all_income
print(math.ceil(total_days_for_return))