# sim toolkit first page

safaricom = 1
mpesa = 2

print("---------Welcome to sim toolkit----------")
print("1. Safaricom +")
print("2. Mpesa")

choice = int(input("Select option to proceed (1 or 2): "))

if choice == 1:
    print("""
            1. My Account
            2. M-Banking Services
    
        """)

elif choice == 2:
    print("""
            1. Send Money
            2. Withdraw cash
            3. Buy Airtime
            4. Loans and Savings
            5. Lipa na Mpesa
            6. My Account
        """)
else:
    print("invalid choice")


