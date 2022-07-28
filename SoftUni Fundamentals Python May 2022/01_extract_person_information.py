n = int(input())
key_words = []

for text in range(n):
    string_data = input().split(' ')
    for name in string_data:
        if '@' in name:
            key_words += [name]
    for age in string_data:
        if '#' in age:
            key_words += [age]

    start_index_name = key_words[0].index('@')
    end_index_name = key_words[0].index('|')

    start_index_age = key_words[1].index('#')
    end_index_age = key_words[1].index('*')

    final_name = key_words[0][start_index_name + 1:end_index_name]
    final_age = key_words[1][start_index_age + 1:end_index_age]
    print(f'{final_name} is {final_age} years old.')

    key_words.clear()
