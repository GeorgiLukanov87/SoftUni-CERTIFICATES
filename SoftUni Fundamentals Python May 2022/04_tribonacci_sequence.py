def tribanacci(sequence: list, number):
    if number > 3:
        for iteration in range(number - 3 + 1):
            num = sum(sequence[-3:])
            sequence.append(num)
        return sequence
    return sequence[:number]

n = int(input())
tribonacci_list = [1, 1]

result = tribanacci(tribonacci_list, n)

print(' '.join(list(map(str, result))))
