print("*****************Default*,*Arguments*,*Kwags***************************************")
# Positional Arguments: Arguments passed in order.
# Default Arguments: Arguments with default values.
# Keyword Arguments: Arguments passed by explicitly naming them.
# *args: Collects extra positional arguments.
# **kwargs: Collects extra keyword arguments.

# Positional Arguments
# def my_name(name, email):
#     print(f"My name is {name}. \nHere is my email: {email}")
# my_name("kevin", "mkamad7@outlook.com")

# Default Arguments
# def my_name(name, email="mkamad7@outlook.com"):
#     print(f"My name is {name}. \nHere is my email: {email}")
# my_name("kevin")

# Keyword Argument
# def my_name(name, email):
#     print(f"My name is {name}. \nHere is my email: {email}")
# my_name(email="mkamad7@outlook.com", name="kevin")

# *Arbitary Arguments
# print("   *Args")
# def my_name(*args):
#     for name in args:
#         print(f"My name is {name}")
# my_name("kevin","mkamad7@outlook.com" )

# Arbitary Keyword Argument
# print("   **Kwargs")
# def my_name(**args):
#     for key, value in args.items():
#         print(f"{key} :{value}")
# my_name(name="Eve", age=29, city="New York" )

# def batch_badge_creator(args):
#     for name in args:
#         print(f'"Hello, my name is {name}."')

# batch_badge_creator(["kevin", "Julia", "Jacky"])

# name =["kevin", "Julia", "Jacky"]
# num = (1,3,2,4)
# namba = [num for i in num]
# print(i)
# def batch_badge_creator(args):
#         i=0
#         for name in args:
#             while i<3:
#              print(f'"Hello, {name}. Your room is Number {i}"')
#             i+=1

# batch_badge_creator(["kevin", "Julia", "Jacky"])

# def batch_badge_creator(args):
#     for i, name in enumerate(args):
#         print(f"Hello, {name}. Your room is Number {10-i}")

# batch_badge_creator(["Kevin", "Julia", "Jacky"])

# for i, num in enumerate(range(10,0,-1)):
#     print(f"Count Down {num}")
    
# print("Take Off")

# countries = ['US', 'GB', 'CA', 'DE']
# for index in range(len(countries)):
#     print(index, countries[index])
def plants(pile):
    planted = []
    for plants in pile:
        pill =planted
        print(f"{plants}!")
plants(["earth", "wind", "fire", "water", "heart"])