gifts_list = input().split(" ")
command = input()

while not command == 'No Money':
    if 'OutOfStock' in command:
        command, gift = command.split(" ")
        for current_gift in range(len(gifts_list)):
            if gifts_list[current_gift] == gift:
                gifts_list[current_gift] = 'None'
    elif 'Required' in command:
        command, gift, index = command.split(" ")
        index = int(index)
        if 0 < index < len(gifts_list):
            gifts_list[index] = gift
    elif 'JustInCase' in command:
        command, gift = command.split(" ")
        gifts_list[-1] = gift
    command = input()

for gifts in range(len(gifts_list)):
    if 'None' in gifts_list:
        gifts_list.remove('None')
print(' '.join(gifts_list))
