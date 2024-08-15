print("*****************Default*,*Arguments*,*Kwags***************************************")
# Positional Arguments: Arguments passed in order.
# Default Arguments: Arguments with default values.
# Keyword Arguments: Arguments passed by explicitly naming them.
# *args: Collects extra positional arguments.
# **kwargs: Collects extra keyword arguments.

# Positional Arguments
def my_name(name, email):
    print(f"My name is {name}. \nHere is my email: {email}")
my_name("kevin", "mkamad7@outlook.com")

# Default Arguments
def my_name(name, email="mkamad7@outlook.com"):
    print(f"My name is {name}. \nHere is my email: {email}")
my_name("kevin")

# Keyword Argument
def my_name(name, email):
    print(f"My name is {name}. \nHere is my email: {email}")
my_name(email="mkamad7@outlook.com", name="kevin")

# *Arbitary Arguments
print("   *Args")
def my_name(*args):
    for name in args:
        print(f"My name is {name}")
my_name("kevin","mkamad7@outlook.com" )

# Arbitary Keyword Argument
print("   **Kwargs")
def my_name(**args):
    for key, value in args.items():
        print(f"{key} :{value}")
my_name(name="Eve", age=29, city="New York" )
