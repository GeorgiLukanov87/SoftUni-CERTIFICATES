n = int(input())
result = 0
for number in range(1, n+1):
    current_number = int(input())
    result += current_number

print(f'{result/n:.2f}')