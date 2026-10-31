#Smallest of Three Numbers using Nested If
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
if num1 <= num2:
    if num1 <= num3:
        result = num1
    else:
        result = num3
else:
    if num2 <= num3:
        result = num2
    else:
        result = num3
print(f"The smallest number is {result} among the numbers {num1}, {num2}, and {num3}.")