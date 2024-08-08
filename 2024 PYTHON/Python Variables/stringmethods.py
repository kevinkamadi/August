name= "why do you want four real" 
print(len(name))
print(name.upper())
print(name.find('you'))
print(name.replace('four', 'for'))
print('j' in name)
print(name.title())
print(name.count('o'))
print(name.index('do'))
print('**************************************************************************')

is_alpha = name.isalpha()  # Check if all characters are alphabetic
is_digit = name.isdigit()  # Check if all characters are digits
is_alnum = name.isalnum()  # Check if all characters are alphanumeric
is_lower = name.islower()  # Check if all characters are lowercase
is_upper = name.isupper()  # Check if all characters are uppercase
is_space = name.isspace()  # Check if all characters are whitespace
starts = name.startswith("Hello")  # Check if string starts with a substring
ends = name.endswith("World!")  # Check if string ends with a substring
print(is_alpha)
print('**********************************************************************')
words = name.split() #split into a list of words
print(words)
s_joined = " ".join(words)  # Join list into a string with spaces
print(s_joined)