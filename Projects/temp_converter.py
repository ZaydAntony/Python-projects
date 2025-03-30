# converting temprature to fahrenheit and vice-versa

temp = float(input("Enter the Temperature: "));
unit = input("Temp in (degrees(c)/fahrenheit(F)): ").lower();

def convert():
    global temp,unit
    if unit =="c":
        temp= (temp * 9)/5 +32
        print(f"Your temperature in fahrenheit is: {temp}F")
    elif unit =="f":
        temp = (temp-32)*5 / 9
        print(f"Your temperature in degrees is: {temp}c")
    else:
        print("Invalid entry");

convert();
