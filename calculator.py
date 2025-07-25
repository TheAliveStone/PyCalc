import math

print("Select an option:")
print("1. Calculator")
print("2. Weight Conversion")
print("3. Temperature Conversion")
print("4. Compound Interest Calculator")
option = int(input())

if option == 1:
    # Calculator project
    while True:
        operator = input("Enter an operator (+, -, *, /, ^, sqrt): ")
        try:
            if operator == "sqrt":
                num1 = float(input("Enter your number: "))
                ans = math.sqrt(num1)
            else:
                num1 = float(input("Enter your first number: "))
                num2 = float(input("Enter your second number: "))
                if operator == "+":
                    ans = num1 + num2
                elif operator == "-":
                    ans = num1 - num2
                elif operator == "*":
                    ans = num1 * num2
                elif operator == "/":
                    ans = num1 / num2
                elif operator == "^":
                    ans = num1 ** num2
                else:
                    print("Your operator is invalid. Please try again")
                    continue
            print(f"The answer is: {ans}")
        except Exception as e:
            print(f"Error: {e}") 
elif option == 2:
    # Weight conversion program
    print("CONVERT YOUR WEIGHT!")
    weight = int(input("Enter your weight (in kilos or pounds): "))
    unit = str(input("Kilos or pounds (type 'kilos' or 'pounds'): "))
    if unit == "kilos":
        ounceChoice = str(input("Do you want to see pounds and ounces? (Y or N): "))
        if ounceChoice == "Y":
            weight = weight / 2.2046226218
            pounds = int(weight)
            ounces = (weight - pounds) * 16
            print(f"You are {weight:.1f} pounds and {ounces:.1f} ounces.")
        elif ounceChoice == "N":
            weight = weight / 2.205
            print(f"You are {weight:.1f} kg. ")
    elif unit == "pounds":
        weight = weight * 2.205
        print(f"You are {weight:.1f} kg. ")
        
elif option == 3:
    pass
elif option == 4:
    pass
else:
    pass

