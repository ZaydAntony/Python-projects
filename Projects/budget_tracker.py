budget_cash = float(input("Enter your budget cash: "));
print(f"Your current budget is Ksh.{budget_cash}");
print("---------------------------------------------")


budget_items= [];
prices = [];
total = 0.0;


while True:
    user_input = input("Enter budget item (q to quit): ").lower();
    if user_input == "q":
        break;
    price = float(input("Enter item price: "));

    budget_items.append(user_input);
    prices.append(price)

    total += price

for item in budget_items:
    print("-------------------------------------")
    print("You budgeted fo the following");
    print(f"-{item}");
print(f"Your full Total is Ksh.{total}");
print("------------------------------------------------------------------------")

print()
if total > budget_cash:
    print("You are way off budget");
else:
    print("You are on budget");


    
