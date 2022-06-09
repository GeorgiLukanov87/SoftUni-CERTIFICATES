def is_positive_negative_zero(n1, n2, n3):
    if (n1 > 0 and n2 > 0 and n3 > 0) and (n1 != 0 and n2 != 0 and n3 != 0):
        print('positive')
    elif (n1 < 0 or n2 < 0 or n3 < 0) and (n1 != 0 and n2 != 0 and n3 != 0):
        print('negative')
    else:
        print('zero')


n1 = int(input())
n2 = int(input())
n3 = int(input())

is_positive_negative_zero(n1, n2, n3)
