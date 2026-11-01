# Write a python program to print Fibonacci series up to N terms using for loop
n = int(input("Enter how many terms: "))
a = 0
b = 1
print("fibonacci series:")
for i in range(n):
    print(a,end=" ")
    c = a+b
    a = b
    b = c
