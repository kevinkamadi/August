player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# inch_heights = list()
# print(inch_heights)
# for height in player_heights:
#     inch_height = height * 740
#     inch_heights.append(inch_height)
# print(inch_heights)
print("********************List Comprehension*************************************************")

inch_heights = [height *740 for height in player_heights]
print(inch_heights) 