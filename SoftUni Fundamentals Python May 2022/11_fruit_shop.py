# banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# '%.2f%'
product = input()
day = input()
quantity = float(input())

if day == 'Saturday' or day == 'Sunday':
    if product == 'banana':
        print('%.2f' % (quantity*2.70))
    elif product == 'apple':
        print('%.2f' % (quantity*1.25))
    elif product == 'orange':
        print('%.2f' % (quantity * 0.90))
    elif product == 'grapefruit':
        print('%.2f' % (quantity * 1.60))
    elif product == 'kiwi':
        print('%.2f' % (quantity * 3.0))
    elif product == 'pineapple':
        print('%.2f' % (quantity * 5.60))
    elif product == 'grapes':
        print('%.2f' % (quantity * 4.20))
    else:
        print('error')
elif day == 'Monday' or day == 'Wednesday' or day == 'Thursday'\
        or day == 'Friday' or day == 'Tuesday':
    if product == 'banana':
        print('%.2f' % (quantity*2.50))
    elif product == 'apple':
        print('%.2f' % (quantity*1.20))
    elif product == 'orange':
        print('%.2f' % (quantity * 0.85))
    elif product == 'grapefruit':
        print('%.2f' % (quantity * 1.45))
    elif product == 'kiwi':
        print('%.2f' % (quantity * 2.70))
    elif product == 'pineapple':
        print('%.2f' % (quantity * 5.50))
    elif product == 'grapes':
        print('%.2f' % (quantity * 3.85))
    else:
        print('error')
else:
    print('error')
