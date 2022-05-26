def collect_function(items, command):
    action, current_item = command.split(' - ')
    if current_item not in items:
        items.append(current_item)
    return items


def drop_function(items, command):
    action, current_item = command.split(' - ')
    if current_item in items:
        items.remove(current_item)
    return items


def combine_item_function(items, old_item, new_item):
    for i in range(len(items)):
        if items[i] == old_item:
            items.insert(i+1, new_item)
    return items


def renew_function(items, command):
    action, current_item = command.split(' - ')
    if current_item in items:
        items.append(current_item)
        items.pop(0)
    return items


item_list = input().split(', ')
command = input()
while not command == 'Craft!':
    if 'Collect' in command:
        collect_function(item_list, command)

    elif 'Drop' in command:
        drop_function(item_list, command)

    elif 'Combine Item' in command:
        result = command.replace('Combine Items - ', "")
        old_item, new_item = result.split(':')
        combine_item_function(item_list, old_item, new_item)

    elif 'Renew' in command:
        renew_function(item_list, command)

    command = input()

print(', '.join(item_list))
