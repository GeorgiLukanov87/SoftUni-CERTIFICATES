text = input()
new_text = ""
for char in text:
    letter = int(ord(char)) + 3
    letter = chr(letter)
    new_text += letter

print(new_text)