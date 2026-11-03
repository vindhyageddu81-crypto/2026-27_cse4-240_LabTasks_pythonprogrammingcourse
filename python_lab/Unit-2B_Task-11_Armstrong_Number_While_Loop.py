# Program to check Armstrong number
# Assume the number has 3 digits

num = int(input("Enter a 3-digit number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")