n = int(input())
registry = {}
for client in range(n):
    data = input()
    data = data.split()
    action = data[0]

    if action == 'register':
        name = data[1]
        code = data[2]
        if name not in registry:
            registry[name] = code
            print(f"{name} registered {code} successfully")
        else:
            print(f"ERROR: already registered with plate number {code}")

    elif action == 'unregister':
        name = data[1]
        if name not in registry:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del registry[name]

for el in registry:
    print(f'{el} => {registry[el]}')
