#largest among three numbers using nested if else
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a >= b:
    if a >= c:
       result = a
    else:
        result = c
else:
    if b >= c:
        result = b
    else:
        result = c
print(f"{result} is the largest number. among {a}, {b} and {c}.")