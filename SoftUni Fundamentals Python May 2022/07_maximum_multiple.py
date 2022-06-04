# num1 = int(input())
# num2 = int(input())
# max_num = -100000
# for i in range(num1, num2+1):
#     if not i % num1 == 0:
#         continue
#     if i > max_num:
#         max_num = i
# print(max_num)


# num1 = int(input())
# num2 = int(input())
#
# for i in range(num2, num1 + 1, -1):
#     if i % num1 == 0:
#         print(i)
#         break



divisor = int(input())
bound = int(input())
res = int(bound / divisor) * divisor
print(res)
