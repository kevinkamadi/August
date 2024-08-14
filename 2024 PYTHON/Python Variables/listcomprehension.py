player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# inch_heights = list()
# print(inch_heights)
# for height in player_heights:
#     inch_height = height * 740
#     inch_heights.append(inch_height)
# print(inch_heights)
print("********************List Comprehension*************************************************")

# inch_heights = [height *740 for height in player_heights]
# print(inch_heights) 

# squared_minus =((n**2)-1 for n in range(2,14))
# print(squared_minus)

# mut =[(i*2) for i in squared_minus]
# print(mut)
k=[0, 1, 3, 5, 7, 8, 9] 
def return_evens(num):
    even=[n for n in num if (n%2==0) ]
    print(even)
return_evens(k)




def make_exclamation(strings):
    for items in strings:
        print(f"{items}!")
make_exclamation([ "Hello", "I'm doing great", "Python is fun"])
