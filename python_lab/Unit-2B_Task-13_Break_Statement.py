# Using break statement in for loop

for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("Loop ended")

#using break statement in while loop

i = 1

while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1