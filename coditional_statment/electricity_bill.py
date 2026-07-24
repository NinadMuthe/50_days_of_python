units = float(input("Enter the number of units consumed: "))

if units < 0:
    print("Invalid input")
elif units <= 100:
    bill = units * 1.50
    print("Electricity Bill = ₹", bill)
elif units <= 200:
    bill = units * 2.50
    print("Electricity Bill = ₹", bill)
elif units <= 300:
    bill = units * 4.00
    print("Electricity Bill = ₹", bill)
else:
    bill = units * 6.00
    print("Electricity Bill = ₹", bill)