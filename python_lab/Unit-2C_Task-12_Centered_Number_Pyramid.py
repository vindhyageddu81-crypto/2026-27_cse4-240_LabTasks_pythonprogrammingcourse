# Print a centered pyramid pattern of numbers

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()