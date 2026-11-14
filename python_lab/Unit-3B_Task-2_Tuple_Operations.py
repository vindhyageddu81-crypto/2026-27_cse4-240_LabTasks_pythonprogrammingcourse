# Creating two tuples
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# 1. Concatenation
result = tuple1 + tuple2
print("Concatenation:", result)

# 2. Slicing
print("Slicing:", result[1:4])

# 3. Unpacking
a, b, c = tuple1
print("Unpacking:")
print("a =", a)
print("b =", b)
print("c =", c)