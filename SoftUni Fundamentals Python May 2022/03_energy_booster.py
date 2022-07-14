type_gel = input()
size_gel = input()
count_gel = int(input())
price = 0
if type_gel == 'Watermelon':
    price = 2 * 56
    if size_gel == 'big':
        price = 5 * 28.70
elif type_gel == 'Mango':
    price = 2 * 36.66
    if size_gel == 'big':
        price = 5 * 19.60
elif type_gel == 'Pineapple':
    price = 2 * 42.10
    if size_gel == 'big':
        price = 5 * 24.80
else:
    price = 2 * 20
    if size_gel == 'big':
        price = 5 * 15.20
total_sum = price * count_gel
if total_sum >=400 and total_sum <= 1000:
    total_sum *= 0.85
elif total_sum > 1000:
    total_sum *= 0.50
print(f"{total_sum:.2f} lv.")
