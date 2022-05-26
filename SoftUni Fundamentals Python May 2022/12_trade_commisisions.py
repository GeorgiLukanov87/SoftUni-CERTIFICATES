town = input()
money = float(input())
commission = 0

if town == 'Sofia':
    if 0 <= money <= 500:
        commission = 0.05 * money
    elif 500 < money <= 1000:
        commission = 0.07 * money
    elif 1000 < money <= 10000:
        commission = 0.08 * money
    else:
        commission = 0.12 * money

elif town == 'Varna':
    if 0 <= money <= 500:
        commission = 0.045 * money
    elif 500 < money <= 1000:
        commission = 0.075 * money
    elif 1000 < money <= 10000:
        commission = 0.10 * money
    else:
        commission = 0.13 * money

elif town == 'Plovdiv':
    if 0 <= money <= 500:
        commission = 0.055 * money
    elif 500 < money <= 1000:
        commission = 0.08 * money
    elif 1000 < money <= 10000:
        commission = 0.12 * money
    else:
        commission = (0.145 * money)

if commission >= 0 and town == "Plovdiv" or town =='Varna' or town =='Sofia':
    print(f'{commission:.2f}')
else:
    print('error')


