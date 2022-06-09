n = int(input())
all_numbers = []
filtered_numbers = []

for i in range(n):
    current_number = int(input())
    all_numbers.append(current_number)

type_of_int = input()

if type_of_int == 'even':
    for number in all_numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)
elif type_of_int == 'odd':
    for number in all_numbers:
        if not number % 2 == 0:
            filtered_numbers.append(number)
elif type_of_int == 'positive':
    for number in all_numbers:
        if number >= 0:
            filtered_numbers.append(number)
else:
    for number in all_numbers:
        if number < 0:
            filtered_numbers.append(number)
print(filtered_numbers)
