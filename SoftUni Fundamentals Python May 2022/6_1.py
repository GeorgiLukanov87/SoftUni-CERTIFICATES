n = int(input())

print(" "*(n+1) + "| ")

for row in range(1, n+1):
    print(" "*(n-row) + "*"*row + " | "+'*'*row)

#christmas_tree