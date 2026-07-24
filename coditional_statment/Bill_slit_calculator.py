amount = float(input("Enter the total Bill Amount: "))
people = float(input("Enter the total number of people: "))
tip = float(input("Enter the tip percentage: "))

tip_amount = (amount*tip)/100

total = amount+tip_amount

split = total/people

print(f"Each person should pay: {split:.2f}")