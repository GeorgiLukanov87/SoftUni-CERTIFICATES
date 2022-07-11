country = input()
discipline = input()
if country == "Bulgaria":
    if discipline == 'ribbon':
        result1 = 9.600
        result2 = 9.400
        total_result = result1 + result2
    elif discipline == 'hoop':
        result1 = 9.550
        result2 = 9.750
        total_result = result1 + result2
    else:
        result1 = 9.500
        result2 = 9.400
        total_result = result1 + result2
elif country == 'Russia':
    if discipline == 'ribbon':
        result1 = 9.100
        result2 = 9.400
        total_result = result1 + result2
    elif discipline == 'hoop':
        result1 = 9.300
        result2 = 9.800
        total_result = result1 + result2
    else:
        result1 = 9.600
        result2 = 9.000
        total_result = result1 + result2
else:
    if discipline == 'ribbon':
        result1 = 9.200
        result2 = 9.500
        total_result = result1 + result2
    elif discipline == 'hoop':
        result1 = 9.450
        result2 = 9.350
        total_result = result1 + result2
    else:
        result1 = 9.700
        result2 = 9.150
        total_result = result1 + result2

print(f"The team of {country} get {total_result:.3f} on {discipline}.")
rest = 20 - total_result
print(f"{(rest/20)*100:.2f}%")