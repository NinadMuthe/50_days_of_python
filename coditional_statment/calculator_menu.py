num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

print("\n1.Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("\nEnter your choice : "))

if choice == 1:
    print(f"Result: {num1+num2:.2f}")
elif choice == 2:
    print(f"Result: {num1-num2:.2f}")
elif choice == 3:
    print(f"Result: {num1*num2:.2f}")
elif choice == 4:
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"Result: {num1/num2:.2f}")
else:
    print("Invalid Choice ")
