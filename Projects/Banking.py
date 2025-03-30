#Banking system with python
# actions: send, withdaw and deposit
amount = 0
running  = True

def sendmoney():
    global amount
    amount_send=int(input("Enter amount to send: "))
    if amount_send > amount:
        print("Insufficient funds 🤔");
    else:
        amount = amount - amount_send
        print(f"You have sent {amount_send}")
    

def withdraw():
    global amount
    amount_withdraw = int(input("Enter the amount you want to withdraw: "))
    if amount_withdraw > amount:
        print("You have insufficient funds 💔")
    else:
        amount = amount - amount_withdraw
        print(f"You have withdrawn ksh. {amount_withdraw}")

def deposit():
    global amount;
    amount_deposit =  int(input("Enter amount to deposit: "));
    amount += amount_deposit;



while running:
    actions = ["1. Send money", "2. Withdraw", "3. Deposit"];
    print(f"Your current balance is: {amount}");
    print("------------------------------------")

    for action in actions:
        print(action);

    user_choice = input("Pick an action to continue (q to quit): ").lower();
    if user_choice == "1":
        sendmoney();
    elif user_choice == "2":
        withdraw()
    elif user_choice == "3":
        deposit()
    elif user_choice == "q":
        running = False;
    else:
        print("Invalid choice")