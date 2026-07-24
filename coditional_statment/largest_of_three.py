n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

if n1>n2 and n1>n3:
    print(f"{n1} is greater number")
elif n2>n3 and n2>n1:
    print(f"{n2} is greater number")
else:
    print(f"{n3} is greater number")