# Defining a function
def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

# Calling the function
l = 10
b = 5

area, perimeter = rectangle(l, b)

# Displaying the results
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)