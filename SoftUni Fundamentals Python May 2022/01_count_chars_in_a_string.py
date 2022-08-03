data = input()
new_data = data.replace(" ", "")
data = new_data
my_dict = {}

for word in data:
    for letter in word:
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1

for el in my_dict:
    print(f'{el} -> {my_dict[el]}')
