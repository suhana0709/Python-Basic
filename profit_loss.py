cp = int(input("Enter the cost price: "))
sp = int(input("Enter the selling price: "))
if cp < sp:
    p = sp - cp
    print("You made profit by ", p)
else:
    print("Its a loss!")