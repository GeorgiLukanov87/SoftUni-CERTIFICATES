budget = float(input())
n = int(input())
m = int(input())
p = int(input())

vcard = 250*n
cpu = vcard*0.35*m
ram = vcard*0.10*p

total_sum = (vcard + cpu + ram)

if n > m:
    total_sum = total_sum - (0.15 * total_sum)

result = abs(budget-total_sum)

if budget >= total_sum:
    print(f"You have {result:.2f} leva left!")
else:
    print(f"Not enough money! You need {result:.2f} leva more!")
