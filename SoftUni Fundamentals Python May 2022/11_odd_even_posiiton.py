even_min_number = 100000000000000000000000
odd_min_number = 100000000000000000000000
even_max_number = -1000000000000000000000
odd_max_number = -1000000000000000000000
n = int(input())
even_sum = 0
odd_sum = 0
for i in range(1, n+1):
    number = float(input())
    if i % 2 == 0:
        if number < even_min_number:
            even_min_number = number
        if number > even_max_number:
            even_max_number = number
        even_sum += number
    if i == 0 or n <= 1:
        even_min_number = 0
        even_max_number = 0
    if i % 2 != 0:
        if number < odd_min_number:
            odd_min_number = number
        if number > odd_max_number:
            odd_max_number = number
        odd_sum += number
    if i == 0 or n < 1:
        odd_max_number = 0
        odd_min_number = 0
if n == 0:
    even_min_number = 0
    even_max_number = 0
    odd_max_number = 0
    odd_min_number = 0
print(f"OddSum={odd_sum:.2f},")
if odd_min_number == 0:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min_number:.2f},")
if odd_max_number == 0:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max_number:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min_number == 0:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min_number:.2f},")
if even_max_number == 0:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max_number:.2f}")

