name = input()

grade = float(input())
counter = 1
result = 0
year = 1

while year < 12:
    result = result + grade
    counter = counter + 1

    if grade >= 4:
        year = year+1
    grade = float(input())

print(f"{name} graduated .Average grade: {(result/counter):.2f}")
