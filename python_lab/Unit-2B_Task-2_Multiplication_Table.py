# multiplication table
num = int(input("Enter a number: "))
count = int(input("Enter the count: "))
for i in range(1, count + 1):
    print(f"{num} x {i} = {num * i}")
    