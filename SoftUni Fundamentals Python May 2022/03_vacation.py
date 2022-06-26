money_need_for_vacation = float(input())
available_money = float(input())
day_counter = 0
spend_counter = 0
condition = False

while available_money < money_need_for_vacation:
    type_of_spending = input()
    current_sum = float(input())
    day_counter += 1
    if type_of_spending == "spend":
        spend_counter += 1
        if spend_counter == 5:
            print(f"You can't save the money.")
            print(f"{day_counter}")
            condition = True
            break

        if current_sum > available_money:
            available_money = 0
        else:
            available_money -= current_sum

    elif type_of_spending == 'save':
        spend_counter = 0
        available_money += current_sum

if not condition:
    print(f"You saved the money for {day_counter} days.")
