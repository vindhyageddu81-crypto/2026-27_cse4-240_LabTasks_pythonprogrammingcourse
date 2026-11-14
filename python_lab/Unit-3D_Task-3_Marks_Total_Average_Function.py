# Defining a function
def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

# Calling the function
a = 85
b = 90
c = 95

total, average = calculate_marks(a, b, c)

# Displaying the results
print("Total Marks:", total)
print("Average Marks:", average)