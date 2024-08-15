# Sets are the last built-in data structure in Python. Sets share the following characteristics:

# Set elements are unique. Duplicates are not supported.
# Set elements are unordered. This means that they cannot be accessed by index.
# Sets are mutable, but can only store immutable data.
 
set_1= set([1,2,3])
set_2= set([4,8,3])
similar = set_2-set_1
print(similar)

print("*************Comprehension in sets*******************\n")
# it uses curly brackets unlike lists using square brackets
# {expression for item in iterable if condition}
# Can be used to remove duplication.
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = {x for x in numbers}
print(unique_numbers) 

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
unique_consonants = {c.lower() for c in sentence if c not in "aeiou ,."}
print(unique_consonants)