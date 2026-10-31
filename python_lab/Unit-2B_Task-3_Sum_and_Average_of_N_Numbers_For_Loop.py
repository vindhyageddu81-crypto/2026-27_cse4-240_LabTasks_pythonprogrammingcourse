# Sum and Average of N Numbers using For Loop
N = int(input("Enter the value of N other than 0: "))
total = 0
for i in range(1, N + 1):
    num = int(input("enter a number: "))
    if i == 1:
        total = num
    else:
        total += num
average = total / N if N > 0 else 0
print(f"Sum: {total}")
print(f"Average: {average}")