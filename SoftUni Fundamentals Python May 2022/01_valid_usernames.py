data = input().split(', ')

for word in data:
    valid = ""
    if not(3 <= len(word) <= 16):
        continue

    elif not word.isalnum() and "-" not in word and "_" not in word:
        continue

    valid += word
    print(valid)

