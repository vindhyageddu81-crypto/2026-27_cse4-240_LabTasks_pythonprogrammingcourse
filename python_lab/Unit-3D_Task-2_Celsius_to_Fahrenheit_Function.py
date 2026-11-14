# Defining a function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Calling the function
c = 37
result = celsius_to_fahrenheit(c)

# Displaying the result
print("Temperature in Celsius:", c)
print("Temperature in Fahrenheit:", result)