

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
print("**********names*****************")
# def get_names(food):
#     for food in spicy_foods:
#         print(food["name"])
# get_names(spicy_foods)
print("***************************")


# for food in spicy_foods:
#     if food["heat_level"]>5:
#         foods=[]
#         foods.append(food)
#         print(foods)
print("**********comprehension*****************")
# def get_spiciest_food(foods):
#     foods =[food for food in spicy_foods if food["heat_level"]>5]
#     print(foods)
# get_spiciest_food(spicy_foods)
print("***************************")

# for food in spicy_foods:
#     print(food[])


# def get_spicy_food_by_cuisine(foods, cuisine):
#     for food in foods:
#         if food['cuisine']==cuisine:
#             print(food)
       
# get_spicy_food_by_cuisine(spicy_foods, "American")
print("***************************")

# initial=2
# while initial <2:

def print_spicy_foods(food):
    for food in spicy_foods:
        if food["heat_level"]>5:
            emojis =food["heat_level"] * "🌶"
            print (f'{food["name"]} ({food["cuisine"]}) | Heat Level: {emojis}')
print_spicy_foods(spicy_foods)