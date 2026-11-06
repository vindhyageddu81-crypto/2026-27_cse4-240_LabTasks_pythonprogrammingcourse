# Check whether a string is a palindrome

str1 = input("Enter a string: ")

if str1 == str1[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
