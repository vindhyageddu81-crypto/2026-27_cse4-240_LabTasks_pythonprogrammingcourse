# Print numbers in a 3x3 grid

i = 1
num = 1

while i <= 3:
    for j in range(3):
        print(num, end=" ")
        num = num + 1
    print()
    i = i + 1