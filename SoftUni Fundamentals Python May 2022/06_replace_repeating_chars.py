data = input()
letter = [data[0]]

for i in range(1, len(data)):
    if data[i] == letter[-1]:
        continue
    letter.append(data[i])

print(''.join(letter))
