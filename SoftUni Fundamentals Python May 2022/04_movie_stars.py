total_budget = float(input())
command = input()
salary = total_budget
condition = True
while command != 'ACTION':
    current_name = command
    if len(current_name) > 15:
        salary -= salary * 0.20
    else:
        salary -= float(input())
    if salary < 0:
        print(f"We need {abs(salary):.2f} leva for our actors.")
        condition = False
        break
    command = input()
if condition:
    print(f"We are left with {salary:.2f} leva.")