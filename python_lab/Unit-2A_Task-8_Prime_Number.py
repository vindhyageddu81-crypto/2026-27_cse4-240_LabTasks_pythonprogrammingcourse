# To check a number is prime or not
num = int(input("Enter a number: "))
if num >0 and num <= 100:  # number is outside 1 to 100?
    print(f"{num} is not between 1 and 100")
elif num == 1:  # 1 is not prime
    print(f"{num} is not a prime number")
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:  # number is 2, 3, 5, or 7?
    print(f"{num} is a prime number")
else: 
    print(f"{num} is not a prime number")
