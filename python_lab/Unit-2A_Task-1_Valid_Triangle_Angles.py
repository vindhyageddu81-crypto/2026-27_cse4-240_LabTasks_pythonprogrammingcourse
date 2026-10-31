#3/10/2026 9:41am
A1 = float(input("Enter the first angle of the triangle: "))
A2 = float(input("Enter the second angle of the triangle: "))
A3 = float(input("Enter the third angle of the triangle: "))  
if  A1>0 and A2>0 and A3>0 and A1 + A2 + A3 == 180:
    print(f"The triangle is valid with angles {A1}, {A2}, and {A3}.")
else:
    print(f"The triangle is not valid with angles {A1}, {A2}, and {A3}.")