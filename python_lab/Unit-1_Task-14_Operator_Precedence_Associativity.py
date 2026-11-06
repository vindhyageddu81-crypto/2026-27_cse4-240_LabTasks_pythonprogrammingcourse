# Program to demonstrate operator precedence and associativity

a = 10 + 2 * 3
b = (10 + 2) * 3
c = 10 - 5 - 2
d = 2 ** 3 ** 2

print("Operator precedence:", a)
print("Using parentheses:", b)
print("Left to right associativity:", c)
print("Right to left associativity:", d)