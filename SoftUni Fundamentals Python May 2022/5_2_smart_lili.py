age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toy_count = 0
sum = 0
money = 0


for year in range(1, age+1):
    if year%2==0:
        money = money+10
        sum = sum + money+9
    else:
        toy_count = toy_count+1

sum = sum + toy_price*toy_count

if sum >= washing_machine_price:
    diff = sum - washing_machine_price
    print("Yes!{0:.2f}" .format(diff))
else:
    diff = washing_machine_price - sum
    print("No!{0:.2f}".format(diff))
