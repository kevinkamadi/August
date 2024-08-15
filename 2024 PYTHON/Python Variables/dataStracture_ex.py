

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]
"🌶"
# for food in spicy_foods:
# #   print(f"{food}")
#   for key, value in food.values():
#       print(f"{value}")

# nested_dict = {
#     "person1": {"name": "Alice", "age": 25},
#     "person2": {"name": "Bob", "age": 30},
# }

# for person, details in nested_dict.items():
#     print(f"{person}:")
#     for key, value in details.items():
#         print(f"  {key}: {value}")
print("***************************")
def get_names(food):
    for food in spicy_foods:
        print(food["name"])
get_names(spicy_foods)