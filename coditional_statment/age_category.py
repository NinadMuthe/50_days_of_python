age = int(input("Enter Your Age :"))

category = ["Invalid age","Child","Teenager","Adult","Senior citizen"]

if age<=0:
    print(category[0])
elif age>0 and age<=12:
    print(f"Category : {category[1]}")
elif age>12 and age<=19:
    print(f"Category : {category[2]}")
elif age>19 and age<=59:
    print(f"Category : {category[3]}")
else:
    print(f"Category : {category[4]}")