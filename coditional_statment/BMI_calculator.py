weight = float(input("Enter the weight in Kg : "))
hight = float(input("Enter the hight in Meter : "))

BMI = weight/(hight*hight)

if weight <= 0 and hight <= 0:
    print("Enter Valid Wight and Hight")
else:
    if BMI<18.5:
        print(f"BMI : {BMI:.2f}")
        print("Category: Underweight")
    elif BMI>=18.5 or BMI<25:
        print(f"BMI : {BMI:.2f}")
        print("Category: Normal")
    elif BMI>=25 or BMI<30:
        print(f"BMI : {BMI:.2f}")
        print("Category: Overweight")
    else:
        print(f"BMI : {BMI:.2f}")
        print("Category: Obese")

