type_motor = input().lower()
current_tank_liters = float(input())


if type_motor == "diesel" or type_motor == 'gasoline' or type_motor == "gas":
    if current_tank_liters >= 25:
        print(f"You have enough {type_motor}.")
    else:
        print(f"Fill your tank with {type_motor}!")

elif not type_motor == "diesel" or type_motor == 'gasoline' or type_motor == "gas":
    print('Invalid fuel!')