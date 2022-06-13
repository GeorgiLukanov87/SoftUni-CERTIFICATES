import math
count_breads = int(input())
max_flour = - 100000000000
max_sugar = - 100000000000
sum_sugar = 0
sum_flour = 0
sugar_packets = 0
flour_packets = 0
for i in range(1, count_breads + 1):
    sugar = int(input())
    flour = int(input())
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour
    sum_sugar += sugar
    sum_flour += flour
sugar_packets = math.ceil(sum_sugar / 950)
flour_packets = math.ceil(sum_flour / 750)
print(f"Sugar: {sugar_packets}")
print(f"Flour: {flour_packets}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
