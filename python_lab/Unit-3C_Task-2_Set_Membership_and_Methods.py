# Creating a set
my_set = {10, 20, 30, 40}

print("Original Set:", my_set)

# Membership testing
print("Is 20 present?", 20 in my_set)
print("Is 50 present?", 50 in my_set)

# Adding an element
my_set.add(50)
print("After adding 50:", my_set)

# Removing an element
my_set.remove(30)
print("After removing 30:", my_set)

# Discarding an element
my_set.discard(60)
print("After discarding 60:", my_set)