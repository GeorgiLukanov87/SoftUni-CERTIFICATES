n = int(input())

stars = 2 * n
space = 5 * n - 4 * n
slash = 2 * n - 2

print('*' * stars + " " * space + '*' * stars)

for row in range(1, (n - 2) + 1):
    if row == n // 2:
        print('*' + '/' * slash + "*" + "|" * space + '*' + '/' * slash + "*")
    else:
        print('*' + '/' * slash + "*" + " " * space + '*' + '/' * slash + "*")

print('*' * stars + " " * space + '*' * stars)
