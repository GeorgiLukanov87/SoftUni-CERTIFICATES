total_egg_stock = int(input())
current_egg_stock = total_egg_stock
command = input()
total_sold_egg = 0
condition = True
while command != 'Close':
    status = command
    current_eggs = int(input())
    if status == 'Buy':
        current_egg_stock -= current_eggs
        total_sold_egg += current_eggs
    else:
        current_egg_stock += current_eggs
    if current_egg_stock < 0:
        print(f"Not enough eggs in store!")
        print(f"You can buy only {current_eggs + current_egg_stock}.")
        condition = False
        break
    command = input()
if condition:
    print(f"Store is closed!")
    print(f"{total_sold_egg} eggs sold.")