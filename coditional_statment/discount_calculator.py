purchase_amount = float(input("Enter the purchase amount : "))


if purchase_amount<0:
    print("Enter Valid amount")
elif purchase_amount>=5000:
    discount = 20
elif purchase_amount<5000 and purchase_amount>=2000:
    discount = 10
elif purchase_amount<2000 and purchase_amount>=1000:
    discount = 5
elif purchase_amount<1000:
    discount = 0
else:
    print("Enter valid amount")

discount_amount = purchase_amount*(discount/100)

print(f"Original Amount: ₹{purchase_amount}")
print(f"Discount: {discount}%")
print(f"Discount Amount: ₹{discount_amount:.2f}")
print(f"Final Amount: ₹{purchase_amount-discount_amount:.2f}")