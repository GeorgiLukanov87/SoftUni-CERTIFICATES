data = input().split('\\')

new_data = data[-1]
new_data = new_data.split('.')

name = new_data[0]
extension = new_data[1]

print(f'File name: {name}')
print(f'File extension: {extension}')
