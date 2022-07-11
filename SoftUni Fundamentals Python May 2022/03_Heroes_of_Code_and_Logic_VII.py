n_heroes = int(input())
heroes = {}
command = input()

for _ in range(n_heroes):
    command = command.split()

    name = command[0]
    hp = int(command[1])
    mp = int(command[2])
    if name not in heroes:
        heroes[name] = [hp] + [mp]
    else:
        heroes[name] += hp
        heroes[name] += mp

    command = input()

while not command == 'End':
    command = command.split(' - ')
    if command[0] == 'CastSpell':
        name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[name][1] >= mp_needed:
            heroes[name][1] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif command[0] == 'TakeDamage':
        name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[name][0] -= damage
        if heroes[name][0] > 0:
            print(f'{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!')
        else:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]

    elif command[0] == 'Recharge':
        name = command[1]
        amount = int(command[2])
        temp_mana = heroes[name][1]
        if temp_mana + amount >= 200:
            heroes[name][1] = 200
            print(f"{name} recharged for {200-temp_mana} MP!")
        else:
            heroes[name][1] += amount
            print(f"{name} recharged for {amount} MP!")

    elif command[0] == 'Heal':
        name = command[1]
        amount = int(command[2])
        temp_health = heroes[name][0]
        if temp_health + amount >= 100:
            heroes[name][0] = 100
            print(f"{name} healed for {100 - temp_health} HP!")
        else:
            heroes[name][0] += amount
            print(f"{name} healed for {amount} HP!")

    command = input()

for hero in heroes:
    print(hero)
    print(f'  HP: {heroes[hero][0]}')
    print(f'  MP: {heroes[hero][1]}')

