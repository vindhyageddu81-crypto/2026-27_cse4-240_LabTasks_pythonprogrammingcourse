def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = 24
num2 = 36

print("GCD:", gcd(num1, num2))