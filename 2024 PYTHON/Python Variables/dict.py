
# size_to_ounce_map = {
#     "tall": 12,
#     "grande": 16,
#     "venti": 20,
# }
# print(size_to_ounce_map)
# size_to_ounce_map.pop("tall")
# print(size_to_ounce_map)
# # size_to_ounce_map.pop("tall")
# # print(size_to_ounce_map)
# size_to_ounce_map.values()
# print(size_to_ounce_map)
# size_to_ounce_map.items()
# print(size_to_ounce_map)




# software_engineer = {
#     "languages": ["JavaScript", "Python"],
#     "certifications": ["Moringa School Certificate of Completion"],
#     "experience": "3 months and counting!",
# }

# print(software_engineer["languages"][1])


# def pour_coffee(size):
#     size_to_ounce_map = {
#         "tall": 12,
#         "grande": 16,
#         "venti": 20,
#     }
#     return size_to_ounce_map[size]

# print(pour_coffee("tall"))

print("**************************Iterating*a*dictionary**********************")

size_to_ounce_map = {
        "tall": 12,
        "grande": 16,
        "venti": 20,
    }
for key, value in size_to_ounce_map.items():
    print(value)
key_value =[(key) for key, value in size_to_ounce_map.items()]
print(key_value)