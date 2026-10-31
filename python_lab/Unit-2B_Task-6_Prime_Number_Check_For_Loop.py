# Write a python program to check whether a given number is prime or not using for loop
#(assume the input number is between 1 and 100)
n = int(input("Enter a number: "))
# for num in range(1,100):
#     if n in (1,3,5,7):
#         print(f"{n} is a prime number." , num)
#     else:
#         if n % 2 == 0 or n% 3 == 0 or n % 5 == 0 or n % 7 == 0 :
#             print(f"{n} is a not a prime number.")
#         else:
#             print(f"{n} is a prime number.")

# logic2
count = 0

for i in range(1,n+1):  # values from 1 to number (use range)
    if n % 2 != 0:  # does number divide evenly by this value?
        count += 1  # increase count by 1

if n % 2 != 0 or n %3 != 0 or n %5 != 0 or n%7 != 0:  # is count exactly 2?
    print(f"{n} is a prime number (divisor count = {count})")
else:
    print(f"{n} is not a prime number (divisor count = {count})")