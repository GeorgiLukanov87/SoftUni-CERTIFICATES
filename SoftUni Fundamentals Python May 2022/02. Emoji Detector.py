import re

regex_pattern1 = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
data = input()
matches = re.findall(regex_pattern1, data)

threshold = 1
for char in data:
    if char.isdigit():
        threshold *= int(char)

cool_emojis = []
for emoji in matches:
    coolness = 0
    for char in emoji[1]:
        coolness += ord(char)

    if coolness > threshold:
        cool_emojis.append(emoji)

print(f'Cool threshold: {threshold}')
if len(matches):
    print(f'{len(matches)} emojis found in the text. The cool ones are:')
    for result in cool_emojis:
        print(''.join(result))
