# my_list = ['Cabbage', 'Apple', 'Banana', 'Potato']
# n =  len(my_list)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if my_list[j]>my_list[j+1]:
#             my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
# print(my_list)

digits=[1,7,34,2,9,5,24,3]
# digits.sort()
# print(digits)
n = len(digits)
for i in range(n):
    # print(i)
    for j in range(0, n-i-1):
        # print(j)
        if digits[j]<digits[j+1]:
            digits[j], digits[j+1] = digits[j+1],digits[j]
print(digits)

print("*******************List Methods****************************************")
print("Delete: Pop: Clear: Remove: ")

# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# del(my_list[0])
# print(my_list)

# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# del(my_list[0])
# print(my_list)

# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# del(my_list[0])
# print(my_list)

