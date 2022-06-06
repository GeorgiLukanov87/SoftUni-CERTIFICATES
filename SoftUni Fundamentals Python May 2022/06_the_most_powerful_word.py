import math
import sys
command = input()
most_points = - sys.maxsize
most_powerful_word = ""
while command != 'End of words':
    current_word = command
    current_word_sum = 0
    for letter in str(current_word):
        current_word_sum += ord(letter)
    first_letter = current_word[0]
    first_letter = first_letter.lower()
    if first_letter == 'a' or first_letter == 'e' or first_letter == 'i' or first_letter == 'o' \
            or first_letter == 'u' or first_letter == 'y':
        current_word_sum *= len(current_word)
    else:
        current_word_sum /= len(current_word)
        current_word_sum = math.floor(current_word_sum)
    if current_word_sum > most_points:
        most_points = current_word_sum
        most_powerful_word = current_word
    command = input()
print(f"The most powerful word is {most_powerful_word} - {most_points}")
