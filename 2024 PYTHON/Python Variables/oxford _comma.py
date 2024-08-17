# Converting Types

# In Python, there are a few methods available to us for converting data types. For example, it is possible to convert an integer into a float, a string that represents a number into a number type, and a string into a list or a list into a string, among other conversions. In this lesson we'll learn about converting between lists and strings, but you can learn about more of them in this tutorial on converting data types in Python

# Links to an external site..
# String to List

# To convert a string into a list, we can use the .split

# Links to an external site. method:

# "Hello World!".split()
# # => ["Hello", "World!"]

# The .split method uses whitespace as the separator by default. If we want to use a different separator, we can pass it as an argument:

# "hippo,giraffe,monkey,horse".split(",")
# # => ["hippo", "giraffe", "monkey", "horse"]

# List to String

# We can use Python's .join

# Links to an external site. method to convert a list to a string. The syntax for the command is:

# separator.join(items-to-join)

# The method is called on a string which represents the separator you want to be inserted between each of the items in the list. If you want to join the items into a single string without any separators, you would call the method on an empty string:

# ''.join(["a", "b", "c"])
# # => "abc"

# On the other hand, if we want to separate each item in our list with a " :-) " ("smiley face"), we would do this:

# " :-) ".join(["a", "b", "c"])
# # => "a :-) b :-) c"

# Instructions

# To get started, run pipenv install to create your virtual environment and pipenv shell to enter the virtual environment. Then run pytest -x to run your tests. Use these instructions and pytest's error messages to complete your work in the lib/ folder.

# Write a function oxford_comma() in the lib/oxford_comma.py file that takes an array of string elements as an argument and converts it into a string using the Oxford comma

# Links to an external site..

# oxford_comma(["fiddleheads", "okra", "kohlrabi"])
# # => "fiddleheads, okra, and kohlrabi"

# Hint: You will need to refer to the section above about converting lists into strings, but note that coding this function will involve a couple of extra challenges.

# This might be a challenging lab, so take your time using Google and playing around with your code. Good luck and have fun!