value = int(input())
gift = input()

count_len = 0
first_letter = 0
total_sum = 0
ticket_counter = 0
other_couter = 0
while True:
    count_len = len(gift)
    if gift == "End":
        break
    if count_len > 8:
        for digits, index in enumerate(gift):
            if digits >= 0 and digits < 2:
                first_letter += ord(index)
                total_sum = value - first_letter
        if total_sum >= 0:
            ticket_counter +=1
    elif count_len < 8:
        for digits, index in enumerate(gift):
            if digits == 0:
                first_letter += ord(index)
                total_sum = value - first_letter
        if total_sum > 0:
            other_couter +=1
    if total_sum <= 0:
        break
    gift = input()
print(ticket_counter)
print(other_couter)