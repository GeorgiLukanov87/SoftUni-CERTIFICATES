data = input().split(", ")
letter_dict = {}

for i in range(0,len(data)):
    key = data[i]
    value = ord(data[i])
    letter_dict[key] = value

print(letter_dict)