from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using map()
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# Using filter()
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# Using reduce()
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)