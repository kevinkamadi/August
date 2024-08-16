# def fibonacci(**number):
#     for num in number:
#         if num<=1:
#             return number
#     print( fibonacci(number-1) + fibonacci(number+1))
# fibonacci(0,1,2)

num = [2,0,8,3,19,21,4.1]
length = len(num)
print(length)

for i in range(length):
    for j in range(0, length-i-1):
       if num[j] > num[j+1]:
           num[j], num[j+1]=num[j+1], num[j]
print(f"Sorted List: {num}")       