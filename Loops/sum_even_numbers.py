n = int(input("Enter N : "))

if n <=0:
    print("Invalid Number")
else:
     total = 0

     for i in range(1, n + 1):
        if i % 2 ==0:
            total += i

     print("Sum of even number = ", total)