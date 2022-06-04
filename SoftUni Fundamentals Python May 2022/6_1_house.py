n = int(input())

is_n_even = n%2==0
range_rows = 0
stars = 1
dash =(n-stars)//2

if is_n_even:
    range_rows = n//2
    stars = 2
else:
    range_rows = n//2 +1

for row in range(0, int(range_rows)):
    print('-'*dash + '*'*stars+'-'*dash)
    stars=stars+2
    dash=(n-stars)//2

other_rows = n - range_rows

for row in range(0 , other_rows):
    print('|' + '*'*(n-2) + '|')
