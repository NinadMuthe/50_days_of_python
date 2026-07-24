side1 = float(input("Enter first side : "))
side2 = float(input("Enter second side : "))
side3 = float(input("Enter third side : "))

if (side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1):

    if side1 == side2 == side3:
        print("Equilateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isoscales")
    else:
        print("Scalene")
else:
    print("Invalid Tringle")