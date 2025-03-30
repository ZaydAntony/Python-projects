weight=float(input("Enter your weight: "));
unit= input("Weight in (kg/lbs): ").lower();

def converter():
    global weight, unit # The variables are accessed as global vars.
    if unit == "kg":
        weight= weight * 2.205; #kg to pounds
        print(f"Your weight in pounds is: {weight}");
    elif unit == "lbs":
        weight= weight / 2.205; #pounds to kgs
        print(f"Your weight in Kgs is: {weight}");
    else:
        print("Invalid unit");

converter();