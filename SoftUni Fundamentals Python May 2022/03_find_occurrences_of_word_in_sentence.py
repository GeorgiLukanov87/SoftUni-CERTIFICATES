import re

text = input().lower()
searched_word = input().lower()
pattern = fr'\b(?P<searched>{searched_word})\b'

valid_words = re.finditer(pattern, text)
list_of_valid_words = []

for el in valid_words:
    list_of_valid_words.append(el.group('searched'))

print(len(list_of_valid_words))
