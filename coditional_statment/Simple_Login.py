correct_username = "admin"
correct_password = "password123"

entered_username = input("Enter the username : ")
entered_password = input("Enter the password : ")

if entered_username==correct_username and entered_password==correct_password:
    print("Acsess granted")
else:
    print("Enter Correct username and password")