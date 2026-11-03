# Print a right-angled triangle using user input

n = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol to print: ")

for i in range(1, n + 1):
    for j in range(i):
        print(symbol, end=" ")
    print()