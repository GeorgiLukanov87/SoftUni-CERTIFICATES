string = list(input())
numbers_list = []
non_numbers = []
for char in range(len(string)):
    current_char = string[char]
    if not current_char.isdigit():
        non_numbers.append(current_char)
    else:
        numbers_list.append(current_char)
take_list = [int(numbers_list[el]) for el in range(len(numbers_list)) if el % 2 == 0]
skip_list = [int(numbers_list[el]) for el in range(len(numbers_list)) if el % 2 != 0]
taken_string = ""
skipped_string = ""
for iterations in range(len(numbers_list)):
    if len(non_numbers) == 0:
        break
    if iterations % 2 == 0:
        counter = 0
        for add in range(int(numbers_list[iterations])):
            counter += 1
            if add >= len(non_numbers):
                break
            taken_string += non_numbers[add]
        non_numbers = non_numbers[counter:]
    else:
        counter = 0
        for remove in range(int(numbers_list[iterations])):
            counter += 1
            skipped_string += non_numbers[remove]
        non_numbers = non_numbers[counter:]

print(taken_string)
