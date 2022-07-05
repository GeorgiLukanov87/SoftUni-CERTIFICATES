numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)
greater_than_average = []

for number in numbers:
    if number > average:
        greater_than_average.append(number)
greater_than_average.sort(reverse=True)
result = greater_than_average
greater_counter = 0

for el in result:
    print(el, end=" ")
    greater_counter += 1
    if greater_counter == 5:
        break

if len(greater_than_average) == 0:
    print('No')